---
layout: null
---
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <meta name="theme-color" content="#ffdae9">

    <title>{{ site.title | default: "柏林反潮流日志 | 情绪避难所" }}</title>
    <link href="https://cdn.jsdelivr.net/npm/remixicon@3.5.0/fonts/remixicon.css" rel="stylesheet">
    <style>
        :root {
            --primary-pink: #ff85b9;
            --hot-pink: #ff4d94;
            --matrix-green: #00ff41;
            --cyber-blue: #00008B;
            --bg-pink: #ffdae9;
            --text-main: rgb(181, 53, 104);
            --border-light: #ff85b9;
            --terminal-black: #111;
            --card-shadow: 4px 4px 0px rgba(255, 77, 148, 0.15);
        }

        * {
            box-sizing: border-box !important;
            outline: none; margin: 0; padding: 0;
            -webkit-tap-highlight-color: transparent !important;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background-color: var(--bg-pink);
            background-image:
                linear-gradient(45deg, rgba(255, 255, 255, 0.4) 25%, transparent 25%),
                linear-gradient(-45deg, rgba(255, 255, 255, 0.4) 25%, transparent 25%),
                linear-gradient(45deg, transparent 75%, rgba(255, 255, 255, 0.4) 75%),
                linear-gradient(-45deg, transparent 75%, rgba(255, 255, 255, 0.4) 75%);
            background-size: 10px 10px; background-attachment: fixed; min-height: 100vh;
            color: var(--text-main);
        }

        /* 1. 顶部导航与星光爆破 */
        .site-header { background: rgba(255, 255, 255, 0.98); border-bottom: 3px solid var(--hot-pink); position: sticky; top: 0; z-index: 1000; width: 100%; }
        .header-inner { max-width: 1050px; margin: 0 auto; padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; }
        .site-title { font-size: 1.4rem; font-weight: 900; color: var(--hot-pink); text-decoration: none; letter-spacing: -0.5px; }
        .desktop-nav { display: flex; gap: 20px; align-items: center; }
        .page-link { text-decoration: none; font-size: 0.95rem; font-weight: 700; color: var(--text-main); padding: 6px 12px; border-radius: 8px; transition: all 0.2s; border: 2px solid transparent; position: relative; }

        /* 导航栏闪烁星光 */
        .page-link:hover { background: var(--bg-pink); color: var(--hot-pink); border: 2px dashed var(--hot-pink); transform: scale(1.05); }
        .page-link:hover::before, .page-link:hover::after {
            content: "✨"; position: absolute; font-size: 12px; top: 50%; left: 50%;
            opacity: 0; pointer-events: none; animation: sparkle-burst 0.5s ease-out forwards;
        }
        .page-link:hover::after { content: "✦"; animation-delay: 0.1s; }

        .lang-btn { background: var(--terminal-black); color: #fff !important; border: 2px solid var(--hot-pink); box-shadow: 2px 2px 0px rgba(255, 77, 148, 0.4); }
        .lang-btn:hover { background: #fff; color: var(--terminal-black) !important; transform: translateY(-2px); box-shadow: 4px 4px 0px rgba(255, 77, 148, 0.4); }

        /* 2. 页面网格：核心修改区！反转了左右的宽窄比例 */
        .app-container { max-width: 1050px; margin: 30px auto; padding: 0 20px; display: grid; grid-template-columns: minmax(0, 1fr); gap: 30px; padding-bottom: 100px; }
        @media screen and (min-width: 800px) { 
            /* 原来是 340px minmax(0, 1fr)，现在改为自适应宽屏在左，340px窄屏在右 */
            .app-container { grid-template-columns: minmax(0, 1fr) 340px; align-items: start; } 
        }

        /* 3. 通用模块 */
        .module-card { background: rgba(255, 255, 255, 0.95); border: 2px solid var(--border-light); border-radius: 16px; padding: 20px; box-shadow: var(--card-shadow); margin-bottom: 25px; }
        .module-dark { background: var(--terminal-black); border-color: var(--terminal-black); padding: 0; overflow: hidden; }
        .section-title { padding-bottom: 15px; font-size: 1.1rem; font-weight: 800; display: flex; align-items: center; gap: 8px; color: var(--hot-pink); }

        /* 4. 情绪墙 */
        .input-group { display: flex; border: 2px solid var(--hot-pink); border-radius: 8px; overflow: hidden; width: 100%; margin-bottom: 15px;}
        #status-input { flex: 1; border: none; padding: 12px; font-family: "Courier New", monospace; color: var(--text-main); font-weight: 600; }
        .save-btn { background: var(--hot-pink); color: white; border: none; padding: 0 20px; font-weight: 900; cursor: pointer; transition: all 0.2s;}
        .save-btn:active { background: var(--cyber-blue); }
        .locked-status { background: #fff; border-bottom: 1px dashed var(--border-light); padding: 12px 5px; display: flex; justify-content: space-between; align-items: flex-start; font-size: 13px; font-weight: 600; line-height: 1.4; }
        .locked-status:last-child { border-bottom: none; }
        .time-tag { color: var(--hot-pink); white-space: nowrap; margin-left: 10px; font-size: 11px;}

        /* 5. 赛博矩阵组件 */
        .grid-tools { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 25px; }
        .btn-screen { background: #000; border-radius: 12px; height: 90px; position: relative; overflow: hidden; display: flex; flex-direction: column; justify-content: center; align-items: center; border: 2px solid #000; box-shadow: var(--card-shadow);}
        .screen-label { z-index: 10; font-weight: 900; letter-spacing: 1px; font-size: 12px; }
        .matrix-bg { position: absolute; top: 0; left: 0; width: 100%; height: 100%; padding: 8px; z-index: 1; }
        .matrix-cell { font-size: 8px; color: rgba(0, 255, 65, 0.15); font-family: monospace; animation: matrix-flicker 1.5s infinite ease-in-out; display: inline-block; }
        .is-today { color: var(--matrix-green) !important; font-weight: 900 !important; text-shadow: 0 0 10px var(--matrix-green); opacity: 1 !important; }

        /* 6. 核心业务：补给站 (修复边缘遮挡问题) */
        .horizontal-scroll {
            display: flex;
            overflow-x: auto;
            gap: 15px;
            scrollbar-width: none;
            width: 100%;
            padding: 12px 4px 12px 4px;
            margin-top: -12px;
            margin-bottom: 8px;
        }
        .horizontal-scroll::-webkit-scrollbar { display: none; }
        .feature-card { min-width: 140px; height: 140px; background: #fff; border: 2px solid var(--border-light); border-radius: 16px; padding: 15px; display: flex; flex-direction: column; justify-content: space-between; text-decoration: none; color: var(--text-main); box-shadow: var(--card-shadow); transition: all 0.2s; position: relative;}

        /* 补给站 Y2K 悬停霓虹故障特效 */
        .feature-card:hover {
            transform: translateY(-5px);
            border-color: var(--matrix-green);
            box-shadow: 4px 4px 0px var(--matrix-green);
            animation: card-glitch 0.3s infinite;
            z-index: 10;
        }

        /* 7. 信息流列表 */
        .article-item { display: flex; gap: 15px; background: #fff; border-radius: 12px; padding: 15px; margin-bottom: 15px; text-decoration: none; color: var(--text-main); border: 2px solid var(--border-light); box-shadow: 2px 2px 0px rgba(255, 133, 185, 0.2); transition: all 0.2s; }
        .article-item:hover {
            transform: translateX(5px);
            border-color: var(--hot-pink);
            box-shadow: 4px 4px 0px var(--hot-pink);
            animation: card-glitch 0.4s infinite alternate;
        }
        .article-icon { width: 45px; height: 45px; background: var(--bg-pink); border-radius: 10px; display: flex; align-items: center; justify-content: center; color: var(--hot-pink); font-size: 1.2rem; flex-shrink: 0;}
        .article-title { font-weight: 800; font-size: 15px; line-height: 1.4; }
        .article-meta { font-size: 12px; color: var(--hot-pink); margin-top: 5px; font-weight: 600; }
        .empty-state { text-align: center; padding: 30px; font-weight: 600; color: var(--border-light); border: 2px dashed var(--border-light); border-radius: 12px; }

        /* 8. 移动端底导 */
        .bottom-nav { display: none; }
        @media screen and (max-width: 768px) {
            .desktop-nav { display: none; }
            .app-container { margin: 15px auto; gap: 15px; padding: 0 15px; }
            .bottom-nav { display: flex; position: fixed; bottom: 0; left: 0; width: 100%; height: 75px; background: rgba(255, 255, 255, 0.98); border-top: 2px solid var(--border-light); justify-content: space-around; align-items: center; z-index: 1000; padding-bottom: env(safe-area-inset-bottom); }
            .nav-item { display: flex; flex-direction: column; align-items: center; color: var(--text-main); text-decoration: none; font-size: 11px; font-weight: 700; gap: 4px; }
            .nav-icon { font-size: 22px; transition: transform 0.2s;}
            .nav-item:active .nav-icon { transform: scale(1.3); color: var(--hot-pink);}
        }

        /* 动画定义区 */
        @keyframes matrix-flicker { 0%, 100% { opacity: 0.1; } 50% { opacity: 0.6; color: rgba(0, 255, 65, 0.4); text-shadow: 0 0 2px var(--matrix-green); } }
        @keyframes sparkle-burst { 0% { transform: translate(-50%, -50%) scale(0); opacity: 1; } 100% { transform: translate(-150%, -150%) scale(1.5) rotate(45deg); opacity: 0; } }
        @keyframes card-glitch {
            0% { border-color: var(--hot-pink); box-shadow: 4px 4px 0px var(--hot-pink); }
            50% { border-color: var(--matrix-green); box-shadow: -4px 4px 0px var(--matrix-green); }
            100% { border-color: var(--cyber-blue); box-shadow: 4px -4px 0px var(--cyber-blue); }
        }

        /* =======================================
           Y2K 老式 CRT 电视机关机转场特效
           ======================================= */
        .crt-turn-off {
            animation: crt-off 0.35s cubic-bezier(0.23, 1, 0.32, 1) forwards !important;
            pointer-events: none;
        }

        @keyframes crt-off {
            0% { transform: scale(1, 1); filter: contrast(1) brightness(1); opacity: 1; }
            40% { transform: scale(1, 0.005); filter: contrast(5) brightness(10); opacity: 1; background: #fff;}
            100% { transform: scale(0, 0.005); filter: contrast(5) brightness(10); opacity: 0; background: #fff;}
        }
    </style>
</head>
<body>

<header class="site-header">
    <div class="header-inner">
        <a href="{{ '/' | relative_url }}" class="site-title">柏林反潮流日志</a>
        <nav class="desktop-nav">
            <a class="page-link" href="{{ '/news/' | relative_url }}">📢 城市动态</a>
            <a class="page-link" href="{{ '/wiki/' | relative_url }}">📚 漫游进程</a>
            <a class="page-link" href="{{ '/map/' | relative_url }}">🗺️ 生活图鉴</a>
            <a class="page-link" href="{{ '/about/' | relative_url }}">☕ 关于</a>
            <a class="page-link lang-btn" href="{{ page.url | prepend: '/de' | replace: '//', '/' | relative_url }}">🇩🇪 DE</a>
        </nav>
    </div>
</header>

<div class="app-container">
    <!-- ================= 新左侧：核心业务与漫游碎片 (原右侧) ================= -->
    <div class="col-main">
        <div class="section-title">⛽ 核心补给站</div>
        <div class="horizontal-scroll">
            <a href="{{ '/termin/' | relative_url }}" class="feature-card">
                <span class="feature-icon">🫂</span>
                <span class="feature-text">陪伴 Termin<br>真实联结</span>
            </a>
            <a href="{{ '/consulting/' | relative_url }}" class="feature-card">
                <span class="feature-icon">🛋️</span>
                <span class="feature-text">心理辅导<br>能量急救窗</span>
            </a>
            <a href="{{ '/survival/' | relative_url }}" class="feature-card">
                <span class="feature-icon">🛟</span>
                <span class="feature-text">柏林生存<br>硬核防御图</span>
            </a>
        </div>

        <a href="{{ '/map/' | relative_url }}" class="section-title" style="margin-top: 10px; text-decoration: none; display: flex; justify-content: space-between; align-items: center; cursor: pointer; transition: opacity 0.2s;">
    <span>🧩 漫游碎片</span>
    <span style="font-size: 13px; font-weight: 600; color: #ff85b9;">更多 >> </span>
</a>
        <div class="article-list">
            {% for post in site.posts limit:8 %}
            <a href="{{ post.url | relative_url }}" class="article-item">
                <div class="article-icon"><i class="ri-file-text-line"></i></div>
                <div>
                    <div class="article-title">{{ post.title }}</div>
                    <div class="article-meta">
                        {{ post.date | date: "%Y.%m.%d" }}
                    </div>
                </div>
            </a>
            {% else %}
            <div class="empty-state">
                <i class="ri-radar-line" style="font-size: 24px; color: var(--hot-pink); display: block; margin-bottom: 10px;"></i>
                雷达正在扫描柏林最新动态...
            </div>
            {% endfor %}
        </div>
    </div>

    <!-- ================= 新右侧：控制面板与音乐 (原左侧) ================= -->
    <div class="col-sidebar">
        <div class="module-card">
            <div class="section-title">🌱 当前状态</div>
            <div class="input-group">
                <input type="text" id="status-input" placeholder="写下夏季要来的心情...">
                <button id="save-status-btn" class="save-btn">发送</button>
            </div>
            <ul id="status-history-list" style="list-style:none;"></ul>
        </div>

        <div class="grid-tools">
            <a href="https://strudel.cc/" target="_blank" class="btn-screen" id="screen-strudel" style="text-decoration: none;">
                <div class="screen-label" style="color:gold;">STRUDEL</div>
                <div class="matrix-bg"></div>
            </a>

            <a href="https://hydra.ojack.xyz/" target="_blank" class="btn-screen" id="screen-hydra" style="text-decoration: none;">
                <div class="screen-label" style="color:skyblue;">HYDRA</div>
                <div class="matrix-bg"></div>
            </a>
        </div>

        <!-- 顶级 DJ 歌单 -->
        <div class="module-card module-dark">
            <iframe width="100%" height="418" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=https%3A//soundcloud.com/ellen-allien&color=%23ff85b9&auto_play=false&hide_related=false&show_comments=false&show_user=true&show_reposts=false&show_teaser=true&visual=false"></iframe>
        </div>
    </div>
</div>

<!-- 移动端底导 -->
<nav class="bottom-nav">
    <a href="{{ '/' | relative_url }}" class="nav-item"><i class="ri-home-4-line nav-icon"></i><span>首页</span></a>
    <a href="{{ '/news/' | relative_url }}" class="nav-item"><i class="ri-megaphone-line nav-icon"></i><span>动态</span></a>
    <a href="{{ '/wiki/' | relative_url }}" class="nav-item"><i class="ri-book-read-line nav-icon"></i><span>生存</span></a>
    <a href="{{ '/about/' | relative_url }}" class="nav-item"><i class="ri-cup-line nav-icon"></i><span>求助</span></a>
</nav>

<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.3/dist/confetti.browser.min.js"></script>
<script>
    (function() {
        // 1. 赛博矩阵
        function fillMatrix(id) {
            const el = document.querySelector(`#${id} .matrix-bg`);
            if (!el) return;
            const now = new Date();
            const today = now.getDate();
            const daysInMonth = new Date(now.getFullYear(), now.getMonth() + 1, 0).getDate();
            let h = `<div style="display:grid; grid-template-columns:repeat(7,1fr); gap:2px;">`;
            for(let d = 1; d <= daysInMonth; d++) {
                const isToday = (d === today) ? 'is-today' : '';
                const delay = (Math.random() * 3).toFixed(2);
                h += `<span class="matrix-cell ${isToday}" style="animation-delay: -${delay}s">${d}</span>`;
            }
            el.innerHTML = h + `</div>`;
        }
        fillMatrix('screen-strudel');
        fillMatrix('screen-hydra');

        // 2. 情绪树洞
        const btn = document.getElementById('save-status-btn');
        const input = document.getElementById('status-input');
        const list = document.getElementById('status-history-list');

        function refreshTreehole() {
            const now = Date.now();
            let history = JSON.parse(localStorage.getItem('berlin_treehole') || "[]");
            history = history.filter(i => (now - i.time) < 86400000);

            list.innerHTML = history.map(i => {
                const rem = Math.round((86400000 - (now - i.time)) / 3600000);
                return `
                    <li class="locked-status">
                        <span>${i.text}</span>
                        <span class="time-tag">⌛ 剩余 ${rem}h</span>
                    </li>`;
            }).reverse().join('');
        }

        if (btn && input) {
            input.addEventListener('keypress', function (e) {
                if (e.key === 'Enter') btn.click();
            });

            btn.addEventListener('click', () => {
                const val = input.value.trim();
                if(!val) return;
                let history = JSON.parse(localStorage.getItem('berlin_treehole') || "[]");
                history.push({ text: val, time: Date.now() });
                localStorage.setItem('berlin_treehole', JSON.stringify(history));
                input.value = '';
                refreshTreehole();
                if(window.confetti) confetti({ particleCount: 60, spread: 60, origin: { y: 0.8 }, colors: ['#ff85b9','#ff4d94', '#00ff41'] });
            });
            refreshTreehole();
        }

        // ==========================================
        // Y2K CRT 老电视关机转场特效
        // ==========================================
        const transitionLinks = document.querySelectorAll('a.page-link, a.feature-card, a.article-item, a.nav-item');

        transitionLinks.forEach(link => {
            link.addEventListener('click', function(e) {
                if (this.target === '_blank' || this.href === window.location.href) return;

                e.preventDefault();
                const destination = this.href;

                document.body.classList.add('crt-turn-off');

                setTimeout(() => {
                    window.location.href = destination;
                }, 350);
            });
        });

        window.addEventListener('pageshow', (event) => {
            if (event.persisted) {
                document.body.classList.remove('crt-turn-off');
            }
        });

    })();
</script>
</body>
</html>