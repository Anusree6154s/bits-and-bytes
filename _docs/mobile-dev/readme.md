---
layout: default
title: Mobile Dev
permalink: mobile-dev
has_children: true
---

<!-- {% assign child_pages = site.docs | where: "parent", page.title | where_exp: "item", "item.hidden != true" | sort: "date" | reverse %}

{% if child_pages.size > 0 %}   
  <p class="text-gamma text-grey-dk-000 mb-4" style="display:flex; justify-content:space-between;">
    <span>Total Topics: {{ child_pages.size }}</span> <span class="text-delta text-grey-dk-000">Newest → Oldest</span>
  </p>
  <br>

  <ul>
    {% for child in child_pages %}
      <li style="display:flex; justify-content:space-between;">
        <a href="{{ child.url | relative_url }}">{{ child.title }}</a>
        {% if child.date %}
          <span class="text-small text-grey-dk-000">{{ child.date | date: "%d/%m/%Y" }}</span>
        {% endif %}
      </li>
    {% endfor %}
  </ul>
{% endif %} -->