import feedparser
import json
import os
import ssl
import socket
import random
import time
from urllib.parse import urljoin

# 1. 解决 SSL 验证问题
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

# 设置超时时间（增加到 30 秒，适应柏林政府服务器的缓慢响应）
socket.setdefaulttimeout(30)

# --- 2. 信号源阵列化 (Multi-Source Array) ---
FEEDS = {
    "traffic": [
        "https://www.rbb24.de/aktuell/index.xml/feed=rss.xml",
        "https://www.viz-berlin.de/aktuelles/-/rss/viz/all/",
        "https://www.vbb.de/vbb-services/presse/pressemitteilungen/rss/"
    ],
    "police": [
        "https://www.berlin.de/polizei/polizeimeldungen/index.php/rss",
        "https://www.presseportal.de/rss/dienststelle_4943.rss2"
    ],
    "free_events": [
        "https://www.berlin.de/tickets/suche/rss/",
        "https://www.exberliner.com/events/feed/"
    ],
    "music_nightlife": [
        "https://www.siegessaeule.de/rss.xml",
        "https://www.tip-berlin.de/stadtleben/feed/"
    ],
    "job_fairs": [
        "https://www.berlin.de/wirtschaft/rss/",
        "https://www.berlin.de/sen/arbeit/presse/pressemitteilungen/index.php/rss"
    ],
    "ethics": [
        "https://www.tip-berlin.de/stadtleben/rss/",
        "https://www.rbb24.de/panorama/index.xml/feed=rss.xml"
    ]
}

def fetch_feed(category, url, limit=12):
    """
    增强型打捞函数：支持深度伪装与链接修复
    """
    print(f"📡 正在接入频率: {url} ...")

    # 模拟真实浏览器请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "application/rss+xml, application/xml;q=0.9, */*;q=0.8",
        "Referer": "https://www.google.com/",
        "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8"
    }

    try:
        # 正确使用 request_headers 进行伪装
        feed = feedparser.parse(url, request_headers=headers)

        # 状态检查
        status = getattr(feed, 'status', None)
        if status and status != 200:
            print(f"❌ 握手失败 (HTTP {status})")
            return []

        items = []
        for entry in feed.entries[:limit]:
            # 自动修复链接：将相对路径转换为绝对路径
            raw_link = entry.link
            clean_link = urljoin(url, raw_link)

            items.append({
                "title": entry.title,
                "link": clean_link,
                "date": entry.get('published', entry.get('updated', ''))
            })

        print(f"✅ {category} 频道子信号打捞成功: {len(items)} 条")
        return items
    except Exception as e:
        print(f"💥 信号中断: {str(e)}")
        return []

def main():
    news_data = {}

    for category, urls in FEEDS.items():
        all_items = []
        # 处理单字符串或列表
        url_list = [urls] if isinstance(urls, str) else urls

        for url in url_list:
            # 随机延迟，防止由于抓取过快被封 IP
            time.sleep(random.uniform(1.5, 3.0))
            items = fetch_feed(category, url)
            all_items.extend(items)

        # --- 信号去重 (基于标题) ---
        unique_items = []
        seen_titles = set()
        for item in all_items:
            if item['title'] not in seen_titles:
                unique_items.append(item)
                seen_titles.add(item['title'])

        # 按打捞到的顺序保留前 15 条最相关的
        news_data[category] = unique_items[:15]

    # 确保 data 文件夹存在
    os.makedirs('data', exist_ok=True)

    # 写入 JSON
    with open('data/news.json', 'w', encoding='utf-8') as f:
        json.dump(news_data, f, ensure_ascii=False, indent=2)

    print(f"\n📦 [打捞任务完成] 情报已存入 data/news.json，共覆盖 {len(news_data)} 个频道。")

if __name__ == "__main__":
    main()