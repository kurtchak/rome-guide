const CACHE_NAME = 'audiosprievodca-v9';

const SHELL_ASSETS = [
    './',
    './index.html',
    './css/style.css',
    './js/data.js',
    './js/audio.js',
    './js/proximity.js',
    './js/app.js',
    './js/views/list.js',
    './js/views/detail.js',
    './js/views/map.js',
    './js/views/route.js',
    './manifest.json'
];

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => cache.addAll(SHELL_ASSETS))
            .then(() => self.skipWaiting())
    );
});

self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys()
            .then(keys => Promise.all(
                keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k))
            ))
            .then(() => self.clients.claim())
    );
});

self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request).then(cached => {
            if (cached) return cached;
            return fetch(event.request).then(response => {
                if (response.ok && event.request.method === 'GET') {
                    const clone = response.clone();
                    caches.open(CACHE_NAME).then(cache => cache.put(event.request, clone));
                }
                return response;
            });
        })
    );
});

// Klik na notifikáciu -> otvorí detail miesta
self.addEventListener('notificationclick', (event) => {
    event.notification.close();

    const placeId = event.notification.data?.placeId;
    const url = placeId ? `/#/miesto/${placeId}` : '/';

    event.waitUntil(
        clients.matchAll({ type: 'window', includeUncontrolled: true }).then(windowClients => {
            for (const client of windowClients) {
                if (client.url.includes(self.registration.scope)) {
                    client.navigate(url);
                    return client.focus();
                }
            }
            return clients.openWindow(url);
        })
    );
});
