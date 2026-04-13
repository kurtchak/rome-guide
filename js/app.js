import { renderList } from './views/list.js';
import { renderDetail } from './views/detail.js';
import { renderMap, cleanupMap } from './views/map.js';
import * as audio from './audio.js';
import { startTracking } from './proximity.js';

const app = document.getElementById('app');
let currentRoute = null;

function route() {
    const hash = location.hash || '#/';
    const match = hash.match(/^#\/miesto\/(.+)$/);

    // Cleanup predchádzajúcej mapy
    if (currentRoute === 'map' && hash !== '#/mapa') {
        cleanupMap();
    }

    if (hash === '#/mapa') {
        audio.stop();
        renderMap(app);
        currentRoute = 'map';
    } else if (match) {
        renderDetail(app, match[1]);
        currentRoute = 'detail';
    } else {
        audio.stop();
        renderList(app);
        currentRoute = 'list';
    }
}

window.addEventListener('hashchange', route);
window.addEventListener('DOMContentLoaded', () => {
    route();
    startTracking();
});
window.addEventListener('popstate', route);
