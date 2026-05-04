---
layout: page
title: 🏠 Start
permalink: /de/
---

<div class="creative-layout">

  <div class="status-module">
    <div class="status-header">
      <span class="status-prefix">🌱 STATUS-LOG</span>
    </div>

    <div class="input-group">
      <input type="text" id="status-input" autocomplete="off" placeholder="Berliner Sommer-Perlen fischen..." />
      <button id="save-status-btn" class="pixel-save-btn">SAVE</button>
    </div>

    <div id="status-history-container">
      <ul id="status-history-list" style="list-style:none; padding:0; margin:0;"></ul>
    </div>
  </div>

  <div class="computer-group-top">
    <a href="https://strudel.cc/" target="_blank" style="text-decoration:none;">
      <div class="btn-screen" id="screen-strudel">
        <div style="color:#FBC02D; text-shadow:0 0 10px #FBC02D; z-index:10; font-weight:bold; font-size:20px;">STRUDEL</div>
        <!-- 注意：这里去掉了 opacity:0.5; -->
        <div class="matrix-bg" style="position:absolute; top:0; left:0; width:100%; height:100%; padding:10px;"></div>
      </div>
      <div style="width:100%; height:6px; background:#00008B; margin-top:2px;"></div>
    </a>

    <a href="https://hydra.ojack.xyz/" target="_blank" style="text-decoration:none;">
      <div class="btn-screen" id="screen-hydra">
        <div style="color:#87CEFA; text-shadow:0 0 10px #87CEFA; z-index:10; font-weight:bold; font-size:20px;">HYDRA</div>
        <!-- 注意：这里去掉了 opacity:0.5; -->
        <div class="matrix-bg" style="position:absolute; top:0; left:0; width:100%; height:100%; padding:10px;"></div>
      </div>
      <div style="width:100%; height:6px; background:#00008B; margin-top:2px;"></div>
    </a>
  </div>

  <div class="nook-module">
    <div class="soundcloud-wrapper">
      <iframe width="100%" height="250" scrolling="no" frameborder="no" allow="autoplay" 
        src="https://w.soundcloud.com/player/?url=https%3A//soundcloud.com/ellen-allien&color=%230000ff&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true">
      </iframe>
    </div>
    <div class="module-label-pink">SN-06 / AUDIO STATION</div>
  </div>

</div>

<!-- 下面是更新后的 JavaScript -->
<script>
  (function() {
    window.addEventListener('pageshow', function() {
      const input = document.getElementById('status-input');
      if (input) { input.value = ''; }
    });

    function fillMatrix(id) {
      const el = document.querySelector(`#${id} .matrix-bg`);
      
      // 自动获取当前月份的实际天数和今天的日期
      const now = new Date();
      const today = now.getDate();
      const daysInMonth = new Date(now.getFullYear(), now.getMonth() + 1, 0).getDate();
      
      let h = `<div style="display:grid; grid-template-columns:repeat(7,1fr); gap:4px;">`;
      
      for(let d = 1; d <= daysInMonth; d++) {
        const isToday = (d === today) ? 'is-today' : '';
        // 生成 0 到 1.5 秒的随机延迟，实现“逐字随机点亮”
        const randomDelay = (Math.random() * 1.5).toFixed(2);
        
        h += `<span class="matrix-cell ${isToday}" style="animation-delay: ${randomDelay}s">${d}</span>`;
      }
      el.innerHTML = h + `</div>`;
    }
    
    fillMatrix('screen-strudel'); 
    fillMatrix('screen-hydra');

    const input = document.getElementById('status-input');
    const btn = document.getElementById('save-status-btn');
    const list = document.getElementById('status-history-list');

    function refresh() {
      const now = Date.now();
      let history = JSON.parse(localStorage.getItem('nook_history') || "[]");
      history = history.filter(i => (now - i.time) < 86400000);
      localStorage.setItem('nook_history', JSON.stringify(history));
      list.innerHTML = history.map(i => {
        const rem = Math.round((86400000 - (now - i.time)) / 3600000);
        return `<li class="locked-status"><span>${i.text}</span><span style="font-size:10px; opacity:0.6;">⌛ ${rem}h</span></li>`;
      }).reverse().join('');
    }

    btn.addEventListener('click', () => {
      if (!input.value.trim()) return; 
      let history = JSON.parse(localStorage.getItem('nook_history') || "[]");
      history.push({ text: input.value, time: Date.now() });
      localStorage.setItem('nook_history', JSON.stringify(history));
      input.value = ''; 
      refresh();
      if(window.confetti) window.confetti({ particleCount:100, origin:{y:0.7}, colors:['#ff4d94','#00ff41','#87CEFA'] });
    });
    refresh();
  })();
</script>