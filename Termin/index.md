---
layout: page
title: "🫂 陪伴 Termin"
permalink: /termin/
---

<style>
    :root {
        --terminal-black: #111;
        --hot-pink: #ff4d94;
        --cyber-blue: #00008B;
        --matrix-green: #00ff41;
        --bg-pink: #ffdae9;
    }

    .termin-container { max-width: 800px; margin: 0 auto; color: #b53568; }

    /* 1. 个人信息卡 */
    .profile-section {
        background: #fff; border: 3px solid var(--terminal-black); padding: 25px;
        box-shadow: 8px 8px 0px var(--hot-pink); margin-bottom: 30px;
    }
    .profile-header { display: flex; align-items: center; gap: 20px; margin-bottom: 20px; }
    .avatar-placeholder { width: 80px; height: 80px; background: var(--bg-pink); border: 2px solid var(--terminal-black); display: flex; align-items: center; justify-content: center; font-size: 40px; }

    /* 2. 安全协议（红线） */
    .safety-protocol {
        background: var(--terminal-black); color: #fff; padding: 20px;
        border-left: 10px solid var(--hot-pink); margin-bottom: 30px;
    }
    .protocol-title { color: var(--hot-pink); font-weight: 900; margin-bottom: 15px; display: flex; align-items: center; gap: 10px; }
    .protocol-list { list-style: none; padding: 0; font-size: 14px; }
    .protocol-list li { margin-bottom: 10px; display: flex; gap: 10px; }
    .no-go { color: #ff4d4d; font-weight: bold; }

    /* 3. 预约窗口结构 */
    .calendar-box { background: #fff; border: 2px dashed var(--hot-pink); padding: 20px; }

    /* 🔥 新增：2x2 矩阵网格 */
    .termin-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 15px;
        margin-top: 15px;
    }
    @media (max-width: 600px) {
        .termin-grid { grid-template-columns: 1fr; }
    }

    /* 月份卡片 (呼吸态) */
    .month-group {
        border: 2px solid var(--terminal-black);
        background: var(--bg-pink);
        transition: all 0.2s ease;
        animation: standby-pulse 2.5s infinite alternate;
        box-shadow: 4px 4px 0px rgba(0,0,0,0.1);
    }

    .month-group:hover {
        transform: translate(-2px, -2px);
        box-shadow: 6px 6px 0px var(--hot-pink);
        border-color: var(--hot-pink);
        animation: none; /* 悬停时停止闪烁 */
    }

    /* 🔥 展开时的状态：停止闪烁，变回硬核 */
    details[open].month-group {
        animation: none;
        border-color: var(--terminal-black);
        box-shadow: 6px 6px 0px var(--terminal-black);
    }

    /* 呼吸闪烁动画 */
    @keyframes standby-pulse {
        0% { opacity: 0.85; box-shadow: 0 0 0px rgba(255, 77, 148, 0); border-color: var(--terminal-black); }
        50% { opacity: 1; box-shadow: 0 0 15px rgba(255, 77, 148, 0.5); border-color: var(--hot-pink); }
        100% { opacity: 0.85; box-shadow: 0 0 0px rgba(255, 77, 148, 0); border-color: var(--terminal-black); }
    }

    /* 折叠标题栏 (Summary) */
    .month-title {
        padding: 12px 15px; font-weight: 900; color: var(--terminal-black);
        cursor: pointer; display: flex; align-items: center; justify-content: space-between;
        list-style: none;
        background: rgba(255, 255, 255, 0.5);
    }
    .month-title::-webkit-details-marker { display: none; }
    .month-title:hover { background: var(--matrix-green); }

    /* 展开状态的标题栏下边框 */
    details[open] .month-title { border-bottom: 2px solid var(--terminal-black); background: var(--hot-pink); color: white; }

    /* 网格容器 (放在展开的内容里) */
    .slot-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(145px, 1fr));
        gap: 10px; padding: 15px; background: #fff;
    }

    /* 单个时间块 */
    .time-slot {
        padding: 12px 5px; border: 2px solid var(--terminal-black); text-align: center;
        cursor: pointer; transition: all 0.2s; font-weight: bold; font-size: 13px;
        line-height: 1.4; color: var(--text-main);
    }
    .time-slot:hover { background: var(--matrix-green); transform: translateY(-3px); box-shadow: 4px 4px 0px var(--terminal-black); color: var(--terminal-black); }
    .time-slot.booked { background: #eee; color: #999; cursor: not-allowed; border-color: #ccc; }

    .time-slot span.date-part { font-size: 11px; opacity: 0.8; display: block; }
    .time-slot span.time-part { font-size: 15px; color: var(--hot-pink); }
    .time-slot:hover span.time-part { color: var(--terminal-black); }

    /* 表单隐藏 */
    #booking-form { display: none; margin-top: 30px; background: var(--bg-pink); padding: 20px; border: 2px solid var(--terminal-black); box-shadow: 6px 6px 0px var(--terminal-black); }
    .form-row { margin-bottom: 12px; }
    .form-row label { font-weight: 800; color: var(--terminal-black); }
    .termin-input {
        width: 100%; box-sizing: border-box; margin-top: 5px; padding: 9px;
        border: 2px solid var(--terminal-black); background: #fff; color: var(--terminal-black);
    }
    .termin-note { font-size: 12px; line-height: 1.5; color: var(--terminal-black); margin: 10px 0 0; }
    .time-slot.selected { background: var(--matrix-green); box-shadow: 4px 4px 0px var(--terminal-black); color: var(--terminal-black); }
    .time-slot.selected span.time-part { color: var(--terminal-black); }
    @keyframes blink { 50% { opacity: 0; } }
</style>

<div class="termin-container">
    <section class="profile-section">
        <div class="profile-header">
            <div class="avatar-placeholder">👨‍🚀</div>
            <div>
                <h2 style="margin:0;">Identity: Survivor 994</h2>
                <p style="margin:5px 0 0 0; opacity:0.8;">性别：男 | 坐标：Berlin | 语言：CN/DE/EN</p>
            </div>
        </div>
        <p>提供柏林行政（Termin）物理陪同、心理支持性散步或纯粹的公共空间存在。我不是法律专家，但我可以作为你的“影子”存在。</p>
    </section>

    <section class="safety-protocol">
        <div class="protocol-title">⚠️ 安全防御协议 (Safety Protocol)</div>
        <ul class="protocol-list">
            <li><span>✅</span> <span>仅限公共场合（外管局、咖啡馆、公园、街道）。</span></li>
            <li><span>✅</span> <span>开始前需在 Telegram 告知第三方紧急联系人位置。</span></li>
            <li><span class="no-go">❌</span> <span>禁止进入任何私人空间（公寓、酒店、封闭包厢）。</span></li>
            <li><span class="no-go">❌</span> <span>禁止任何形式的身体接触（NSFW 绝对禁止）。</span></li>
            <li><span class="no-go">❌</span> <span>禁止涉及非法交易、毒品、或代替签字等法律责任行为。</span></li>
        </ul>
    </section>

    <section class="calendar-box">
        <div class="protocol-title" style="color:var(--terminal-black);">
            📅 可释放时间段 (Available Slots)
            <span style="font-size: 10px; background: var(--matrix-green); color: #000; padding: 2px 6px; border: 1px solid #111; border-radius: 4px; animation: blink 1s step-end infinite;">LIVE</span>
        </div>
        <p style="font-size:12px;">点击下方时段提交预约申请。确认后你会收到一封自动邮件副本。</p>

        <div id="calendar-slots">
            </div>

        <form id="booking-form" action="https://formsubmit.co/{{ site.email }}" method="POST">
            <h3 style="margin-top:0;">确认预约</h3>
            <input type="hidden" name="_subject" value="新的陪伴 Termin 预约申请">
            <input type="hidden" name="_template" value="table">
            <input type="hidden" name="_next" value="{{ site.url }}{{ site.baseurl }}/termin/success/">
            <input type="hidden" name="_autoresponse" value="你的陪伴 Termin 预约申请已经收到。邮件里附有你提交的时间和联系方式；我会尽快人工确认最终安排。若需要更改或取消，请直接回复这封邮件。">
            <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
            <input type="hidden" name="selected_time" id="hidden-time">
            <div class="form-row">
                <label for="client-name">你的称呼:</label><br>
                <input id="client-name" class="termin-input" type="text" name="client_name" autocomplete="name" required>
            </div>
            <div class="form-row">
                <label for="client-email">Email:</label><br>
                <input id="client-email" class="termin-input" type="email" name="email" autocomplete="email" placeholder="name@example.com" required>
            </div>
            <div class="form-row">
                <label for="client-message">备注 / Telegram（可选）:</label><br>
                <textarea id="client-message" class="termin-input" name="message" rows="3" placeholder="例如：我要去外管局 / 希望 Telegram 联系 / 其他需要提前知道的边界"></textarea>
            </div>
            <p class="termin-note">提交后会跳转到确认页，并由 FormSubmit 给这个邮箱发送自动确认邮件。请保留页面默认的验证步骤；关闭验证会影响自动回复。</p>
            <button type="submit" class="save-btn" style="width:100%; padding:12px; background:var(--terminal-black); color:var(--matrix-green); border:none; cursor:pointer; font-weight:900; font-size: 16px; transition: 0.2s;">确认发送 Bestätigung</button>
        </form>
    </section>
</div>

<script>
    const slotGridContainer = document.getElementById('calendar-slots');
    const bookingForm = document.getElementById('booking-form');
    const hiddenTime = document.getElementById('hidden-time');

    // 核心打捞逻辑：异步读取并按月分组
    async function loadSlots() {
        try {
            const res = await fetch("{{ '/data/slots.json' | relative_url }}");
            if (!res.ok) throw new Error("信号源连接失败");

            const availableSlots = await res.json();

            if (availableSlots.length === 0) {
                slotGridContainer.innerHTML = `
                    <div style="text-align:center; padding: 20px; border: 1px dashed var(--hot-pink); color: var(--hot-pink);">
                        [⚠️ 当前暂无空闲频段，请等待下一次信号释放]
                    </div>`;
                return;
            }

            // 1. 数据分组与“时间段”转换器
            const groupedSlots = {};
            availableSlots.forEach(slot => {
                const [datePart, timePart] = slot.split(' ');
                const monthKey = datePart.substring(0, 7);

                const [hour, minute] = timePart.split(':');
                const endHour = String(parseInt(hour, 10) + 3).padStart(2, '0');
                const timeRange = `${timePart} - ${endHour}:${minute}`;

                if (!groupedSlots[monthKey]) {
                    groupedSlots[monthKey] = [];
                }

                groupedSlots[monthKey].push({
                    full: slot,
                    date: datePart,
                    time: timeRange
                });
            });

          // 2. 渲染手风琴折叠面板 (加入 termin-grid 容器)
            let htmlStr = '<div class="termin-grid">'; // 开启 2x2 网格

            for (const [month, slots] of Object.entries(groupedSlots)) {

                // 去掉了 open 相关的判断，直接输出纯净的 details 标签
                htmlStr += `
                <details class="month-group">
                    <summary class="month-title">
                        <span>📅 ${month} 频段</span>
                        <span style="font-size:12px; font-weight:normal;">[ 余量: ${slots.length} ]</span>
                    </summary>
                    <div class="slot-grid">
                        ${slots.map(s => `
                            <div class="time-slot" data-slot="${s.full}" onclick="selectSlot('${s.full}')">
                                <span class="date-part">${s.date}</span>
                                <span class="time-part">${s.time}</span>
                            </div>
                        `).join('')}
                    </div>
                </details>
                `;
            }
            htmlStr += '</div>'; // 关闭 2x2 网格

            slotGridContainer.style.display = 'block';
            slotGridContainer.innerHTML = htmlStr;

        } catch (error) {
            console.error("加载槽位出错:", error);
            slotGridContainer.innerHTML = `<div style="color: red;">❌ 无法读取时间槽，请检查数据库链路。</div>`;
        }
    }

    // 选中槽位后触发
    function selectSlot(time) {
        hiddenTime.value = time;
        bookingForm.style.display = 'block';

        document.querySelectorAll('.time-slot.selected').forEach(slot => slot.classList.remove('selected'));
        const selectedSlot = document.querySelector(`[data-slot="${time}"]`);
        if (selectedSlot) selectedSlot.classList.add('selected');

        const formTitle = bookingForm.querySelector('h3');
        if (formTitle) formTitle.innerText = `确认预约: ${time}`;

        bookingForm.scrollIntoView({ behavior: 'smooth' });
    }

    document.addEventListener('DOMContentLoaded', loadSlots);
</script>
