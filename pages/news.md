---
layout: default
title: News
permalink: /news/
description: "News and announcements from the Kreitz Research Group"
---

# News

{% if site.data.news.size > 0 %}
  {% assign sorted_news = site.data.news | sort: "date" | reverse %}
  {% assign current_year = "" %}
  {% for item in sorted_news %}
    {% assign year = item.date | date: "%Y" %}
    {% if year != current_year %}
      {% unless forloop.first %}
  </ul>
      {% endunless %}
## {{ year }}
<ul class="news-list">
      {% assign current_year = year %}
    {% endif %}
  <li class="news-item">
    <span class="news-date">{{ item.date | date: "%b %-d" }}</span>
    <div class="news-body">
      {{ item.body | markdownify }}
      {% if item.link and item.link != "" %}
      <a href="{{ item.link }}" target="_blank" rel="noopener"><span class="visually-hidden">Read more about: {{ item.body | markdownify | strip_html | strip_newlines | truncate: 70 }} (opens in a new tab)</span><span aria-hidden="true">&rarr;</span></a>
      {% endif %}
      {% if item.image and item.image != "" %}
      <img class="news-image" src="{{ '/assets/images/news/' | append: item.image | relative_url }}" alt="{{ item.image_alt | default: '' }}">
      {% endif %}
    </div>
  </li>
    {% if forloop.last %}
  </ul>
    {% endif %}
  {% endfor %}
{% else %}
*News items will appear here. Add entries to `_data/news.yml`.*
{% endif %}
