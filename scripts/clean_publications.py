#!/usr/bin/env python3
"""
Phase 2: Clean and deduplicate raw publication records using Claude.

Usage:
  python clean_publications.py
  python clean_publications.py --dry-run
  python clean_publications.py --raw raw_publications.json --output ../_data/publications.yml

Requires ANTHROPIC_API_KEY environment variable.
"""

import argparse
import json
import os
import sys

import anthropic
import yaml


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BATCH_SIZE = 40   # papers per Claude call (stay under token limits)

SYSTEM_PROMPT = """You are a research publication curator. You receive a JSON array of raw publication
records fetched from Semantic Scholar, ORCID, and arXiv. Your tasks:

1. **Deduplicate**: merge records that refer to the same paper (identical or near-identical titles, same DOI).
2. **Resolve preprint/published pairs**: when the same work appears as both an arXiv preprint and a
   journal article, keep the journal version with preprint=false. Set preprint=true only when no
   published version exists.
3. **Normalize authors**: convert author strings to "Lastname FM, Lastname2 FM2, ..." format.
4. **Clean venues**: expand common abbreviations, remove "Proceedings of the" prefixes, standardize
   journal names.

Return ONLY a valid JSON array. Each element must have these fields (use null when unknown):
  title          (string)
  authors        (string, normalized)
  journal        (string or null)
  year           (integer or null)
  doi            (string, lowercase, no "https://doi.org/" prefix, or null)
  url            (string — prefer DOI URL; fall back to arXiv URL)
  arxiv_id       (string or null)
  abstract       (string or null)
  preprint       (boolean)

No commentary, no markdown fences — raw JSON array only."""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

MANUAL_FIELDS = {
    "featured", "image", "corresponding_author", "preprint", "abstract",
    "catalysis_surface_science", "data_science", "computational_chemistry",
}


def load_existing(path: str) -> dict[str, dict]:
    """Load existing publications.yml indexed by DOI to preserve manual fields."""
    if not os.path.exists(path):
        return {}
    with open(path) as fh:
        data = yaml.safe_load(fh) or []
    return {p["doi"].lower(): p for p in data if p.get("doi")}


def preserve_manual(pub: dict, existing: dict[str, dict]) -> dict:
    doi = (pub.get("doi") or "").lower().strip()
    if doi and doi in existing:
        for field in MANUAL_FIELDS:
            if field in existing[doi]:
                pub.setdefault(field, existing[doi][field])
    return pub


CATALYSIS_KW = [
    "catalysis", "catalyst", "surface", "adsorption", "tof", "turnover",
    "sabatier", "volcano", "heterogeneous", "active site", "nitrogen",
    "ammonia", "oxidation", "hydrogenation", "zeolite", "metal oxide",
]
DATA_KW = [
    "machine learning", "neural network", "deep learning", "data science",
    "artificial intelligence", "regression", "prediction", "language model",
    "transformer", "graph neural", "gnn", "nlp", "large language",
]
COMP_KW = [
    "dft", "density functional", "electronic structure", "ab initio",
    "force field", "molecular dynamics", "monte carlo", "microkinetic",
    "first principles", "quantum chemistry", "simulation", "kinetic monte",
]


def kw_score(text: str, keywords: list[str]) -> float:
    count = sum(1 for kw in keywords if kw in text)
    return min(1.0, round(count / max(3, len(keywords) * 0.3), 2))


def category_scores(pub: dict) -> dict:
    text = " ".join(filter(None, [
        pub.get("title", ""),
        pub.get("abstract") or "",
        pub.get("journal") or "",
    ])).lower()
    return {
        "catalysis_surface_science": kw_score(text, CATALYSIS_KW),
        "data_science": kw_score(text, DATA_KW),
        "computational_chemistry": kw_score(text, COMP_KW),
    }


def is_corresponding(pub: dict, orcid_dois: set[str]) -> bool:
    doi = (pub.get("doi") or "").lower().strip()
    return bool(doi and doi in orcid_dois)


def clean_batch(client: anthropic.Anthropic, batch: list[dict]) -> list[dict]:
    resp = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=8192,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": json.dumps(batch)}],
    )
    text = resp.content[0].text.strip()
    # Strip accidental markdown fences
    if text.startswith("```"):
        text = "\n".join(text.split("\n")[1:])
        text = text.rsplit("```", 1)[0].strip()
    return json.loads(text)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Clean publications with Claude")
    parser.add_argument("--raw", default="raw_publications.json")
    parser.add_argument("--output", default="../_data/publications.yml")
    parser.add_argument("--dry-run", action="store_true", help="Print YAML without writing")
    args = parser.parse_args()

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: set ANTHROPIC_API_KEY environment variable", file=sys.stderr)
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    with open(args.raw) as fh:
        raw = json.load(fh)

    papers: list[dict] = raw.get("papers", [])
    orcid_dois: set[str] = {d.lower() for d in raw.get("orcid_dois", [])}
    print(f"Loaded {len(papers)} raw records, {len(orcid_dois)} ORCID DOIs")

    existing = load_existing(args.output)
    print(f"Loaded {len(existing)} existing entries (for manual-override preservation)")

    # --- Claude cleaning in batches ---
    cleaned: list[dict] = []
    total_batches = (len(papers) + BATCH_SIZE - 1) // BATCH_SIZE
    for i in range(0, len(papers), BATCH_SIZE):
        batch_num = i // BATCH_SIZE + 1
        batch = papers[i : i + BATCH_SIZE]
        print(f"Cleaning batch {batch_num}/{total_batches} ({len(batch)} papers) ...", flush=True)
        try:
            result = clean_batch(client, batch)
            cleaned.extend(result)
        except Exception as exc:
            print(f"  WARNING: batch {batch_num} failed: {exc}", file=sys.stderr)

    print(f"Claude returned {len(cleaned)} cleaned records")

    # --- Cross-batch deduplication by DOI, then by title ---
    seen_dois: set[str] = set()
    seen_titles: set[str] = set()
    deduped: list[dict] = []
    for pub in cleaned:
        doi = (pub.get("doi") or "").lower().strip()
        title = (pub.get("title") or "").lower().strip()
        if doi:
            if doi not in seen_dois:
                seen_dois.add(doi)
                deduped.append(pub)
        elif title:
            if title not in seen_titles:
                seen_titles.add(title)
                deduped.append(pub)
    print(f"After deduplication: {len(deduped)} papers")

    # --- Enrich ---
    final: list[dict] = []
    for pub in deduped:
        scores = category_scores(pub)
        for k, v in scores.items():
            pub.setdefault(k, v)
        pub.setdefault("corresponding_author", is_corresponding(pub, orcid_dois))
        pub = preserve_manual(pub, existing)
        final.append(pub)

    # Sort newest first
    final.sort(key=lambda p: p.get("year") or 0, reverse=True)

    if args.dry_run:
        print(yaml.dump(final, allow_unicode=True, sort_keys=False))
    else:
        out_dir = os.path.dirname(os.path.abspath(args.output))
        os.makedirs(out_dir, exist_ok=True)
        with open(args.output, "w") as fh:
            yaml.dump(final, fh, allow_unicode=True, sort_keys=False)
        print(f"Written {len(final)} publications to {args.output}")


if __name__ == "__main__":
    main()
