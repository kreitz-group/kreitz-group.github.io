---
layout: default
title: Home
description: "Computational chemistry research at Georgia Institute of Technology"
---

<!-- The masthead already shows the group name, so the page title is not
     repeated visually. It stays in the markup, first and readable by screen
     readers and search engines, so the page still has an h1 and the heading
     order does not jump straight to h2. -->
# Kreitz Research Group
{: .visually-hidden}

<figure class="hero-figure">
  <img src="{{ '/assets/images/home/group-hero.jpg' | relative_url }}"
       alt="The Kreitz research group photographed together on the Georgia Tech campus, spring 2026."
       width="1800" height="1206">
</figure>

We are a computational and experimental catalysis research group at the [School of Chemical & Biomolecular Engineering](https://chbe.gatech.edu) at Georgia Tech. Our work combines quantum chemistry, multiscale modeling, and kinetic experiments to unravel the detailed chemical kinetics of complex heterogeneously catalyzed reactions.
{: .lede}

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


