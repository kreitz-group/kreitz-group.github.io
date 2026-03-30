#!/usr/bin/env python3
"""
Phase 1: Fetch raw publication data from multiple sources.

Strategy:
  1. ORCID → authoritative DOI list
  2. Semantic Scholar paper lookup by DOI (avoids rate-limited author/search)
  3. arXiv search by author name (catches recent preprints)

Usage:
  python fetch_publications.py --orcid 0000-0001-XXXX-XXXX --author-name "Kreitz"
  python fetch_publications.py --orcid 0000-0001-XXXX-XXXX  # arXiv search skipped

Output: raw_publications.json
"""

import argparse
import json
import time
import xml.etree.ElementTree as ET
import urllib.parse
import sys

import requests


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def s2_get(url, params=None, retries=4):
    """GET with backoff on 429 (max ~30s total wait)."""
    for attempt in range(retries):
        resp = requests.get(url, params=params, timeout=30)
        if resp.status_code == 429:
            wait = 2 ** attempt * 2
            print(f"    S2 rate limit, waiting {wait}s ...", flush=True)
            time.sleep(wait)
            continue
        resp.raise_for_status()
        return resp
    resp.raise_for_status()


# ---------------------------------------------------------------------------
# ORCID → DOI list
# ---------------------------------------------------------------------------

def orcid_fetch_works(orcid):
    """Return list of (doi, title) pairs from ORCID public API."""
    url = f"https://pub.orcid.org/v3.0/{orcid}/works"
    resp = requests.get(url, headers={"Accept": "application/json"}, timeout=30)
    resp.raise_for_status()
    works = []
    for group in resp.json().get("group", []):
        doi = None
        title = None
        for summary in group.get("work-summary", []):
            if title is None:
                t = summary.get("title", {}).get("title", {}).get("value")
                if t:
                    title = t
            for ext in summary.get("external-ids", {}).get("external-id", []):
                if ext.get("external-id-type") == "doi":
                    doi = ext.get("external-id-value", "").lower().strip()
        if doi or title:
            works.append({"doi": doi, "title": title})
    return works


# ---------------------------------------------------------------------------
# Semantic Scholar: paper lookup by DOI
# ---------------------------------------------------------------------------

S2_FIELDS = "title,authors,year,externalIds,journal,abstract,venue"


def s2_paper_by_doi(doi):
    """Fetch a single paper from S2 using its DOI."""
    url = f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}"
    try:
        resp = s2_get(url, params={"fields": S2_FIELDS})
        return resp.json()
    except requests.HTTPError as exc:
        if exc.response.status_code == 404:
            return None
        raise


def normalize_s2(paper):
    ext = paper.get("externalIds") or {}
    journal = paper.get("journal") or {}
    doi_raw = ext.get("DOI", "")
    return {
        "title": paper.get("title", ""),
        "authors_list": [a.get("name", "") for a in (paper.get("authors") or [])],
        "year": paper.get("year"),
        "doi": doi_raw.lower() if doi_raw else None,
        "arxiv_id": ext.get("ArXiv"),
        "journal": journal.get("name") if journal else paper.get("venue", ""),
        "abstract": paper.get("abstract") or "",
        "source": "semantic_scholar",
        "s2_id": paper.get("paperId"),
    }


# ---------------------------------------------------------------------------
# arXiv search by author name
# ---------------------------------------------------------------------------

def arxiv_fetch(author_name, max_results=200):
    """Fetch recent papers from arXiv by author surname."""
    query = urllib.parse.quote(f'au:"{author_name}"')
    url = (
        f"https://export.arxiv.org/api/query"
        f"?search_query={query}"
        f"&max_results={max_results}"
        f"&sortBy=submittedDate&sortOrder=descending"
    )
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()

    ns = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
    root = ET.fromstring(resp.text)
    papers = []
    for entry in root.findall("atom:entry", ns):
        title_el = entry.find("atom:title", ns)
        summary_el = entry.find("atom:summary", ns)
        id_el = entry.find("atom:id", ns)
        pub_el = entry.find("atom:published", ns)
        if title_el is None or id_el is None:
            continue
        paper = {
            "title": title_el.text.strip().replace("\n", " "),
            "abstract": summary_el.text.strip() if summary_el is not None else "",
            "arxiv_id": id_el.text.split("/abs/")[-1],
            "authors_list": [
                a.find("atom:name", ns).text
                for a in entry.findall("atom:author", ns)
                if a.find("atom:name", ns) is not None
            ],
            "year": int(pub_el.text[:4]) if pub_el is not None else None,
            "source": "arxiv",
            "doi": None,
        }
        doi_el = entry.find("arxiv:doi", ns)
        if doi_el is not None and doi_el.text:
            paper["doi"] = doi_el.text.strip().lower()
        papers.append(paper)
    return papers


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Fetch publications from ORCID + S2 + arXiv")
    parser.add_argument("--orcid", required=True, help="ORCID ID, e.g. 0000-0001-XXXX-XXXX")
    parser.add_argument("--author-name", default="", help="Surname for arXiv search, e.g. 'Kreitz'")
    parser.add_argument("--output", default="raw_publications.json")
    args = parser.parse_args()

    all_papers = []

    # --- 1. ORCID: get authoritative DOI list ---
    print("Fetching works from ORCID ...", flush=True)
    orcid_works = orcid_fetch_works(args.orcid)
    orcid_dois = [w["doi"] for w in orcid_works if w["doi"]]
    print(f"  {len(orcid_works)} works, {len(orcid_dois)} with DOIs")

    # --- 2. Semantic Scholar: look up each DOI ---
    print(f"Fetching {len(orcid_dois)} papers from Semantic Scholar by DOI ...", flush=True)
    s2_found = 0
    for i, doi in enumerate(orcid_dois):
        paper = s2_paper_by_doi(doi)
        if paper and paper.get("paperId"):
            all_papers.append(normalize_s2(paper))
            s2_found += 1
        else:
            # Fall back to ORCID-provided title only
            title = next((w["title"] for w in orcid_works if w["doi"] == doi), None)
            if title:
                all_papers.append({
                    "title": title,
                    "doi": doi,
                    "authors_list": [],
                    "year": None,
                    "journal": "",
                    "abstract": "",
                    "source": "orcid_fallback",
                    "s2_id": None,
                    "arxiv_id": None,
                })
        if (i + 1) % 10 == 0:
            print(f"  {i + 1}/{len(orcid_dois)} ...", flush=True)
        time.sleep(0.2)   # gentle rate limiting
    print(f"  S2 returned data for {s2_found}/{len(orcid_dois)} DOIs")

    # --- 3. arXiv ---
    if args.author_name:
        print(f"Fetching from arXiv (author: {args.author_name!r}) ...", flush=True)
        try:
            arxiv_papers = arxiv_fetch(args.author_name)
            all_papers.extend(arxiv_papers)
            print(f"  {len(arxiv_papers)} papers")
        except Exception as exc:
            print(f"  WARNING: arXiv fetch failed ({exc}); continuing without it", file=sys.stderr)

    result = {
        "papers": all_papers,
        "orcid_dois": orcid_dois,
        "orcid": args.orcid,
    }

    with open(args.output, "w") as fh:
        json.dump(result, fh, indent=2)

    print(f"\nSaved {len(all_papers)} raw records to {args.output}")


if __name__ == "__main__":
    main()
