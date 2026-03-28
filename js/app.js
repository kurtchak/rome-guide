import { renderList } from './views/list.js';
import { renderDetail } from './views/detail.js';
import * as audio from './audio.js';
import { startTracking } from './proximity.js';

const app = document.getElementById('app');

function route() {
    const hash = location.hash || '#/';
    const match = hash.match(/^#\/miesto\/(.+)$/);

    if (match) {
        renderDetail(app, match[1]);
    } else {
        audio.stop();
        renderList(app);
    }
}

window.addEventListener('hashchange', route);
window.addEventListener('DOMContentLoaded', () => {
    route();
    startTracking();
});

// Handle back navigation
window.addEventListener('popstate', route);
