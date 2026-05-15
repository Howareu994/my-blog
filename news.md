---
layout: page
title: "📢 城市动态"
permalink: /news/
---

{% include news-style.html %}

<style>
    /* --- 1. 核心变量 (黑客色调) --- */
    :root {
        --terminal-black: #0a0a0a;
        --hot-pink: #ff4d94;
        --matrix-green: #00ff41;
        --deep-blue: #00008B;
        --bg-pink: #ffdae9;
    }

    * { border-radius: 0 !important; }
    html, body { margin: 0 !important; padding: 0 !important; background-color: var(--bg-pink); }

    .dashboard-container {
        width: 100%; margin: 0 auto; display: flex; flex-direction: column; position: relative;
        background-color: var(--bg-pink);
        background-image: linear-gradient(45deg, rgba(255,255,255,0.4) 25%, transparent 25%),
                          linear-gradient(-45deg, rgba(255,255,255,0.4) 25%, transparent 25%);
        background-size: 10px 10px;
    }

    .post-header { display: none !important; }
    .post-content { padding-top: 15px !important; }

    /* --- 2. 核心布局 --- */
    .terminal-body { flex: 1; display: flex; padding: 10px; gap: 10px; position: relative; }
    .left-pillar { width: 65px; display: flex; flex-direction: column; gap: 10px; flex-shrink: 0; }

    .pillar-btn {
        background: var(--terminal-black); color: var(--matrix-green); flex: 1;
        border: 2px solid var(--hot-pink); display: flex; align-items: center; justify-content: center;
        writing-mode: vertical-lr; text-orientation: mixed; font-size: 11px; font-weight: 900;
        cursor: pointer; box-shadow: 4px 4px 0px rgba(255, 77, 148, 0.2);
        overflow: hidden;
    }

    /* --- 3. 黑客帝国闪烁核心 (Matrix Blinking) --- */
    @keyframes matrix-blink {
        0%, 100% { opacity: 0.2; color: #005511; text-shadow: none; }
        50% { opacity: 1; color: var(--matrix-green); text-shadow: 0 0 8px var(--matrix-green), 0 0 12px var(--matrix-green); }
    }

    /* --- 4. 信息流与卡片 --- */
    .right-feed { flex: 1; display: flex; flex-direction: column; gap: 15px; padding-bottom: 100px; }
    .news-card { background: rgba(255, 255, 255, 0.95); border: 2px dashed var(--hot-pink); padding: 15px; cursor: pointer; }
    .news-card h4 { margin: 0 0 10px 0; font-size: 12px; font-weight: 900; color: var(--hot-pink); display: flex; justify-content: space-between; align-items: center; }
    .news-card ul { padding: 0; list-style: none; margin: 0; font-size: 13px; color: #b53568; }
    .news-card li { margin-bottom: 8px; border-bottom: 1px dotted var(--bg-pink); padding-bottom: 4px; line-height: 1.4; }

    .classic-refresh { font-style: normal; cursor: pointer; display: inline-block; padding: 0 5px; color: var(--hot-pink); transition: transform 0.3s; }
    .classic-refresh:hover { color: var(--matrix-green); transform: rotate(180deg); }

    /* 传送链接样式 */
    .signal-link { text-decoration: none; color: inherit; display: block; }
    .signal-link:hover { color: var(--hot-pink); }
    .link-icon { font-size: 10px; margin-left: 5px; color: var(--hot-pink); font-weight: 900; }

    /* 阅读沙盒 */
    #browser-overlay {
        position: absolute; top: 10px; left: 85px; right: 10px; bottom: 10px;
        width: calc(100% - 95px); max-width: 850px;
        background: #fff; border: 3px solid var(--terminal-black);
        display: none; flex-direction: column; z-index: 2000;
        box-shadow: 0 20px 60px rgba(0,0,0,0.4);
    }

    .browser-header { background: #f1f1f1; padding: 10px; border-bottom: 1px solid #ddd; display: flex; justify-content: space-between; }
    .close-btn { background: var(--hot-pink); color: #fff; border: none; padding: 4px 12px; font-weight: 800; cursor: pointer; }
    #reader-content { flex: 1; padding: 25px; overflow-y: auto; color: #333; line-height: 1.6; }

    @media screen and (max-width: 768px) {
        .left-pillar { width: 45px !important; }
        #browser-overlay { left: 55px !important; width: calc(100% - 65px) !important; }
    }
</style>

<div class="dashboard-container">
    <!-- 🟢 统一天气组件 -->
    {% include terminal-weather.html %}

    <div class="terminal-body">
        <div class="left-pillar">
            <div class="pillar-btn" id="vademecum-btn" onclick="openManual()">幸存者手册(VADEMECUM)</div>
            <div class="pillar-btn" style="flex:0.25; background: #fff; color: #000; writing-mode: vertical-lr; text-orientation: mixed; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 900;">MAP</div>
        </div>

        <div class="right-feed">
            <div class="news-card" onclick="expandSignal('🚆 交通信号解码', 'vbb-list')">
                <h4><span>🚆 交通 & 罢工</span> <span class="classic-refresh" onclick="refreshCategory(event, 'vbb')">🔄</span></h4>
                <ul id="vbb-list"></ul>
            </div>

            <div class="news-card" onclick="expandSignal('🛡️ 安全预警广播', 'police-list')">
                <h4><span>🛡️ 安全快讯</span> <span class="classic-refresh" onclick="refreshCategory(event, 'police')">🔄</span></h4>
                <ul id="police-list"></ul>
            </div>

            <div class="news-card" onclick="expandSignal('🎡 免费活动清单', 'free-list')">
                <h4><span>🎡 免费活动</span> <span class="classic-refresh" onclick="refreshCategory(event, 'free')">🔄</span></h4>
                <ul id="free-list"></ul>
            </div>

            <div class="news-card" onclick="expandSignal('💃 柏林脉搏频率', 'club-list')">
                <h4><span>💃 柏林脉搏</span> <span class="classic-refresh" onclick="refreshCategory(event, 'club')">🔄</span></h4>
                <ul id="club-list"></ul>
            </div>
        </div>

        <div id="browser-overlay">
            <div class="browser-header">
                <span id="browser-title" style="font-size: 10px; font-family: monospace; font-weight: 900;">SIGNAL_READER</span>
                <button class="close-btn" onclick="closeSource()">关闭 [X]</button>
            </div>
            <div id="reader-content"></div>
        </div>
    </div>
</div>

<!-- 幸存者手册内容 (无删减) -->
<div id="manual-content" style="display:none;">
    <h2 style="color:var(--hot-pink); margin-bottom:15px; font-size:18px;">📕 柏林幸存者手册 (Survival Vademecum)</h2>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px;">
        <div>
            <strong style="color:var(--hot-pink); display:block; margin-bottom:8px;">🥗 生活补给：菜市场</strong>
            <ul style="padding-left: 0; list-style: none; font-size: 12px;">
                <li>📍 Genter Markt (Wedding)</li>
                <li>📍 Maybachufer (Neukölln)</li>
                <li>📍 Crelle Markt (Schöneberg)</li>
            </ul>
        </div>
        <div>
            <strong style="color:var(--hot-pink); display:block; margin-bottom:8px;">📦 旧物盒子 (Zu Verschenken)</strong>
            <p style="font-size: 11px; color:#4a5568;">
                - <strong>警报：</strong> 严禁搬分布艺家具！柏林床虫 (Bettwanzen) 泛滥。<br>
                - <strong>规则：</strong> 请勿从慈善处拿走留给流浪汉的食物。
            </p>
        </div>
        <div>
            <strong style="color:var(--hot-pink); display:block; margin-bottom:8px;">💼 2026 招聘会</strong>
            <p style="font-size: 11px;">🏢 Connecticum (学生/职场新人)<br>🚀 Karrieretag Berlin (全职必备)</p>
        </div>
    </div>
</div>

<script>
// --- 信号池升级版 (带链接) ---
const signalPools = {
    vbb: [
        {t: "Güterzug in Senftenberg entgleist - Regionalverkehr läuft wieder", u: "https://www.rbb24.de/wirtschaft/beitrag/2026/05/brandenburg-senftenberg-zug-entgleist-regionalbahn.html"},
        {t: "S-Bahn Berlin: Signalstörung auf der Stadtbahn führt zu Verspätungen", u: "https://sbahn.berlin/fahren/fahrplanaenderungen/"},
        {t: "BVG: Streikankündigung der Gewerkschaft GDL für Donnerstag", u: "https://www.bvg.de/de/presse"},
        {t: "U-Bahn U7: Bauarbeiten zwischen Hermannplatz und Britz-Süd", u: "https://www.bvg.de/de/verbindungen/bauinfos"},
        {t: "Ersatzverkehr: Busse statt Bahnen auf der S2 Richtung Bernau", u: "https://sbahn.berlin/fahren/fahrplanaenderungen/"}
    ],
    police: [
        {t: "Polizei Berlin: Schüsse auf ein Café in Neukölln gemeldet", u: "https://www.berlin.de/polizei/polizeimeldungen/"},
        {t: "Feuerwehr: Großbrand in einer Lagerhalle in Spandau gelöscht", u: "https://www.berliner-feuerwehr.de/einsaetze/"},
        {t: "Verkehrsunfall: A100 nach Kollision mehrerer Fahrzeuge gesperrt", u: "https://www.viz-berlin.de/"},
        {t: "Fahrraddiebstahl-Ring in Wedding ausgehoben", u: "https://www.berlin.de/polizei/polizeimeldungen/"}
    ],
    free: [
        {t: "[06.21] Fête de la Musique: Ganz Berlin wird zur Bühne", u: "https://www.fetedelamusique.de/"},
        {t: "[07.25] CSD Berlin: Pride Parade durch das Regierungsviertel", u: "https://csd-berlin.de/"},
        {t: "Museumssonntag: Kostenloser Eintritt in über 60 Museen", u: "https://www.museumssonntag.berlin/"}
    ],
    club: [
        {t: "Siegessäule: Queer Kulturkalender für den Frühling", u: "https://www.siegessaeule.de/termine/"},
        {t: "Tresor Berlin: 35 Jahre Techno-Geschichte im Kraftwerk", u: "https://tresorberlin.com/"},
        {t: "Berghain: Line-up für die Klubnacht am Wochenende steht", u: "https://www.berghain.berlin/en/program/"}
    ]
};

// --- 功能引擎 ---
function refreshCategory(event, category) {
    if (event) event.stopPropagation();
    const pool = signalPools[category];
    const list = document.getElementById(`${category}-list`);
    const shuffled = [...pool].sort(() => 0.5 - Math.random());
    const selected = shuffled.slice(0, 3);
    list.innerHTML = selected.map(item => `<li data-url="${item.u}">${item.t}</li>`).join('');
}

async function expandSignal(title, listId) {
    const overlay = document.getElementById('browser-overlay');
    const reader = document.getElementById('reader-content');
    const items = document.querySelectorAll(`#${listId} li`);
    let html = `<h2 style="color:var(--hot-pink); font-size:18px; margin-bottom:20px;">${title}</h2><ul style="list-style:none; padding:0;">`;

    items.forEach((item, index) => {
        const txt = item.innerText.trim();
        const url = item.getAttribute('data-url');
        html += `
            <li style="margin-bottom:25px; border-bottom:1px dotted #eee; padding-bottom:15px;">
                <a href="${url}" target="_blank" class="signal-link">
                    <div style="font-weight:800; font-size:13px; line-height:1.4;">${txt} <span class="link-icon">↗传送</span></div>
                </a>
                <div id="trans-${listId}-${index}" style="color:var(--hot-pink); font-size:11px; margin-top:8px; font-weight:600;">信号解调中...</div>
            </li>`;
    });

    reader.innerHTML = html + `</ul>`;
    document.getElementById('browser-title').innerText = "信号调频: " + title;
    overlay.style.display = 'flex';

    items.forEach(async (item, index) => {
        const txt = item.innerText.trim();
        const target = document.getElementById(`trans-${listId}-${index}`);
        try {
            const res = await fetch(`https://translate.googleapis.com/translate_a/single?client=gtx&sl=de&tl=zh-CN&dt=t&q=${encodeURIComponent(txt)}`);
            const result = await res.json();
            target.innerHTML = `🏮 解码：${result[0].map(x => x[0]).join("")}`;
        } catch (e) { target.innerHTML = "❌ 信号受损"; }
    });
}

function openManual() {
    document.getElementById('reader-content').innerHTML = document.getElementById('manual-content').innerHTML;
    document.getElementById('browser-title').innerText = "协议读取: VADEMECUM";
    document.getElementById('browser-overlay').style.display = 'flex';
}
function closeSource() { document.getElementById('browser-overlay').style.display = 'none'; }

// --- 初始化与黑客帝国闪烁逻辑 ---
document.addEventListener("DOMContentLoaded", () => {
    // 1. 填充初始数据
    ['vbb', 'police', 'free', 'club'].forEach(cat => refreshCategory(null, cat));

    // 2. 注入黑客帝国闪烁脚本
    const vBtn = document.getElementById('vademecum-btn');
    if (vBtn) {
        const text = "幸存者手册(VADEMECUM)";
        vBtn.innerHTML = text.split('').map(char => {
            const delay = (Math.random() * 2).toFixed(2);
            return `<span style="animation: matrix-blink 1.2s infinite alternate ${delay}s">${char}</span>`;
        }).join('');
    }

    // 3. 自动展开手册
    setTimeout(() => { if(document.getElementById('browser-overlay').style.display !== 'flex') openManual(); }, 2000);
});
</script>

{% include news-script.html %}