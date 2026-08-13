---
layout: default
title: Tools
permalink: /tools/
description: "Software tools developed by the Kreitz Research Group"
---

# Tools

Software developed by or contributed to by our group.

{% if site.data.repos.size > 0 %}
## Open-Source Software

<div class="repo-grid">
{% for repo in site.data.repos %}
<div class="repo-card">
  <h3><a href="{{ repo.url }}" target="_blank" rel="noopener">{{ repo.name }}<span class="visually-hidden"> (opens in a new tab)</span></a></h3>
  {% if repo.description and repo.description != "" %}
  <p>{{ repo.description }}</p>
  {% endif %}
  <div class="person-tag-links">
    <a href="{{ repo.url }}" target="_blank" rel="noopener" class="btn">GitHub<span class="visually-hidden"> repository for {{ repo.name }} (opens in a new tab)</span> <span aria-hidden="true">&rarr;</span></a>
    {% if repo.docs_url and repo.docs_url != "" %}
    <a href="{{ repo.docs_url }}" target="_blank" rel="noopener" class="btn">Docs<span class="visually-hidden"> for {{ repo.name }} (opens in a new tab)</span> <span aria-hidden="true">&rarr;</span></a>
    {% endif %}
  </div>
</div>
{% endfor %}
</div>
{% else %}
*Software tools will be listed here. Add entries to `_data/repos.yml`.*
{% endif %}
