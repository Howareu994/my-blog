---
layout: page
title: "📚 漫游进程"
permalink: /wiki/
---

<style>
    /* --- 1. 核心变量与全局滤镜 --- */
    :root {
        --hot-pink: #ff4d94;
        --text-dark: #b53568;
        --cyber-blue: #00008B;
        --matrix-green: #00ff41;
        --bg-glass: rgba(0, 0, 0, 0.9);
        --scanline: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.1) 50%);
    }

    /* 强制全站直角 */
    * { border-radius: 0 !important; }

    .post-header { display: none !important; }
    .post-content { padding-top: 15px !important; }

    /* --- 2. 生存窗口：增加 CRT 扫描线质感 --- */
    .survival-window {
        background: #fff;
        border: 2px solid #fff;
        box-shadow: 0 12px 40px rgba(255, 77, 148, 0.15);
        overflow: hidden;
        margin-bottom: 80px;
        position: relative;
    }

    /* 模拟屏幕微弱频闪与扫描线 */
    .survival-window::after {
        content: " ";
        display: block;
        position: absolute;
        top: 0; left: 0; bottom: 0; right: 0;
        background: var(--scanline);
        background-size: 100% 4px;
        z-index: 2001;
        pointer-events: none;
        opacity: 0.2;
    }

    .window-body { padding: 15px; background: #fafafa; }

    /* --- 3. 压扁版解码器 (Visual Impact Upgrade) --- */
    .decoder-panel {
        border: 2px solid var(--hot-pink);
        padding: 12px;
        background: repeating-linear-gradient(0deg, transparent, transparent 1px, rgba(255, 77, 148, 0.03) 1px, rgba(255, 77, 148, 0.03) 2px);
        margin-bottom: 15px;
        position: relative;
    }

    .decoder-title { color:var(--hot-pink); font-size:9px; font-weight:900; margin-bottom:6px; letter-spacing: 1px; }

    .decoder-display {
        background: #fff;
        height: 42px;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 1px solid rgba(255, 77, 148, 0.2);
        margin-bottom: 8px;
        font-weight: 900;
        color: var(--hot-pink);
        font-size: 1rem;
        font-family: monospace;
        position: relative;
        overflow: hidden;
    }

    .btn-feed {
        width: 100%;
        background: #fff;
        border: 2px solid var(--hot-pink);
        color: var(--hot-pink);
        padding: 8px;
        font-weight: 900;
        font-size: 11px;
        cursor: pointer;
        font-family: monospace;
    }

    .btn-feed:hover { background: var(--hot-pink); color: #fff; }

    .is-decoding { animation: cyber-shake 0.1s infinite; background: var(--hot-pink) !important; color: #fff !important; }
    @keyframes cyber-shake { 0% { transform: translate(1px, 0); } 50% { transform: translate(-1px, 1px); } 100% { transform: translate(0, -1px); } }

    /* --- 4. 地图容器与 HUD --- */
    .map-container {
        height: 60vh;
        border: 2px solid var(--hot-pink);
        position: relative;
        overflow: hidden;
        display: flex;
        flex-direction: column;
    }

    .map-frame { flex: 1; width: 100%; border: none; filter: contrast(1.1) brightness(0.95); }

    .map-hud {
        position: absolute;
        top: 15px;
        right: 15px;
        z-index: 1000;
        background: var(--bg-glass);
        border: 1px solid var(--matrix-green);
        padding: 8px 12px;
        width: 200px;
        color: var(--matrix-green);
        font-family: monospace;
        pointer-events: none;
    }

    .hud-label { font-size: 8px; opacity: 0.8; margin-bottom: 4px; display: block; }
    .hud-stats { font-size: 13px; font-weight: 900; margin-bottom: 8px; display: block; }
    .progress-track { height: 3px; background: rgba(0, 255, 65, 0.1); width: 100%; position: relative; }
    .progress-fill { height: 100%; background: var(--matrix-green); width: 0%; box-shadow: 0 0 8px var(--matrix-green); transition: width 1s ease; }

    /* --- 5. 手机端专项震撼优化 (打破边界，但不贴死) --- */
    @media screen and (max-width: 768px) {
        /* 击碎 Jekyll 默认的大白边，但保留极少量的内边距让内容有呼吸感 */
        .wrapper, .page-content { 
            padding-left: 0 !important; 
            padding-right: 0 !important; 
            max-width: 100% !important; 
        }

        /* 整个生存窗口取消两边的空白，直接铺满 */
        .survival-window {
            border-left: none;
            border-right: none;
            box-shadow: none; /* 手机上不需要两边的阴影 */
        }

        /* 内部内容区微调：不要贴死屏幕边缘 */
        .window-body { 
            padding: 10px; /* 控制边距：让内部的框和手机边缘保持 10px 距离，不太宽也不太窄 */
        }

        .map-hud {
            position: static;
            width: 100%;
            padding: 8px 12px;
            background: #000;
            border: none;
            border-top: 2px solid var(--matrix-green);
            order: 2;
        }

        .hud-header-row { display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px; }
        .hud-label { font-size: 7px; }
        .hud-stats { font-size: 11px; }
    }
</style>

<div class="survival-window">
    <!-- 🟢 引入全站统一的天气组件 -->
    {% include terminal-weather.html %}

    <div class="window-body">
        <!-- 压扁版解码器模块 -->
        <div class="decoder-panel">
            <div class="decoder-title">SIGNAL_DECODER // 信号解码</div>
            <div id="res-display" class="decoder-display">READY</div>
            <button class="btn-feed" id="feed-btn" onclick="roll(event)">FEED ME / 投喂我</button>
        </div>

        <!-- 地图容器 -->
        <div class="map-container">
            <iframe id="map-frame" class="map-frame" src="{{ '/map.html' | relative_url }}"></iframe>

            <!-- 手机端自动变底部的 HUD -->
            <div class="map-hud">
                <div class="hud-header-row">
                    <span class="hud-label">Exploration Progress / 探索进度</span>
                    <span class="hud-stats" id="hud-text">SYNCING...</span>
                </div>
                <div class="progress-track">
                    <div class="progress-fill" id="hud-bar"></div>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
    let pool = [];
    const hudText = document.getElementById('hud-text');
    const hudBar = document.getElementById('hud-bar');
    const resDisplay = document.getElementById('res-display');
    const mapFrame = document.getElementById('map-frame');

    // 1. 进度数据同步
    fetch('{{ "/data.json" | relative_url }}')
        .then(r => r.json())
        .then(data => {
            pool = data.filter(i => i.name && (i.lat || i.latitude));
            const vCount = data.filter(i => {
                const status = (i.Visited || i.visited || "").toString().toLowerCase().trim();
                return status === 'yes' || status === 'true';
            }).length;
            const percent = Math.round((vCount / pool.length) * 100);
            hudText.innerText = `${vCount} / ${pool.length} NODES`;
            hudBar.style.width = `${percent}%`;
        })
        .catch(err => { hudText.innerText = `ERROR`; });

    // 2. 抽选/投喂逻辑
    function roll(event) {
        if (!pool.length) return;
        const btn = event.target;
        btn.disabled = true;
        resDisplay.classList.add('is-decoding');

        let count = 0;
        const timer = setInterval(() => {
            resDisplay.innerText = pool[Math.floor(Math.random() * pool.length)].name;
            if (++count > 20) {
                clearInterval(timer);
                const winner = pool[Math.floor(Math.random() * pool.length)];
                resDisplay.classList.remove('is-decoding');
                resDisplay.innerText = winner.name;

                // 地图联动信号发送
                if (mapFrame.contentWindow) {
                    mapFrame.contentWindow.postMessage({ type: 'FLY_TO', name: winner.name }, '*');
                }
                setTimeout(() => { btn.disabled = false; }, 1000);
            }
        }, 50);
    }
</script>