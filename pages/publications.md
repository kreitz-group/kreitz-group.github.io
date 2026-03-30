---
layout: default
title: Publications
permalink: /publications/
description: "Publications from the Kreitz Research Group at Georgia Tech"
---

# Publications

{% assign all_pubs = site.data.publications %}
{% assign published = all_pubs | where_exp: "p", "p.preprint != true" %}
{% assign preprints = all_pubs | where: "preprint", true %}

{% assign featured = published | where: "featured", true %}
{% if featured.size > 0 %}
## Featured

<div class="pub-list">
{% for pub in featured %}
{% include publication-card.html pub=pub %}
{% endfor %}
</div>

---
{% endif %}

{% assign group_pubs = published | where: "corresponding_author", true | sort: "year" | reverse %}
{% if group_pubs.size > 0 %}
## Group Publications

<div class="pub-list">
{% for pub in group_pubs %}
{% include publication-card.html pub=pub %}
{% endfor %}
</div>

---
{% endif %}

{% assign other_pubs = published | sort: "year" | reverse %}
{% if other_pubs.size > 0 %}
## All Publications

<div class="pub-list">
{% for pub in other_pubs %}
{% include publication-card.html pub=pub %}
{% endfor %}
</div>
{% endif %}

{% if preprints.size > 0 %}
---

## Preprints

<div class="pub-list">
{% for pub in preprints %}
{% include publication-card.html pub=pub %}
{% endfor %}
</div>
{% endif %}

{% if all_pubs.size == 0 %}
*Publication list will appear here after running `scripts/fetch_publications.py` and `scripts/clean_publications.py`.*
{% else %}
---
*Publication list auto-updated via Semantic Scholar and arXiv. Last updated: {{ site.time | date: "%B %Y" }}.*
{% endif %}
