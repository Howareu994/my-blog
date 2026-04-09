---
layout: page
title: "🎞️ 生活图鉴"
permalink: /gallery/
---

<style>
    /* 专属的排版样式 */
    .gallery-container { max-width: 800px; margin: 0 auto; padding: 10px 0; font-family: 'Helvetica Neue', sans-serif; }
    
    /* 日记列表样式 */
    .post-list { list-style: none; padding: 0; margin: 0; }
    .post-item { margin-bottom: 25px; border-bottom: 1px dashed rgba(255, 133, 185, 0.3); padding-bottom: 20px; transition: transform 0.2s ease; }
    .post-item:hover { transform: translateX(5px); }
    
    /* 文章标题 */
    .post-title { font-size: 20px; font-weight: bold; color: #333; text-decoration: none; display: block; margin-bottom: 8px; transition: color 0.2s; }
    .post-title:hover { color: #ff4d94; }
    
    /* 日期和摘要 */
    .post-meta { font-size: 12px; color: #94a3b8; font-family: monospace; }
    .post-excerpt { font-size: 14px; color: #64748b; margin-top: 10px; line-height: 1.6; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
</style>

<div class="gallery-container">
    <h3 style="color: #ff4d94; border-bottom: 2px solid rgba(255, 133, 185, 0.2); padding-bottom: 10px; margin-bottom: 20px;">
        🖋️ 幸存者日志
    </h3>

    <ul class="post-list">
        {% for post in site.posts %}
        <li class="post-item">
            <a class="post-title" href="{{ post.url | relative_url }}">{{ post.title }}</a>
            <div class="post-meta">🕒 {{ post.date | date: "%Y年 %m月 %d日" }}</div>
            <div class="post-excerpt">
                {{ post.excerpt | strip_html }}
            </div>
        </li>
        {% endfor %}
    </ul>
</div>