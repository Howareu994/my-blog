---
layout: page
title: "🛟 硬核防御图"
permalink: /survival/
---

<style>
    /* --- 1. 核心变量 (超重度毛玻璃) --- */
    :root {
        --glass-bg: rgba(255, 255, 255, 0.1);
        --glass-border: rgba(255, 255, 255, 0.15);
        --matrix-green: #00ff41;
        --matrix-glow: 0 0 10px #00ff41, 0 0 20px #00ff41;
        --hot-pink: #ff4d94;
        --terminal-black: #000;
    }

    .survival-vault {
        max-width: 850px; margin: 20px auto;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }

    .ultra-glass {
        background: var(--glass-bg) !important;
        backdrop-filter: blur(40px) saturate(180%) !important;
        -webkit-backdrop-filter: blur(40px) saturate(180%) !important;
        border: 1px solid var(--glass-border) !important;
        border-radius: 24px !important;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.05) !important;
        transition: 0.3s cubic-bezier(0.19, 1, 0.22, 1);
    }

    /* --- 3. 头部：黑客帝国 CRT 终端 --- */
    .matrix-terminal {
        background: rgba(0, 0, 0, 0.8) !important;
        border: 1px solid var(--matrix-green) !important;
        padding: 30px; margin-bottom: 30px;
        color: var(--matrix-green);
        text-shadow: var(--matrix-glow);
        position: relative; overflow: hidden;
    }

    .matrix-terminal::before {
        content: " "; display: block; position: absolute; top: 0; left: 0; bottom: 0; right: 0;
        background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.1) 50%);
        background-size: 100% 4px; z-index: 2; pointer-events: none;
    }

    .matrix-rain {
        position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        color: rgba(0, 255, 65, 0.05);
        font-family: monospace; font-size: 8px; line-height: 1;
        white-space: nowrap; user-select: none; pointer-events: none;
        animation: rain-fall 20s linear infinite;
        opacity: 0.6;
    }
    @keyframes rain-fall { from { transform: translateY(-50%); } to { transform: translateY(50%); } }

    .emergency-channel {
        margin-bottom: 30px; padding: 25px;
        display: flex; justify-content: space-between; align-items: center;
        border: 1px solid rgba(255, 77, 148, 0.5) !important;
    }
    .order-btn {
        background: var(--hot-pink); color: #fff; border: none;
        padding: 12px 24px; border-radius: 14px; font-weight: 900;
        cursor: pointer; transition: 0.3s;
        box-shadow: 0 5px 20px rgba(255, 77, 148, 0.3);
    }
    .order-btn:hover { transform: translateY(-3px) scale(1.05); box-shadow: 0 8px 30px rgba(255, 77, 148, 0.5); }

    /* --- 5. 文件切片网格 & 柔和呼吸灯 --- */
    .slice-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-bottom: 30px; }

    .data-slice {
        padding: 25px; display: flex; align-items: center; gap: 15px; cursor: pointer;
        /* 🔥 新增：柔和的透明模块呼吸效果 */
        animation: soft-cyber-pulse 3.5s infinite alternate ease-in-out;
    }

    /* 让第二个和第四个卡片呼吸错开，显得更自然 */
    .data-slice:nth-child(even) { animation-delay: 1.5s; }

    .data-slice:hover {
        background: rgba(255, 255, 255, 0.3) !important;
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1) !important;
        border-color: rgba(255, 255, 255, 0.5) !important;
        animation: none; /* 悬浮时停止呼吸，锁定状态 */
    }

    /* 🔥 柔和呼吸动画定义 */
    @keyframes soft-cyber-pulse {
        0% { box-shadow: 0 0 0px rgba(255, 77, 148, 0); border-color: var(--glass-border); }
        100% { box-shadow: 0 0 20px rgba(255, 77, 148, 0.2); border-color: rgba(255, 77, 148, 0.4); }
    }

    .slice-id { font-size: 10px; background: var(--matrix-green); color: #000; padding: 4px 8px; border-radius: 8px; font-weight: 900; }
    .slice-title { font-weight: 800; color: #333; font-size: 16px; }

    /* --- 6. 信号阅读器 --- */
    #signal-overlay {
        position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(255, 218, 233, 0.2);
        backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px);
        display: none; justify-content: center; align-items: center; z-index: 9999;
    }
    .reader-window {
        background: rgba(255, 255, 255, 0.8) !important;
        backdrop-filter: blur(40px) saturate(180%) !important;
        -webkit-backdrop-filter: blur(40px) saturate(180%) !important;
        width: 90%; max-width: 650px; height: 80vh;
        border-radius: 32px; border: 1px solid rgba(255,255,255,0.4);
        display: flex; flex-direction: column;
        box-shadow: 0 30px 60px rgba(0,0,0,0.1) !important;
        animation: ios-zoom 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
    }
    @keyframes ios-zoom { from { transform: scale(0.9); opacity: 0; } to { transform: scale(1); opacity: 1; } }

    .reader-header { padding: 25px 30px; border-bottom: 1px solid rgba(0,0,0,0.05); display: flex; justify-content: space-between; }
    #reader-body { flex: 1; padding: 40px; overflow-y: auto; color: #222; }

    .tip-box { background: rgba(255, 77, 148, 0.08); padding: 20px; border-radius: 16px; border-left: 6px solid var(--hot-pink); margin: 25px 0; }
</style>

<div class="survival-vault">

    <div class="matrix-terminal ultra-glass" style="border-radius: 24px !important;">
        <div class="matrix-rain">
            <script>
                let rainText = "";
                for(let i=0; i<40; i++) {
                    let line = "";
                    for(let j=0; j<60; j++) { line += String.fromCharCode(0x30A0 + Math.random() * 96); }
                    rainText += line + "<br>";
                }
                document.write(rainText);
            </script>
        </div>
        <div style="position: relative; z-index: 5;">
            <div id="decipher-title" style="font-weight: 900; letter-spacing: 3px; font-size: 18px; min-height: 25px;"></div>
            <div id="decipher-desc" style="font-size: 13px; opacity: 0.9; margin-top: 10px; font-family: monospace; min-height: 18px;"></div>
        </div>
    </div>

    <div class="ultra-glass emergency-channel">
        <div>
            <div style="font-weight: 900; font-size: 17px; color: var(--terminal-black);">📨 黄信封 / 官方法律文书破译</div>
            <div style="font-size: 13px; color: #555; margin-top: 5px;">看不懂罚单 Frist？拍照发送，获取人工硬核建议。</div>
        </div>
        <div style="text-align: right;">
            <div style="font-weight: 900; color: var(--hot-pink); margin-bottom: 8px; font-size: 18px;">€ 9.90</div>
            <button class="order-btn" onclick="location.href='mailto:survivor994@gmail.com'">呼叫支援</button>
        </div>
    </div>

    <div class="slice-grid">
        <div class="ultra-glass data-slice" onclick="openSignal('anmeldung')">
            <span class="slice-id">DATA_01</span>
            <span class="slice-title">Anmeldung 灰色指南</span>
        </div>
        <div class="ultra-glass data-slice" onclick="openSignal('flat')">
            <span class="slice-id">DATA_02</span>
            <span class="slice-title">找房自荐信模板</span>
        </div>
        <div class="ultra-glass data-slice" onclick="openSignal('insurance')">
            <span class="slice-id">DATA_03</span>
            <span class="slice-title">开荒清单/保险</span>
        </div>
        <div class="ultra-glass data-slice" onclick="openSignal('rules')">
            <span class="slice-id">DATA_04</span>
            <span class="slice-title">生存潜规则 [RED]</span>
        </div>
    </div>

    <div class="ultra-glass" style="padding: 25px; display: flex; justify-content: space-between; align-items: center;">
        <div style="font-weight: 900; font-size: 14px; display: flex; align-items: center; gap: 10px;">🔋 <span style="color: #333;">能源回传中心</span></div>
        <div style="text-align: right;">
            <div style="font-size: 12px; font-family: monospace; color: var(--hot-pink); font-weight: 800;">PayPal: survivor994@gmail.com</div>
        </div>
    </div>
</div>

<div id="signal-overlay" onclick="closeSignal(event)">
    <div class="reader-window" onclick="event.stopPropagation()">
        <div class="reader-header">
            <span style="font-family:monospace; font-weight:900; font-size:11px; color:#aaa; letter-spacing:1px;">SIGNAL_DECODING...</span>
            <button class="close-btn" style="background:none; border:none; color:var(--hot-pink); font-weight:900; cursor:pointer;" onclick="closeSignal(null)">关闭 [X]</button>
        </div>
        <div id="reader-body"></div>
    </div>
</div>

<script>
    // ==========================================
    // 📂 核心数据库
    // ==========================================
    const vaultData = {
        'anmeldung': {
            title: 'Anmeldung 灰色地带生存指南',
            icon: '🛂',
            html: `
                <h2>如何搞定“不可能”的户口登记</h2>
                <p>在柏林，没有 Anmeldung 就意味着你在这个系统中不存在。</p>
                <div class="tip-box">
                    <strong>战术建议：</strong> 只要你居住超过三个月，房东在法律上有义务为你提供证明。
                </div>
            `
        },
        'flat': {
            title: '去“弱者化”找房申请模板',
            icon: '🏠',
            html: `
                <h2>猎人不需要怜悯</h2>
                <p>房东寻找的是“秩序”。第一封信要像商业提案。</p>
                <div style="background:rgba(0,0,0,0.03); border-radius:15px; padding:20px; font-family:monospace; font-size:14px; margin:15px 0;">
                    Sehr geehrte Damen und Herren,<br> ich bin ein ordentlicher Mieter...
                </div>
            `
        },
        'insurance': {
            title: '必办保险与开荒清单',
            icon: '🛡️',
            html: `<h2>防御底线</h2><p>1. 第三方责任险 (Haftpflicht)<br>2. TK 医保</p>`
        },
        'rules': {
            title: '柏林生存潜规则',
            icon: '🚫',
            html: `<h2>红线禁区</h2><p>1. 瓶子放桶边。<br>2. 晚上10点后消音。</p>`
        }
    };

    function openSignal(key) {
        const data = vaultData[key];
        const overlay = document.getElementById('signal-overlay');
        const body = document.getElementById('reader-body');
        if (data && overlay && body) {
            body.innerHTML = `<h2 style="color:var(--hot-pink); display:flex; align-items:center; gap:12px;"><span>${data.icon}</span> ${data.title}</h2>` + data.html;
            overlay.style.display = 'flex';
        }
    }

    function closeSignal(e) {
        if (e && e.target !== document.getElementById('signal-overlay')) return;
        document.getElementById('signal-overlay').style.display = 'none';
    }

    // ==========================================
    // 👽 黑客帝国文字解调特效 (Matrix Decipher)
    // ==========================================
    class MatrixDecipher {
        constructor(element, text) {
            this.element = element;
            this.text = text;
            this.chars = '!<>-_\\\\/[]{}—=+*^?#_010101';
            this.frame = 0;
            this.queue = [];
            for (let i = 0; i < text.length; i++) {
                const start = Math.floor(Math.random() * 40);
                const end = start + Math.floor(Math.random() * 40);
                this.queue.push({ from: this.chars[Math.floor(Math.random() * this.chars.length)], to: text[i], start, end, char: '' });
            }
            this.update = this.update.bind(this);
            this.update();
        }
        update() {
            let output = '';
            let complete = 0;
            for (let i = 0, n = this.queue.length; i < n; i++) {
                let { from, to, start, end, char } = this.queue[i];
                if (this.frame >= end) {
                    complete++;
                    output += to;
                } else if (this.frame >= start) {
                    if (!char || Math.random() < 0.28) {
                        char = this.chars[Math.floor(Math.random() * this.chars.length)];
                        this.queue[i].char = char;
                    }
                    output += `<span style="color: rgba(255,255,255,0.7); text-shadow: none;">${char}</span>`;
                } else {
                    output += from;
                }
            }
            this.element.innerHTML = output;
            if (complete === this.queue.length) {
                this.element.innerHTML += '<span style="animation: blink 1s infinite;">_</span>';
            } else {
                requestAnimationFrame(this.update);
                this.frame++;
            }
        }
    }

    // 页面加载完成后，触发黑客特效
    document.addEventListener('DOMContentLoaded', () => {
        // 第一行：解调标题
        new MatrixDecipher(document.getElementById('decipher-title'), '[ SURVIVAL_VAULT_v6.0 ]');

        // 稍微延迟一下，解调第二行
        setTimeout(() => {
            new MatrixDecipher(document.getElementById('decipher-desc'), '> 正在进行超重度透明解调...');
        }, 600);
    });
</script>

<style> @keyframes blink { 50% { opacity: 0; } } </style>