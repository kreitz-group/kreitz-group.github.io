---
layout: default
title: Home
description: "Computational chemistry research at Georgia Institute of Technology"
---

# Kreitz Research Group

We are a computational and experimental catalysis research group at the [School of Chemical & Biomolecular Engineering](https://chbe.gatech.edu) at Georgia Tech. Our work combines quantum chemistry, multiscale modeling, and kinetic experiments to unravel the detailed chemical kinetics of complex heterogeneously catalyzed reactions.

## Research Overview


We develop and apply computational methods in combination with experiments to address fundamental questions in heterogeneous catalysis. Key areas include:

- **Heterogeneous catalysis** — understanding reaction mechanisms on surfaces from first principles
- **Automated mechanism generation** — accelerating the development of detailed chemical kinetic models of catalytic reactions
- **Multiscale modeling** — connecting molecular-scale insights to macroscopic reactor performance

Visit the [Research](/research/) page for more detail.

## News

{% if site.data.news.size > 0 %}
{% assign sorted_news = site.data.news | sort: "date" | reverse %}
<ul class="news-list">
{% for item in sorted_news limit: 3 %}
  <li class="news-item">
    <span class="news-date">{{ item.date | date: "%b %-d, %Y" }}</span>
    <div class="news-body">
      {{ item.body | markdownify }}
      {% if item.link and item.link != "" %}
      <a href="{{ item.link }}" target="_blank" rel="noopener"><span class="visually-hidden">Read more about: {{ item.body | markdownify | strip_html | strip_newlines | truncate: 70 }} (opens in a new tab)</span><span aria-hidden="true">&rarr;</span></a>
      {% endif %}
    </div>
  </li>
{% endfor %}
</ul>

[See all news &rarr;](/news/)
{% else %}
*News coming soon.*
{% endif %}

---

**Contact:** {{ site.pi.email }}
**Office:** [Georgia Institute of Technology](https://gatech.edu), Atlanta, GA


