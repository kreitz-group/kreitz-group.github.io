---
layout: default
title: Photos
permalink: /photos/
description: "Photos from the Kreitz Research Group"
---

# Photos

{% if site.data.photos.size > 0 %}
{% assign sorted_photos = site.data.photos | sort: "date" | reverse %}
<div class="photo-grid">
{% for item in sorted_photos %}
<figure class="photo-item">
  <img src="{{ '/assets/images/photos/' | append: item.image | relative_url }}"
       alt="{{ item.caption | default: 'Group photo' }}">
  {% if item.caption and item.caption != "" %}
  <figcaption class="photo-caption">
    {{ item.caption }}{% if item.date %} <span class="photo-date">&middot; {{ item.date | date: '%b %Y' }}</span>{% endif %}
  </figcaption>
  {% elsif item.date %}
  <figcaption class="photo-caption">{{ item.date | date: '%b %Y' }}</figcaption>
  {% endif %}
</figure>
{% endfor %}
</div>
{% else %}
*Group photos will appear here. Add files to `assets/images/photos/` and entries to `_data/photos.yml`.*
{% endif %}
