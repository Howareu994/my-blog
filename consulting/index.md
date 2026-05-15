---
layout: page
title: "🛋️ 能量急救窗"
permalink: /consulting/
---

<style>
    /* 专属定制的柔和商业色彩系统 */
    :root {
        --calm-blue: #4A90E2;
        --soft-pink: #fdf3f6;
        --text-dark: #2c3e50;
        --text-muted: #7f8c8d;
        --card-bg: #ffffff;
        --border-soft: #eaeaea;
        --shadow-soft: 0 8px 30px rgba(0, 0, 0, 0.04);
    }

    .consulting-container {
        max-width: 750px;
        margin: 0 auto;
        color: var(--text-dark);
    }

    /* 1. 咨询师名片 */
    .profile-card {
        background: var(--card-bg);
        border-radius: 20px;
        padding: 35px;
        box-shadow: var(--shadow-soft);
        margin-bottom: 35px;
        border: 1px solid var(--border-soft);
        text-align: center;
    }
    .avatar-wrapper {
        width: 90px; height: 90px;
        background: var(--soft-pink);
        border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-size: 40px; margin: 0 auto 20px auto;
    }
    .profile-card h2 { margin: 0 0 10px 0; color: var(--text-dark); font-weight: 700; }
    .profile-card p { margin: 0; color: var(--text-muted); font-size: 15px; line-height: 1.6; }

    /* 2. 咨访契约 */
    .ethics-section {
        background: #f8f9fa;
        border-radius: 16px;
        padding: 30px;
        margin-bottom: 35px;
    }
    .ethics-title {
        color: var(--calm-blue); font-weight: 700;
        margin-bottom: 20px; display: flex; align-items: center; gap: 8px; font-size: 18px;
    }
    .ethics-list { list-style: none; padding: 0; margin: 0; font-size: 15px; color: var(--text-dark); }
    .ethics-list li { margin-bottom: 15px; display: flex; gap: 12px; align-items: flex-start; line-height: 1.5; }
    .icon-safe { color: #27ae60; font-size: 18px; }
    .icon-warn { color: #e74c3c; font-size: 18px; }

    /* 3. 预约模块 */
    .booking-section {
        background: var(--card-bg);
        border-radius: 20px;
        padding: 35px;
        box-shadow: var(--shadow-soft);
        border: 1px solid var(--border-soft);
    }

    /* 🔥 新增：2x2 矩阵网格 */
    .consulting-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 15px;
        margin-top: 15px;
    }
    @media (max-width: 600px) {
        .consulting-grid { grid-template-columns: 1fr; }
    }

    /* 🔥 闭合状态的呼吸卡片 */
    .month-group {
        border: 1px solid var(--border-soft);
        background: #fff;
        border-radius: 12px;
        transition: all 0.3s ease;
        animation: calm-pulse 2.5s infinite alternate;
        box-shadow: var(--shadow-soft);
    }

    .month-group:hover {
        transform: translateY(-2px);
        border-color: var(--calm-blue);
        box-shadow: 0 6px 20px rgba(74, 144, 226, 0.15);
        animation: none; /* 悬停时停止闪烁 */
    }

    /* 🔥 展开状态：停止呼吸，边框固定为蓝色 */
    details[open].month-group {
        animation: none;
        border-color: var(--calm-blue);
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }

    /* 柔和的海洋蓝呼吸灯动画 */
    @keyframes calm-pulse {
        0% { box-shadow: 0 0 0px rgba(74, 144, 226, 0); border-color: var(--border-soft); }
        50% { box-shadow: 0 0 15px rgba(74, 144, 226, 0.3); border-color: rgba(74, 144, 226, 0.6); }
        100% { box-shadow: 0 0 0px rgba(74, 144, 226, 0); border-color: var(--border-soft); }
    }

    .month-title {
        padding: 15px; font-weight: 600; color: var(--text-dark);
        cursor: pointer; display: flex; align-items: center; justify-content: space-between;
        list-style: none; font-size: 16px; transition: color 0.3s;
        border-radius: 12px;
    }
    .month-title::-webkit-details-marker { display: none; }
    .month-title:hover { color: var(--calm-blue); }
    details[open] .month-title { border-bottom: 1px solid var(--border-soft); border-bottom-left-radius: 0; border-bottom-right-radius: 0; }

    .slot-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(135px, 1fr));
        gap: 15px; padding: 15px;
    }

    .time-slot {
        background: #fff; border: 1px solid #dcdde1; border-radius: 12px;
        padding: 15px 10px; text-align: center;
        cursor: pointer; transition: all 0.25s ease;
    }
    .time-slot:hover {
        background: var(--calm-blue); color: #fff;
        border-color: var(--calm-blue); transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(74, 144, 226, 0.2);
    }
    .time-slot span.date-part { font-size: 12px; opacity: 0.7; display: block; margin-bottom: 4px; }
    .time-slot span.time-part { font-size: 16px; font-weight: 600; }

    /* 表单 */
    #booking-form {
        display: none; margin-top: 30px; background: #f8f9fa;
        padding: 30px; border-radius: 16px;
    }
    .input-field {
        width: 100%; padding: 12px 15px; border: 1px solid #dcdde1;
        border-radius: 8px; margin-top: 8px; font-size: 15px;
    }
    .input-field:focus { border-color: var(--calm-blue); outline: none; }

    .submit-btn {
        width: 100%; padding: 14px; background: var(--calm-blue);
        color: white; border: none; border-radius: 8px; font-size: 16px;
        font-weight: 600; cursor: pointer; margin-top: 20px; transition: background 0.3s;
    }
    .submit-btn:hover { background: #357abd; }
</style>

<div class="consulting-container">
    <section class="profile-card">
        <div class="avatar-wrapper">🛋️</div>
        <h2>心理能量急救与支持</h2>
        <p>这里是一个安全、无评判的倾听空间。<br>我提供短期心理疏导、情绪急救以及异国生存压力支持。<br>每一次对话，都是一次重新锚定内心的过程。</p>
    </section>

    <section class="ethics-section">
        <div class="ethics-title"><i class="ri-shield-check-line"></i> 咨访契约 (Ethics & Boundaries)</div>
        <ul class="ethics-list">
            <li><span class="icon-safe">🌿</span> <span><strong>绝对保密：</strong> 所有的对话内容将严格保密，除非涉及对您或他人的严重生命威胁。</span></li>
            <li><span class="icon-safe">🌿</span> <span><strong>专业边界：</strong> 咨询时间严格遵照预约时段。保持双边尊重，咨询外不进行私人社交。</span></li>
            <li><span class="icon-warn">⚠️</span> <span><strong>非医疗替代：</strong> 我提供心理支持与辅导。若经历严重的精神疾病发作，请立即寻求医疗系统帮助。</span></li>
        </ul>
    </section>

    <section class="booking-section">
        <h3 style="margin-top:0; margin-bottom: 5px; color:var(--text-dark);">选择咨询时间</h3>
        <p style="color:var(--text-muted); font-size: 14px; margin-bottom: 10px;">排期仅显示柏林时间的可用时段。</p>

        <div id="calendar-slots">
            </div>

        <form id="booking-form">
            <h3 style="margin-top:0; color:var(--text-dark);">确认预约信息</h3>
            <input type="hidden" id="hidden-time">
            <div style="margin-bottom:15px;">
                <label style="color:var(--text-muted); font-size:14px;">您的称呼 / 化名:</label>
                <input type="text" class="input-field" placeholder="如何称呼您？" required>
            </div>
            <div style="margin-bottom:15px;">
                <label style="color:var(--text-muted); font-size:14px;">联络方式 (Email 或 Telegram):</label>
                <input type="text" class="input-field" placeholder="用于接收确认信息" required>
            </div>
            <button type="button" class="submit-btn" onclick="alert('前端界面测试正常。邮件闭环暂未接入。')">提交预约请求</button>
        </form>
    </section>
</div>

<script>
    const slotGridContainer = document.getElementById('calendar-slots');
    const bookingForm = document.getElementById('booking-form');
    const hiddenTime = document.getElementById('hidden-time');

    async function loadSlots() {
        try {
            const res = await fetch("{{ '/data/consulting_slots.json' | relative_url }}");
            if (!res.ok) throw new Error("连接失败");

            const availableSlots = await res.json();

            if (availableSlots.length === 0) {
                slotGridContainer.innerHTML = `
                    <div style="text-align:center; padding: 30px; background:#f8f9fa; border-radius:12px; color: var(--text-muted);">
                        🌿 当前暂无空闲咨询时段，请稍后再来看看。
                    </div>`;
                return;
            }

            const groupedSlots = {};

            availableSlots.forEach(slot => {
                const datePart = slot.substring(0, 10);
                const timeRange = slot.substring(11);
                const monthKey = datePart.substring(0, 7);

                if (!groupedSlots[monthKey]) { groupedSlots[monthKey] = []; }

                groupedSlots[monthKey].push({
                    full: slot,
                    date: datePart,
                    time: timeRange
                });
            });

            // 🔥 改动：加入 2x2 网格容器，并移除了 open 属性
            let htmlStr = '<div class="consulting-grid">';

            for (const [month, slots] of Object.entries(groupedSlots)) {

                // 输出纯净的 details 标签，默认全部折叠
                htmlStr += `
                <details class="month-group">
                    <summary class="month-title">
                        <span>📅 ${month} 排期</span>
                        <span style="font-size:13px; color:var(--text-muted); font-weight:normal;">剩余 ${slots.length} 个</span>
                    </summary>
                    <div class="slot-grid">
                        ${slots.map(s => `
                            <div class="time-slot" onclick="selectSlot('${s.full}')">
                                <span class="date-part">${s.date}</span>
                                <span class="time-part">${s.time}</span>
                            </div>
                        `).join('')}
                    </div>
                </details>
                `;
            }
            htmlStr += '</div>';

            slotGridContainer.innerHTML = htmlStr;

        } catch (error) {
            console.error("加载槽位出错:", error);
            slotGridContainer.innerHTML = `<div style="text-align:center; color: #e74c3c;">暂无排期数据，请确保 data/consulting_slots.json 已正确生成。</div>`;
        }
    }

    function selectSlot(time) {
        hiddenTime.value = time;
        bookingForm.style.display = 'block';
        const formTitle = bookingForm.querySelector('h3');
        if (formTitle) formTitle.innerText = `确认预约: ${time} (柏林时间)`;
        bookingForm.scrollIntoView({ behavior: 'smooth' });
    }

    document.addEventListener('DOMContentLoaded', loadSlots);
</script>