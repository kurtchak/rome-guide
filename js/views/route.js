import { PLACES, HOME } from '../data.js';

const ROME_CENTER = [41.902, 12.480];

let map = null;
let markers = [];
let routeLine = null;
let startMarker = null;
let selectedIds = new Set();
let startMode = 'gps'; // 'gps' | 'home' | 'place'
let startCoords = null; // {lat, lon, label}
let gpsPosition = null;

function haversine(a, b) {
    const R = 6371000;
    const dLat = (b.lat - a.lat) * Math.PI / 180;
    const dLon = (b.lon - a.lon) * Math.PI / 180;
    const x = Math.sin(dLat / 2) ** 2 +
        Math.cos(a.lat * Math.PI / 180) * Math.cos(b.lat * Math.PI / 180) *
        Math.sin(dLon / 2) ** 2;
    return R * 2 * Math.atan2(Math.sqrt(x), Math.sqrt(1 - x));
}

// Nearest-neighbor route, s 2-opt vylepšením na konci
function optimizeRoute(start, places) {
    if (places.length === 0) return [];

    const remaining = [...places];
    const route = [];
    let current = start;

    while (remaining.length > 0) {
        let bestIdx = 0;
        let bestDist = Infinity;
        for (let i = 0; i < remaining.length; i++) {
            const d = haversine(current, remaining[i].coords);
            if (d < bestDist) {
                bestDist = d;
                bestIdx = i;
            }
        }
        route.push(remaining[bestIdx]);
        current = remaining[bestIdx].coords;
        remaining.splice(bestIdx, 1);
    }

    // 2-opt
    let improved = true;
    while (improved) {
        improved = false;
        for (let i = 0; i < route.length - 1; i++) {
            for (let j = i + 1; j < route.length; j++) {
                const a = i === 0 ? start : route[i - 1].coords;
                const b = route[i].coords;
                const c = route[j].coords;
                const d = j < route.length - 1 ? route[j + 1].coords : null;
                const currentDist = haversine(a, b) + (d ? haversine(c, d) : 0);
                const newDist = haversine(a, c) + (d ? haversine(b, d) : 0);
                if (newDist + 0.1 < currentDist) {
                    route.splice(i, j - i + 1, ...route.slice(i, j + 1).reverse());
                    improved = true;
                }
            }
        }
    }

    return route;
}

function formatDist(m) {
    if (m < 1000) return `${Math.round(m)} m`;
    return `${(m / 1000).toFixed(1)} km`;
}

function formatTime(min) {
    if (min < 60) return `${Math.round(min)} min`;
    const h = Math.floor(min / 60);
    const m = Math.round(min % 60);
    return m ? `${h} h ${m} min` : `${h} h`;
}

function getStartCoords() {
    if (startMode === 'home') return { ...HOME.coords, label: 'Ubytovanie' };
    if (startMode === 'place' && startCoords) return startCoords;
    if (gpsPosition) return { ...gpsPosition, label: 'Moja poloha' };
    return null;
}

export function renderRoute(container) {
    container.innerHTML = `
        <div class="route-header">
            <h2>Plán trasy</h2>
        </div>
        <div class="route-controls">
            <div class="route-row">
                <label class="route-label">Štart:</label>
                <select id="start-select" class="route-select">
                    <option value="gps">📍 Moja poloha</option>
                    <option value="home">🏠 Ubytovanie</option>
                    <option value="place">📌 Vybrať miesto</option>
                </select>
            </div>
            <div id="start-place-picker" class="route-row" style="display:none">
                <select id="start-place-select" class="route-select">
                    <option value="">-- vyber miesto --</option>
                    ${PLACES.filter(p => p.coords).map(p => `
                        <option value="${p.id}">${p.emoji} ${p.name}</option>
                    `).join('')}
                </select>
            </div>
            <div class="route-row route-chips">
                <button class="route-chip" data-action="add-vatikan">+ Celý Vatikán</button>
                <button class="route-chip" data-action="add-rim">+ Celý Rím</button>
                <button class="route-chip route-chip-clear" data-action="clear">Vymazať</button>
            </div>
        </div>
        <div id="route-map" class="route-map"></div>
        <div id="route-summary" class="route-summary"></div>
        <div class="route-list">
            <h3 class="route-list-title">Miesta (<span id="sel-count">0</span>)</h3>
            <div id="route-places"></div>
        </div>
    `;

    document.getElementById('start-select').value = startMode;
    document.getElementById('start-select').addEventListener('change', (e) => {
        startMode = e.target.value;
        const picker = document.getElementById('start-place-picker');
        picker.style.display = startMode === 'place' ? 'flex' : 'none';
        if (startMode !== 'place') startCoords = null;
        refreshAll();
    });

    document.getElementById('start-place-select').addEventListener('change', (e) => {
        const placeId = e.target.value;
        const place = PLACES.find(p => p.id === placeId);
        if (place?.coords) {
            startCoords = { ...place.coords, label: place.name };
        } else {
            startCoords = null;
        }
        refreshAll();
    });

    container.querySelectorAll('.route-chip').forEach(btn => {
        btn.addEventListener('click', () => handleChip(btn.dataset.action));
    });

    initMap();
    refreshPlacesList();
    refreshRoute();

    // Auto-get GPS
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (pos) => {
                gpsPosition = { lat: pos.coords.latitude, lon: pos.coords.longitude };
                if (startMode === 'gps') refreshAll();
            },
            () => {},
            { enableHighAccuracy: true, timeout: 8000, maximumAge: 60000 }
        );
    }
}

function handleChip(action) {
    if (action === 'add-vatikan') {
        PLACES.filter(p => p.category === 'vatikan').forEach(p => selectedIds.add(p.id));
    } else if (action === 'add-rim') {
        PLACES.filter(p => p.category === 'rim').forEach(p => selectedIds.add(p.id));
    } else if (action === 'clear') {
        selectedIds.clear();
    }
    refreshAll();
}

function initMap() {
    if (typeof L === 'undefined') {
        document.getElementById('route-map').innerHTML = '<div class="loading">Mapa nie je dostupná</div>';
        return;
    }
    map = L.map('route-map', { zoomControl: true }).setView(ROME_CENTER, 13);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap',
    }).addTo(map);
}

function refreshAll() {
    refreshPlacesList();
    refreshRoute();
}

function refreshPlacesList() {
    const container = document.getElementById('route-places');
    document.getElementById('sel-count').textContent = selectedIds.size;

    const ordered = [
        ...PLACES.filter(p => selectedIds.has(p.id)),
        ...PLACES.filter(p => !selectedIds.has(p.id)),
    ];

    container.innerHTML = ordered.map(place => `
        <label class="route-item ${selectedIds.has(place.id) ? 'selected' : ''}" data-id="${place.id}">
            <input type="checkbox" ${selectedIds.has(place.id) ? 'checked' : ''}>
            <span class="route-item-emoji">${place.emoji}</span>
            <span class="route-item-name">${place.name}</span>
            <span class="route-item-cat">${place.category === 'vatikan' ? 'Vatikán' : 'Rím'}</span>
        </label>
    `).join('');

    container.querySelectorAll('.route-item input').forEach(input => {
        input.addEventListener('change', (e) => {
            const id = e.target.closest('.route-item').dataset.id;
            if (e.target.checked) selectedIds.add(id);
            else selectedIds.delete(id);
            refreshAll();
        });
    });
}

function refreshRoute() {
    if (!map) return;

    // Cleanup starých vrstiev
    markers.forEach(m => m.remove());
    markers = [];
    if (routeLine) { routeLine.remove(); routeLine = null; }
    if (startMarker) { startMarker.remove(); startMarker = null; }

    const start = getStartCoords();
    const selected = PLACES.filter(p => selectedIds.has(p.id) && p.coords);

    const summary = document.getElementById('route-summary');

    if (!start) {
        summary.innerHTML = '<div class="route-summary-hint">Čaká sa na polohu… (povoľ GPS alebo zvoľ iný štart)</div>';
    }

    if (selected.length === 0) {
        if (start) summary.innerHTML = '<div class="route-summary-hint">Vyber miesta, ktoré chceš navštíviť.</div>';
        return;
    }

    const orderedRoute = start
        ? optimizeRoute(start, selected)
        : selected;

    // Start marker
    if (start) {
        const startIcon = L.divIcon({
            html: `<div class="route-pin route-pin-start">🏁</div>`,
            className: 'map-pin-wrapper',
            iconSize: [36, 36],
            iconAnchor: [18, 18],
        });
        startMarker = L.marker([start.lat, start.lon], { icon: startIcon }).addTo(map);
        startMarker.bindPopup(`<strong>Štart:</strong> ${start.label || ''}`);
    }

    // Place pins s číslovaním
    const latlngs = start ? [[start.lat, start.lon]] : [];
    orderedRoute.forEach((place, idx) => {
        const icon = L.divIcon({
            html: `<div class="route-pin route-pin-num">${idx + 1}</div>`,
            className: 'map-pin-wrapper',
            iconSize: [36, 36],
            iconAnchor: [18, 18],
        });
        const marker = L.marker([place.coords.lat, place.coords.lon], { icon }).addTo(map);
        marker.bindPopup(`<strong>${idx + 1}. ${place.name}</strong>`);
        markers.push(marker);
        latlngs.push([place.coords.lat, place.coords.lon]);
    });

    // Spojnica
    if (latlngs.length >= 2) {
        routeLine = L.polyline(latlngs, {
            color: '#e94560',
            weight: 4,
            opacity: 0.75,
            dashArray: '8 6',
        }).addTo(map);
    }

    // Fit bounds
    if (latlngs.length) {
        map.fitBounds(latlngs, { padding: [40, 40], maxZoom: 15 });
    }

    // Summary
    let totalDist = 0;
    const stops = [];
    let prev = start;
    orderedRoute.forEach((place, idx) => {
        const d = prev ? haversine(prev, place.coords) : 0;
        totalDist += d;
        stops.push({ place, dist: d, idx });
        prev = place.coords;
    });
    const walkingMin = (totalDist / 1000) * 12; // ~12 min/km

    const gmapsUrl = buildGoogleMapsUrl(start, orderedRoute);

    summary.innerHTML = `
        <div class="route-summary-stats">
            <span class="route-stat"><strong>${orderedRoute.length}</strong> zastávok</span>
            <span class="route-stat"><strong>${formatDist(totalDist)}</strong></span>
            <span class="route-stat">~ <strong>${formatTime(walkingMin)}</strong> pešo</span>
        </div>
        <a class="route-gmaps-btn" href="${gmapsUrl}" target="_blank" rel="noopener">
            🧭 Otvoriť trasu v Google Maps
        </a>
        <div class="route-stops">
            ${start ? `<div class="route-stop route-stop-start"><span class="route-stop-marker">🏁</span><span>${start.label || 'Štart'}</span></div>` : ''}
            ${stops.map(s => `
                <div class="route-stop">
                    <span class="route-stop-marker">${s.idx + 1}</span>
                    <span class="route-stop-name">${s.place.name}</span>
                    <span class="route-stop-dist">${start || s.idx > 0 ? '+ ' + formatDist(s.dist) : ''}</span>
                </div>
            `).join('')}
        </div>
    `;
}

function buildGoogleMapsUrl(start, route) {
    if (!route.length) return '#';
    const origin = start
        ? `${start.lat},${start.lon}`
        : `${route[0].coords.lat},${route[0].coords.lon}`;
    const routePoints = start ? route : route.slice(1);
    if (routePoints.length === 0) {
        return `https://www.google.com/maps/dir/?api=1&destination=${origin}&travelmode=walking`;
    }
    const destination = `${routePoints[routePoints.length - 1].coords.lat},${routePoints[routePoints.length - 1].coords.lon}`;
    const waypoints = routePoints.slice(0, -1)
        .slice(0, 9) // Google Maps limit ~9 waypoints
        .map(p => `${p.coords.lat},${p.coords.lon}`)
        .join('|');
    let url = `https://www.google.com/maps/dir/?api=1&origin=${origin}&destination=${destination}&travelmode=walking`;
    if (waypoints) url += `&waypoints=${encodeURIComponent(waypoints)}`;
    return url;
}

export function cleanupRoute() {
    if (map) {
        map.remove();
        map = null;
    }
    markers = [];
    routeLine = null;
    startMarker = null;
}
