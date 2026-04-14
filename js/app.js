import { renderList } from './views/list.js';
import { renderDetail } from './views/detail.js';
import { renderMap, cleanupMap } from './views/map.js';
import { renderRoute, cleanupRoute } from './views/route.js';
import * as audio from './audio.js';
import { startTracking } from './proximity.js';

const app = document.getElementById('app');
let currentRoute = null;

function route() {
    const hash = location.hash || '#/';
    const match = hash.match(/^#\/miesto\/(.+)$/);

    if (currentRoute === 'map' && hash !== '#/mapa') cleanupMap();
    if (currentRoute === 'route' && hash !== '#/trasa') cleanupRoute();

    if (hash === '#/mapa') {
        audio.stop();
        renderMap(app);
        currentRoute = 'map';
    } else if (hash === '#/trasa') {
        audio.stop();
        renderRoute(app);
        currentRoute = 'route';
    } else if (match) {
        renderDetail(app, match[1]);
        currentRoute = 'detail';
    } else {
        audio.stop();
        renderList(app);
        currentRoute = 'list';
    }

    updateTabbar();
}

function updateTabbar() {
    const body = document.body;
    if (currentRoute === 'detail') {
        body.classList.remove('tabbar-visible');
    } else {
        body.classList.add('tabbar-visible');
    }

    document.querySelectorAll('.tab').forEach(tab => {
        tab.classList.toggle('active', tab.dataset.tab === currentRoute);
    });
}

window.addEventListener('hashchange', route);
window.addEventListener('DOMContentLoaded', () => {
    route();
    startTracking();
});
window.addEventListener('popstate', route);
