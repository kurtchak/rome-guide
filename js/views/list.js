import { PLACES } from '../data.js';

let currentFilter = 'all';
let currentContainer = null;

function getDistance(lat1, lon1, lat2, lon2) {
    const R = 6371000;
    const dLat = (lat2 - lat1) * Math.PI / 180;
    const dLon = (lon2 - lon1) * Math.PI / 180;
    const a = Math.sin(dLat / 2) ** 2 +
        Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *
        Math.sin(dLon / 2) ** 2;
    return R * 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
}

function formatDistance(m) {
    if (m < 1000) return `${Math.round(m)} m`;
    return `${(m / 1000).toFixed(1)} km`;
}

export function renderList(container) {
    currentContainer = container;
    container.innerHTML = `
        <div class="header">
            <h1>Audiosprievodca</h1>
            <p>Rím a Vatikán</p>
        </div>
        <div class="filters">
            <button class="filter-btn ${currentFilter === 'all' ? 'active' : ''}" data-filter="all">Všetky</button>
            <button class="filter-btn ${currentFilter === 'vatikan' ? 'active' : ''}" data-filter="vatikan">Vatikán</button>
            <button class="filter-btn ${currentFilter === 'rim' ? 'active' : ''}" data-filter="rim">Rím</button>
        </div>
        <div id="nearby-section"></div>
        <div class="grid">
            ${getFilteredPlaces().map(place => `
                <div class="card" data-id="${place.id}">
                    <img class="card-img"
                         src="${place.image}"
                         alt="${place.name}"
                         onerror="this.style.display='none';this.nextElementSibling.style.display='flex';"
                         loading="lazy">
                    <div class="card-img-placeholder" style="display:none">${place.emoji}</div>
                    <div class="card-label">
                        <span class="card-category">${place.category === 'vatikan' ? 'Vatikán' : 'Rím'}</span>
                        ${place.name}
                    </div>
                </div>
            `).join('')}
        </div>
    `;

    container.querySelectorAll('.filter-btn[data-filter]').forEach(btn => {
        btn.addEventListener('click', () => {
            currentFilter = btn.dataset.filter;
            renderList(container);
        });
    });

    container.querySelectorAll('.card').forEach(card => {
        card.addEventListener('click', () => {
            location.hash = `/miesto/${card.dataset.id}`;
        });
    });

    loadNearby();
}

function loadNearby() {
    if (!navigator.geolocation) return;

    navigator.geolocation.getCurrentPosition(
        (pos) => renderNearby(pos.coords.latitude, pos.coords.longitude),
        () => {},
        { enableHighAccuracy: false, timeout: 5000, maximumAge: 120000 }
    );
}

function renderNearby(lat, lon) {
    const section = document.getElementById('nearby-section');
    if (!section) return;

    const withDistance = PLACES
        .filter(p => p.coords)
        .map(p => ({
            place: p,
            dist: getDistance(lat, lon, p.coords.lat, p.coords.lon),
        }))
        .sort((a, b) => a.dist - b.dist)
        .slice(0, 5);

    if (withDistance.length === 0) return;

    // Ak je najbližšie miesto viac ako 50 km, nezobraz
    if (withDistance[0].dist > 50000) return;

    section.innerHTML = `
        <div class="nearby">
            <h3 class="nearby-title">V okolí</h3>
            <div class="nearby-scroll">
                ${withDistance.map(({ place, dist }) => `
                    <div class="nearby-card" data-id="${place.id}">
                        <img src="${place.image}"
                             alt="${place.name}"
                             onerror="this.style.display='none';this.nextElementSibling.style.display='flex';"
                             loading="lazy">
                        <div class="nearby-card-placeholder" style="display:none">${place.emoji}</div>
                        <div class="nearby-card-body">
                            <div class="nearby-card-name">${place.name}</div>
                            <div class="nearby-card-dist">${formatDistance(dist)}</div>
                        </div>
                    </div>
                `).join('')}
            </div>
        </div>
    `;

    section.querySelectorAll('.nearby-card').forEach(card => {
        card.addEventListener('click', () => {
            location.hash = `/miesto/${card.dataset.id}`;
        });
    });
}

function getFilteredPlaces() {
    if (currentFilter === 'all') return PLACES;
    return PLACES.filter(p => p.category === currentFilter);
}
