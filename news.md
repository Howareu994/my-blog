---
layout: page
title: "📢 城市动态"
permalink: /news/
---

{% include news-style.html %}

<div class="dashboard-container">

    <div class="weather-hero">
        <div>
            <div class="weather-temp" id="w-temp">--°C</div>
            <div id="w-desc">打捞信号中...</div>
        </div>
        <div class="weather-info" style="text-align: right; font-size: 13px;">
            <div id="w-wind">💨 风速: -- km/h</div>
            <div id="w-hum">💧 湿度: --%</div>
            <div id="w-time" style="opacity: 0.7; margin-top: 5px;">更新于 --:--</div>
        </div>
    </div>

    <div class="survival-accordion">
        <details>
            <summary>
                <div class="star-title">柏林幸存者手册 (Survival Vademecum)</div>
                <div class="fat-arrow">↓↓↓</div>
            </summary>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px; margin-top: 15px; cursor: default;">
                <div style="font-size: 13px;">
                    <strong style="color: #ff4d94;">🥗 生活补给：性价比周集</strong>
                    <ul style="padding-left: 0; list-style: none; margin-top: 8px;">
                        <li style="margin-bottom: 5px;">📍 <a href="https://www.google.com/maps/search/?api=1&query=Genter+Markt+Berlin" target="_blank">Genter Markt (Wedding) ↗</a></li>
                        <li style="margin-bottom: 5px;">📍 <a href="https://www.google.com/maps/search/?api=1&query=Maybachufer+12047+Berlin" target="_blank">Maybachufer (Neukölln) ↗</a></li>
                        <li style="margin-bottom: 5px;">📍 <a href="https://www.google.com/maps/search/?api=1&query=Crellestrasse+10827+Berlin" target="_blank">Crelle Markt (Schöneberg) ↗</a></li>
                    </ul>
                </div>
                <div style="font-size: 13px;">
                    <strong style="color: #ff4d94;">📦 街道伦理：Zu Verschenken</strong>
                    <p style="font-size: 11px; margin-top: 8px; line-height: 1.5; color: #64748b;">
                        - <strong>警报：</strong> 严禁搬运布艺家具（床垫/沙发）。柏林 <b>Bettwanzen (床虫)</b> 泛滥，一旦入室倾家荡产。<br>
                        - <strong>规则：</strong> 纸箱占道严禁超过 24h。请勿从慈善捐赠箱拿取物品。
                    </p>
                </div>
                <div style="font-size: 13px;">
                    <strong style="color: #ff4d94;">💼 2026 求职猎场</strong>
                    <ul id="job-fair-list" style="padding-left: 0; list-style: none; margin-top: 8px;">
                        <li>正在加载招聘会信息...</li>
                    </ul>
                </div>
            </div>
        </details>
    </div>

    <div class="search-box">
        <input type="text" id="berlin-search" placeholder="在柏林寻找答案 (Google / VBB / Police)...">
    </div>

    <div class="news-grid">
        <div class="news-card">
            <h4 class="tag-vbb"><span>🚆 交通 & 罢工</span> <span class="refresh-btn" onclick="displayTraffic()">🔄</span></h4>
            <ul id="vbb-list"><li>等待打捞...</li></ul>
        </div>

        <div class="news-card">
            <h4 class="tag-safe"><span>🛡️ 安全快讯</span> <span class="refresh-btn" onclick="displayPolice()">🔄</span></h4>
            <ul id="police-list"><li>信号同步中...</li></ul>
        </div>

        <div class="news-card">
            <h4 class="tag-life"><span>🎡 免费活动</span> <span class="refresh-btn" onclick="displayFree()">🔄</span></h4>
            <ul id="free-list"><li>打捞中...</li></ul>
        </div>

        <div class="news-card" style="border-color: rgba(204, 0, 255, 0.2);">
            <h4 class="tag-club"><span>💃 柏林脉搏</span> <span class="refresh-btn" onclick="displayCulture()">🔄</span></h4>
            <ul id="club-list"><li>同步中...</li></ul>
        </div>
    </div>

    <footer class="site-footer-custom">
        <p style="color: #94a3b8; font-size: 11px;">
            数据基于本地情报库同步 · 祝你在柏林幸存
        </p>
    </footer>
</div>

{% include news-script.html %}