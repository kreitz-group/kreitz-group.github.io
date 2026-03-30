---
layout: default
title: People
permalink: /people/
description: "Members of the Kreitz Research Group at Georgia Tech"
---

# People

{% assign pi = site.data.people | where: "status", "pi" %}
{% for person in pi %}
<div class="pi-card">
  {% if person.photo and person.photo != "" %}
  <img src="{{ '/assets/images/people/' | append: person.photo | relative_url }}" alt="{{ person.name }}">
  {% else %}
  <div class="person-photo-placeholder">👤</div>
  {% endif %}
  <div class="pi-card-info">
    <h3>{{ person.name }}</h3>
    <p class="person-role">{{ person.role }}</p>
    {% if person.education and person.education != "" %}
    <p class="person-meta"><strong>Education:</strong> {{ person.education }}</p>
    {% endif %}
    {% if person.info and person.info != "" %}
    <p class="person-meta">{{ person.info }}</p>
    {% endif %}
    <div class="person-tag-links">
      {% if person.email and person.email != "" %}
      <a href="mailto:{{ person.email }}" class="btn">Email</a>
      {% endif %}
      {% if person.cv_url and person.cv_url != "" %}
      <a href="{{ person.cv_url | relative_url }}" class="btn">CV</a>
      {% endif %}
      {% if person.google_scholar and person.google_scholar != "" %}
      <a href="{{ person.google_scholar }}" target="_blank" rel="noopener" class="btn">Scholar</a>
      {% endif %}
      {% if person.github and person.github != "" %}
      <a href="{{ person.github }}" target="_blank" rel="noopener" class="btn">GitHub</a>
      {% endif %}
      {% if person.linkedin and person.linkedin != "" %}
      <a href="{{ person.linkedin }}" target="_blank" rel="noopener" class="btn">LinkedIn</a>
      {% endif %}
    </div>
  </div>
</div>
{% endfor %}

---

{% assign graduate = site.data.people | where: "status", "current" | where: "type", "graduate" %}
{% assign undergraduate = site.data.people | where: "status", "current" | where: "type", "undergraduate" %}

{% if graduate.size > 0 %}
## Graduate Students

<div class="person-list">
{% assign graduate_sorted = graduate | sort: "year_joined" | reverse %}
{% for person in graduate_sorted %}
<div class="person-card">
  {% if person.photo and person.photo != "" %}
  <img src="{{ '/assets/images/people/' | append: person.photo | relative_url }}" alt="{{ person.name }}">
  {% else %}
  <div class="person-photo-placeholder">👤</div>
  {% endif %}
  <div class="person-info">
    <h3>{{ person.name }}</h3>
    <p class="person-role">{{ person.role }}</p>
    {% if person.education and person.education != "" %}
    <p class="person-meta"><strong>Education:</strong> {{ person.education }}</p>
    {% endif %}
    {% if person.info and person.info != "" %}
    <p class="person-meta">{{ person.info }}</p>
    {% endif %}
    {% if person.year_joined %}
    <p class="person-meta"><strong>Joined:</strong> {{ person.year_joined }}</p>
    {% endif %}
    <div class="person-tag-links">
      {% if person.email and person.email != "" %}
      <a href="mailto:{{ person.email }}" class="btn">Email</a>
      {% endif %}
      {% if person.github and person.github != "" %}
      <a href="{{ person.github }}" target="_blank" rel="noopener" class="btn">GitHub</a>
      {% endif %}
      {% if person.linkedin and person.linkedin != "" %}
      <a href="{{ person.linkedin }}" target="_blank" rel="noopener" class="btn">LinkedIn</a>
      {% endif %}
    </div>
  </div>
</div>
{% endfor %}
</div>
{% endif %}

{% if undergraduate.size > 0 %}
---

## Undergraduate Researchers

<div class="person-list">
{% assign undergraduate_sorted = undergraduate | sort: "year_joined" | reverse %}
{% for person in undergraduate_sorted %}
<div class="person-card">
  {% if person.photo and person.photo != "" %}
  <img src="{{ '/assets/images/people/' | append: person.photo | relative_url }}" alt="{{ person.name }}">
  {% else %}
  <div class="person-photo-placeholder">👤</div>
  {% endif %}
  <div class="person-info">
    <h3>{{ person.name }}</h3>
    <p class="person-role">{{ person.role }}</p>
    {% if person.education and person.education != "" %}
    <p class="person-meta"><strong>Education:</strong> {{ person.education }}</p>
    {% endif %}
    {% if person.info and person.info != "" %}
    <p class="person-meta">{{ person.info }}</p>
    {% endif %}
    <div class="person-tag-links">
      {% if person.email and person.email != "" %}
      <a href="mailto:{{ person.email }}" class="btn">Email</a>
      {% endif %}
      {% if person.github and person.github != "" %}
      <a href="{{ person.github }}" target="_blank" rel="noopener" class="btn">GitHub</a>
      {% endif %}
      {% if person.linkedin and person.linkedin != "" %}
      <a href="{{ person.linkedin }}" target="_blank" rel="noopener" class="btn">LinkedIn</a>
      {% endif %}
    </div>
  </div>
</div>
{% endfor %}
</div>
{% endif %}

{% assign alumni = site.data.people | where: "status", "alumni" %}
{% if alumni.size > 0 %}
---

## Alumni

<div class="alumni-grid">
{% assign alumni_sorted = alumni | sort: "year_joined" | reverse %}
{% for person in alumni_sorted %}
<div class="alumni-card">
  <h4>{{ person.name }}</h4>
  <p class="person-role">{{ person.role }}</p>
  {% if person.current_position and person.current_position != "" %}
  <p class="person-meta">Now: {{ person.current_position }}</p>
  {% endif %}
  {% if person.linkedin and person.linkedin != "" %}
  <div style="margin-top: 0.5em;">
    <a href="{{ person.linkedin }}" target="_blank" rel="noopener" class="btn">LinkedIn</a>
  </div>
  {% endif %}
</div>
{% endfor %}
</div>
{% endif %}
