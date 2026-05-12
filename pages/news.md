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
      <a href="{{ item.link }}" target="_blank" rel="noopener">&rarr;</a>
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
