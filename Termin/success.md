---
layout: page
title: "预约信号已送达"
permalink: /termin/success/
---

<style>
    :root {
        --terminal-black: #111;
        --hot-pink: #ff4d94;
        --matrix-green: #00ff41;
        --bg-pink: #ffdae9;
    }

    .termin-success {
        max-width: 720px;
        margin: 0 auto;
        background: #fff;
        border: 3px solid var(--terminal-black);
        box-shadow: 8px 8px 0 var(--hot-pink);
        padding: 28px;
        color: var(--terminal-black);
    }

    .termin-success h2 { margin-top: 0; color: var(--hot-pink); }
    .termin-success p { line-height: 1.7; }
    .termin-success a {
        display: inline-block;
        margin-top: 12px;
        padding: 10px 14px;
        background: var(--terminal-black);
        color: var(--matrix-green);
        text-decoration: none;
        font-weight: 900;
    }
</style>

<div class="termin-success">
    <h2>预约申请已收到</h2>
    <p>如果你填写的邮箱无误，系统会发送一封自动确认邮件，里面包含你提交的预约信息。</p>
    <p>这封邮件代表“申请已收到”。我会再人工确认具体安排；如果需要更改或取消，直接回复确认邮件即可。</p>
    <a href="{{ '/termin/' | relative_url }}">返回陪伴 Termin</a>
</div>
