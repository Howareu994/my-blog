---
layout: page
title: "📢 Stadtpuls"
permalink: /de/news/
---

{% include news-style.html %}

<div class="dashboard-container">

    <div class="weather-hero">
        <div>
            <div class="weather-temp" id="w-temp">--°C</div>
            <div id="w-desc">Suche nach Signalen...</div>
        </div>
        <div class="weather-info" style="text-align: right; font-size: 13px;">
            <div id="w-wind">💨 Wind: -- km/h</div>
            <div id="w-hum">💧 Feuchte: --%</div>
            <div id="w-time" style="opacity: 0.7; margin-top: 5px;">Update: --:--</div>
        </div>
    </div>

    <div class="survival-accordion">
        <details>
            <summary>
                <div class="star-title">Berlin Survival-Guide (Überlebenshandbuch)</div>
                <div class="fat-arrow">↓↓↓</div>
            </summary>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px; margin-top: 15px; cursor: default;">
                <div style="font-size: 13px;">
                    <strong style="color: #ff4d94;">🥗 Rationen: Lokale Wochenmärkte</strong>
                    <ul style="padding-left: 0; list-style: none; margin-top: 8px;">
                        <li style="margin-bottom: 5px;">📍 <a href="https://www.google.com/maps/search/?api=1&query=Genter+Markt+Berlin" target="_blank">Genter Markt (Wedding) ↗</a></li>
                        <li style="margin-bottom: 5px;">📍 <a href="https://www.google.com/maps/search/?api=1&query=Maybachufer+12047+Berlin" target="_blank">Maybachufer (Neukölln) ↗</a></li>
                        <li style="margin-bottom: 5px;">📍 <a href="https://www.google.com/maps/search/?api=1&query=Crellestrasse+10827+Berlin" target="_blank">Crelle Markt (Schöneberg) ↗</a></li>
                    </ul>
                </div>
                <div style="font-size: 13px;">
                    <strong style="color: #ff4d94;">📦 Straßenkodex: Zu Verschenken</strong>
                    <p style="font-size: 11px; margin-top: 8px; line-height: 1.5; color: #64748b;">
                        - <strong>WARNUNG:</strong> Keine Polstermöbel (Matratzen/Sofas) mitnehmen. <b>Bettwanzen</b> sind eine Plage in Berlin. Einmal drin, wird's richtig teuer.<br>
                        - <strong>REGELN:</strong> Kartons max. 24h auf dem Gehweg. Nichts aus Kleiderspenden-Containern klauen.
                    </p>
                </div>
                <div style="font-size: 13px;">
                    <strong style="color: #ff4d94;">💼 Job-Radar 2026</strong>
                    <ul id="job-fair-list" style="padding-left: 0; list-style: none; margin-top: 8px;">
                        <li>Suche nach Jobmessen...</li>
                    </ul>
                </div>
            </div>
        </details>
    </div>

    <div class="search-box">
        <input type="text" id="berlin-search" placeholder="Suche Antworten in Berlin (Google / BVG / Polizei)...">
    </div>

    <div class="news-grid">
        <div class="news-card">
            <h4 class="tag-vbb"><span>🚆 BVG & Streiks</span> <span class="refresh-btn" onclick="displayTraffic()">🔄</span></h4>
            <ul id="vbb-list"><li>Warte auf Signale...</li></ul>
        </div>

        <div class="news-card">
            <h4 class="tag-safe"><span>🛡️ Polizei-Ticker</span> <span class="refresh-btn" onclick="displayPolice()">🔄</span></h4>
            <ul id="police-list"><li>Synchronisiere Daten...</li></ul>
        </div>

        <div class="news-card">
            <h4 class="tag-life"><span>🎡 For Free</span> <span class="refresh-btn" onclick="displayFree()">🔄</span></h4>
            <ul id="free-list"><li>Lade Feeds...</li></ul>
        </div>

        <div class="news-card" style="border-color: rgba(204, 0, 255, 0.2);">
            <h4 class="tag-club"><span>🪩 Szene & Clubs</span> <span class="refresh-btn" onclick="displayCulture()">🔄</span></h4>
            <ul id="club-list"><li>Synchronisiere...</li></ul>
        </div>
    </div>

    <footer class="site-footer-custom">
        <p style="color: #94a3b8; font-size: 11px;">
            Live-Daten aus Berliner Quellen · Viel Glück beim Überleben.
        </p>
    </footer>
</div>

<!-- 复用你之前的自动展开脚本 -->
<style>
    .survival-accordion details[open] > div {
        animation: elasticDrop 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
        transform-origin: top center;
    }
    @keyframes elasticDrop {
        from { opacity: 0; transform: translateY(-20px) scale(0.95); }
        to { opacity: 1; transform: translateY(0) scale(1); }
    }
    .survival-accordion details:not([open]) .fat-arrow {
        animation: hintJump 1s infinite alternate;
    }
    @keyframes hintJump {
        from { transform: translateY(0); }
        to { transform: translateY(5px); color: #ff1493; }
    }
</style>

<script>
    document.addEventListener('DOMContentLoaded', function() {
        setTimeout(function() {
            const survivalDetails = document.querySelector('.survival-accordion details');
            if (survivalDetails) { survivalDetails.setAttribute('open', ''); }
        }, 3000); 
    });
</script>

{% include news-script.html %}