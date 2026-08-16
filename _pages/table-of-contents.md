---
permalink: /all-posts
layout: default
nav_order: 3
title: Table Of Contents
nav_exclude: true
---

<div class="toc-container">
  <div class="toc-post-list">
    {% assign active_posts = site.docs | where_exp: "post", "post.hidden != true" | sort: "date" | reverse %}
    
    <div class="toc-meta-header">
      <p class="toc-total-count"><span>Total Posts: {{ active_posts.size }}</span></p>
      <span class="toc-sort-badge">Sorted: Newest → Oldest</span>
    </div>

    <div class="toc-list">
      {% for post in active_posts %}
        <a href="{{ post.url | relative_url }}" class="toc-item">
          <div class="toc-item-main">
            <div class="toc-item-header">
              <p class="toc-item-title">{{ post.title }}</p>
              {% if post.date %}
                <span class="toc-item-date">{{ post.date | date: "%d/%m/%Y" }}</span>
              {% endif %}
            </div>

            {% if post.excerpt %}
              <p class="toc-item-excerpt">{{ post.excerpt | strip_html | truncatewords: 20 }}</p>
            {% endif %}

            {% if post.tags.size > 0 %}
              <div class="toc-item-tags">
                <span class="toc-tag-label">TAGS:</span>
                <span class="toc-tag-list">{{ post.tags | join: ', ' | escape }}</span>
              </div>
            {% endif %}
          </div>
        </a>
      {% endfor %}
    </div>
  </div>
</div>

<style>
.toc-container {
  margin: 1.5rem 0;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}

.toc-meta-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.25rem;
  gap: 1rem;
}

.toc-total-count {
  margin: 0;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: #f472b6;
}

.toc-sort-badge {
  font-size: 0.7rem;
  font-weight: 600;
  color: #64748b;
  background-color: #f1f5f9;
  padding: 0.2rem 0.55rem;
  border-radius: 12px;
  border: 1px solid #e2e8f0;
  white-space: nowrap;
}

.toc-list {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.toc-item {
  display: block;
  padding: 0.85rem 1rem;
  border-radius: 8px;
  background: transparent;
  text-decoration: none;
  transition: background-color 0.15s ease;
}

.toc-item:hover {
  background-color: #f8fafc;
}

.toc-item-main {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
}

.toc-item-header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 1rem;
}

.toc-item-title {
  margin: 0;
  font-size: 0.95rem;
  font-weight: 600;
  color: #0f172a;
  line-height: 1.35;
  transition: color 0.15s ease;
}

.toc-item:hover .toc-item-title {
  color: #ec4899;
}

.toc-item-date {
  font-size: 0.75rem;
  font-weight: 500;
  color: #94a3b8;
  white-space: nowrap;
}

.toc-item-excerpt {
  margin: 0;
  font-size: 0.82rem;
  color: #64748b;
  line-height: 1.5;
}

.toc-item-tags {
  margin-top: 0.2rem;
  font-size: 0.7rem;
  display: flex;
  align-items: center;
  gap: 0.35rem;
}

.toc-tag-label {
  font-weight: 700;
  color: #cbd5e1;
  letter-spacing: 0.03em;
}

.toc-tag-list {
  color: #94a3b8;
}

@media (max-width: 500px) {
  .toc-item-header {
    flex-direction: column;
    gap: 0.15rem;
  }
}
</style>