---
layout: page
title: "🗺️ 生活图鉴"
permalink: /map/
---

<style>
    /* =========================================
       1. 局部色彩变量 (对接你的全局系统)
       ========================================= */
    :root {
        --hot-pink: #ff4d94;
        --border-light: rgba(255, 133, 185, 0.3);
        --text-title: #333333;
        --text-excerpt: #64748b;
        --text-meta: #94a3b8;
    }

    /* =========================================
       2. 列表容器与标题
       ========================================= */
    .gallery-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 10px 0;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }

    .gallery-header {
        color: var(--hot-pink);
        font-size: 1.2rem;
        border-bottom: 2px solid rgba(255, 133, 185, 0.2);
        padding-bottom: 10px;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* =========================================
       3. 日志列表项 (幸存者碎纸片风格)
       ========================================= */
    .post-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }

    .post-item {
        margin-bottom: 25px;
        border-bottom: 1px dashed var(--border-light);
        padding-bottom: 20px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .post-item:hover {
        transform: translateX(8px);
        border-bottom-color: var(--hot-pink); /* 悬停时底边框高亮 */
    }

    /* =========================================
       4. 排版细节 (标题、元数据、摘要)
       ========================================= */
    .post-title {
        font-size: 18px;
        font-weight: 800;
        color: var(--text-title);
        text-decoration: none;
        display: inline-block;
        margin-bottom: 8px;
        transition: color 0.2s;
    }

    .post-title:hover {
        color: var(--hot-pink);
    }

    .post-meta {
        font-size: 12px;
        color: var(--text-meta);
        font-family: "Courier New", monospace;
        font-weight: 600;
    }

    .post-excerpt {
        font-size: 13.5px;
        color: var(--text-excerpt);
        margin-top: 10px;
        line-height: 1.6;
        display: -webkit-box;
        -webkit-line-clamp: 2; /* 严格限制只显示两行 */
        -webkit-box-orient: vertical;
        overflow: hidden;
    }
</style>

<div class="gallery-container">
    <h3 class="gallery-header">
        🖋️ 幸存者日志
    </h3>

    <ul class="post-list">
        <!-- Jekyll 原生循环渲染 -->
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