import feedparser
import json
import os
import ssl
import socket

# 1. 解决 SSL 验证问题（部分服务器抓取 HTTPS 必备）
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

# 设置超时时间，防止某个链接卡死导致整个 Action 失败
socket.setdefaulttimeout(15)

# scripts/fetch_news.py 里的 FEEDS 修改如下：

FEEDS = {
    "traffic": "https://www.rbb24.de/aktuell/index.xml/feed=rss.xml",
    "police": "https://www.berlin.de/polizei/polizeimeldungen/index.php/rss",
    
    # 修改 1：使用 berlin.de 更通用的票务/活动 RSS (包含很多免费演出)
    "free_events": "https://www.berlin.de/tickets/suche/rss/",
    
    # 修改 2：舍弃不稳定的 RSSHub，直接抓取 Siegessäule 的原生信号
    "music_nightlife": "https://www.siegessaeule.de/rss.xml",
    
    # 修改：抓取招聘会相关信息 (利用 Berlin.de 的经济/就业 RSS)
    "job_fairs": "https://www.berlin.de/wirtschaft/rss/",
    
    # 修改：抓取街道生活/社区规则相关的文章
    "ethics": "https://www.tip-berlin.de/stadtleben/rss/"
    
}
def fetch_feed(category, url, limit=10):
    print(f"📡 正在打捞 {category} 信号...")
    # 伪装成浏览器，防止被网站屏蔽
    agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    
    try:
        # 使用 feedparser 抓取
        feed = feedparser.parse(url, agent=agent)
        
        # 检查是否抓取成功
        if feed.bozo:
            print(f"⚠️ {category} 信号解析异常，尝试强制提取...")

        items = []
        for entry in feed.entries[:limit]:
            items.append({
                "title": entry.title,
                "link": entry.link,
                "date": entry.get('published', entry.get('updated', ''))
            })
        print(f"✅ {category} 打捞成功: {len(items)} 条")
        return items
    except Exception as e:
        print(f"❌ {category} 信号中断: {str(e)}")
        return []

def main():
    news_data = {}
    for category, url in FEEDS.items():
        news_data[category] = fetch_feed(category, url)
    
    # 确保 data 文件夹存在
    os.makedirs('data', exist_ok=True)
    
    # 写入 JSON，确保中文不乱码
    with open('data/news.json', 'w', encoding='utf-8') as f:
        json.dump(news_data, f, ensure_ascii=False, indent=2)
    print("\n📦 所有情报已存入 data/news.json")

if __name__ == "__main__":
    main()