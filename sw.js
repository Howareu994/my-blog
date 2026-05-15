const CACHE_NAME = 'gegenstrom-v1';
const urlsToCache = [
  '/my-blog/',
  '/my-blog/assets/main.css'
];

// 安装阶段：把核心文件塞进手机缓存
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('缓存已打开');
        return cache.addAll(urlsToCache);
      })
  );
});

// 拦截阶段：断网时直接从缓存里拿东西
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        // 如果缓存里有，就直接给缓存；没有就去联网请求
        return response || fetch(event.request);
      })
  );
});