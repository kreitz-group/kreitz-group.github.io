# Publication Scripts

Two-phase workflow to auto-populate `_data/publications.yml`.

## Setup (first time)

```bash
cd scripts
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...   # add to ~/.zshrc for convenience
```

---

## Phase 1 — `fetch_publications.py`

Queries up to four sources and writes `raw_publications.json`.

| Source | Notes |
|---|---|
| **Semantic Scholar** | Primary. Finds papers by ORCID → author ID. |
| **ORCID** | Authoritative DOI list for cross-checking. |
| **arXiv** | Catches recent preprints not yet in S2. |
| **Google Scholar** | Optional; requires `scholarly`; frequently rate-limited. |

```bash
# Recommended:
python fetch_publications.py --orcid 0000-0001-XXXX-XXXX

# Include arXiv search by author surname:
python fetch_publications.py --orcid 0000-0001-XXXX-XXXX --author-name "Kreitz"

# With Google Scholar:
pip install scholarly
python fetch_publications.py --orcid 0000-0001-XXXX-XXXX --scholar-id SCHOLAR_ID
```

**Output:** `scripts/raw_publications.json`

---

## Phase 2 — `clean_publications.py`

Sends batches to Claude to deduplicate, normalize, and classify, then writes `_data/publications.yml`.

**Claude does:**
- Merges duplicate records (same paper from multiple sources)
- Identifies preprint/published pairs → keeps published version
- Normalizes author strings to `Lastname FM, ...` format
- Cleans journal/venue names

**Local (no Claude tokens):**
- Keyword-based category scores (`catalysis_surface_science`, `data_science`, `computational_chemistry`)
- `corresponding_author` heuristic (DOI present in ORCID list)
- Cross-batch deduplication by DOI/title

```bash
python clean_publications.py

# Dry run (print without writing):
python clean_publications.py --dry-run

# Custom paths:
python clean_publications.py --raw raw_publications.json --output ../_data/publications.yml
```

**Output:** `_data/publications.yml`

---

## Full workflow

```bash
cd scripts
source .venv/bin/activate
python fetch_publications.py --orcid 0000-0001-XXXX-XXXX --author-name "Kreitz"
python clean_publications.py
# Review the diff:
cd ..
git diff _data/publications.yml
# If happy:
git add _data/publications.yml && git commit -m "Update publications"
```

---

## Manual overrides

These fields in `_data/publications.yml` are **never overwritten** on re-runs:

| Field | Default | Purpose |
|---|---|---|
| `featured` | false | Highlight on Publications page |
| `image` | — | Thumbnail from `assets/images/publications/` |
| `corresponding_author` | heuristic | Override if heuristic is wrong |
| `preprint` | Claude | Override if misclassified |
| `abstract` | API | Override with custom text |
| `catalysis_surface_science` | keyword score | 0–1 topic relevance |
| `data_science` | keyword score | 0–1 topic relevance |
| `computational_chemistry` | keyword score | 0–1 topic relevance |

Set them directly in `_data/publications.yml`:
```yaml
- doi: "10.1021/acscatal.2025.xxxxx"
  featured: true
  image: "my_paper_fig.png"
  corresponding_author: true
```
