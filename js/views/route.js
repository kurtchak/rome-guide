import { PLACES, HOME } from '../data.js';

const ROME_CENTER = [41.902, 12.480];
const WALK_MIN_PER_KM = 12; // pešo ~5 km/h
const DEFAULT_VISIT_MIN = 45; // typický čas na jednom mieste

let map = null;
let markers = [];
let routeLine = null;
let startMarker = null;
let selectedIds = new Set();
let startMode = 'gps';
let startCoords = null;
let gpsPosition = null;
let startTimeStr = null; // "HH:MM" alebo null = teraz
let visitTimes = {}; // {placeId: "HH:MM"}

function haversine(a, b) {
    const R = 6371000;
    const dLat = (b.lat - a.lat) * Math.PI / 180;
    const dLon = (b.lon - a.lon) * Math.PI / 180;
    const x = Math.sin(dLat / 2) ** 2 +
        Math.cos(a.lat * Math.PI / 180) * Math.cos(b.lat * Math.PI / 180) *
        Math.sin(dLon / 2) ** 2;
    return R * 2 * Math.atan2(Math.sqrt(x), Math.sqrt(1 - x));
}

function timeToMin(str) {
    if (!str) return null;
    const [h, m] = str.split(':').map(Number);
    return h * 60 + m;
}

function minToTime(min) {
    min = ((min % (24 * 60)) + 24 * 60) % (24 * 60);
    const h = Math.floor(min / 60);
    const m = Math.round(min % 60);
    return `${h.toString().padStart(2, '0')}:${m.toString().padStart(2, '0')}`;
}

function nowMin() {
    const d = new Date();
    return d.getHours() * 60 + d.getMinutes();
}

function getStartTimeMin() {
    return startTimeStr ? timeToMin(startTimeStr) : nowMin();
}

// Nearest-neighbor v rámci segmentu
function nearestNeighbor(start, places) {
    const remaining = [...places];
    const route = [];
    let cur = start;
    while (remaining.length) {
        let bi = 0, bd = Infinity;
        for (let i = 0; i < remaining.length; i++) {
            const d = haversine(cur, remaining[i].coords);
            if (d < bd) { bd = d; bi = i; }
        }
        route.push(remaining[bi]);
        cur = remaining[bi].coords;
        remaining.splice(bi, 1);
    }
    return route;
}

// Plán trasy s ukotvenými časmi
// Anchored miesta sa držia v poradí podľa času; flex sa vkladá podľa minimálnej obchádzky
function planRoute(start, places) {
    const anchored = places.filter(p => visitTimes[p.id]);
    const flex = places.filter(p => !visitTimes[p.id]);
    anchored.sort((a, b) => timeToMin(visitTimes[a.id]) - timeToMin(visitTimes[b.id]));

    if (anchored.length === 0) {
        return nearestNeighbor(start, flex);
    }

    // Segmenty: [start → A1], [A1 → A2], ..., [An → ∞]
    const segments = [];
    let prev = start;
    for (const a of anchored) {
        segments.push({ from: prev, to: a.coords, flex: [] });
        prev = a.coords;
    }
    segments.push({ from: prev, to: null, flex: [] });

    // Priradenie flex k segmentu s najmenšou obchádzkou
    for (const f of flex) {
        let bestIdx = 0, bestDetour = Infinity;
        for (let i = 0; i < segments.length; i++) {
            const s = segments[i];
            const direct = s.to ? haversine(s.from, s.to) : 0;
            const via = haversine(s.from, f.coords) + (s.to ? haversine(f.coords, s.to) : 0);
            const detour = via - direct;
            if (detour < bestDetour) { bestDetour = detour; bestIdx = i; }
        }
        segments[bestIdx].flex.push(f);
    }

    // Zostrojenie finálneho poradia
    const route = [];
    for (let i = 0; i < segments.length; i++) {
        const s = segments[i];
        const ordered = nearestNeighbor(s.from, s.flex);
        route.push(...ordered);
        if (i < anchored.length) route.push(anchored[i]);
    }
    return route;
}

// Vypočíta odhadované časy príchodu a odchodu pre každú zastávku
function computeTimes(start, route, startMin) {
    const stops = [];
    let t = startMin;
    let prev = start;
    for (const p of route) {
        const distM = haversine(prev, p.coords);
        const walkMin = (distM / 1000) * WALK_MIN_PER_KM;
        let arrival = t + walkMin;
        const anchorStr = visitTimes[p.id];
        let lateMin = 0;
        if (anchorStr) {
            const anchorMin = timeToMin(anchorStr);
            if (arrival > anchorMin + 0.5) {
                lateMin = arrival - anchorMin; // neskoro
            }
            // Ak prídeme skôr, počkáme na daný čas
            arrival = Math.max(arrival, anchorMin);
        }
        const departure = arrival + DEFAULT_VISIT_MIN;
        stops.push({ place: p, distM, walkMin, arrival, departure, lateMin, anchor: anchorStr });
        t = departure;
        prev = p.coords;
    }
    return stops;
}

function formatDist(m) {
    if (m < 1000) return `${Math.round(m)} m`;
    return `${(m / 1000).toFixed(1)} km`;
}

function formatDur(min) {
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
            <div class="route-row">
                <label class="route-label">Od:</label>
                <input type="time" id="start-time" class="route-select" value="${startTimeStr || ''}" placeholder="teraz">
                <button class="route-chip route-chip-clear" id="start-time-now" type="button">Teraz</button>
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
            <div class="route-hint">Pri miestach s rezerváciou môžeš nastaviť čas vstupu 🕐 — trasa sa prispôsobí.</div>
            <div id="route-places"></div>
        </div>
    `;

    document.getElementById('start-select').value = startMode;
    document.getElementById('start-select').addEventListener('change', (e) => {
        startMode = e.target.value;
        document.getElementById('start-place-picker').style.display = startMode === 'place' ? 'flex' : 'none';
        if (startMode !== 'place') startCoords = null;
        refreshAll();
    });

    document.getElementById('start-place-select').addEventListener('change', (e) => {
        const placeId = e.target.value;
        const place = PLACES.find(p => p.id === placeId);
        startCoords = place?.coords ? { ...place.coords, label: place.name } : null;
        refreshAll();
    });

    document.getElementById('start-time').addEventListener('change', (e) => {
        startTimeStr = e.target.value || null;
        refreshAll();
    });

    document.getElementById('start-time-now').addEventListener('click', () => {
        startTimeStr = null;
        document.getElementById('start-time').value = '';
        refreshAll();
    });

    container.querySelectorAll('.route-chip[data-action]').forEach(btn => {
        btn.addEventListener('click', () => handleChip(btn.dataset.action));
    });

    initMap();
    refreshPlacesList();
    refreshRoute();

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
        visitTimes = {};
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
        <div class="route-item ${selectedIds.has(place.id) ? 'selected' : ''}" data-id="${place.id}">
            <label class="route-item-main">
                <input type="checkbox" ${selectedIds.has(place.id) ? 'checked' : ''}>
                <span class="route-item-emoji">${place.emoji}</span>
                <span class="route-item-name">${place.name}</span>
                <span class="route-item-cat">${place.category === 'vatikan' ? 'Vatikán' : 'Rím'}</span>
            </label>
            ${selectedIds.has(place.id) ? `
                <div class="route-item-time">
                    <span class="route-item-time-icon">🕐</span>
                    <input type="time" class="route-item-time-input" data-place="${place.id}" value="${visitTimes[place.id] || ''}" placeholder="Vstup o">
                    ${visitTimes[place.id] ? `<button class="route-item-time-clear" data-place="${place.id}" type="button" title="Zrušiť čas">✕</button>` : ''}
                </div>
            ` : ''}
        </div>
    `).join('');

    container.querySelectorAll('.route-item input[type=checkbox]').forEach(input => {
        input.addEventListener('change', (e) => {
            const id = e.target.closest('.route-item').dataset.id;
            if (e.target.checked) {
                selectedIds.add(id);
            } else {
                selectedIds.delete(id);
                delete visitTimes[id];
            }
            refreshAll();
        });
    });

    container.querySelectorAll('.route-item-time-input').forEach(input => {
        input.addEventListener('change', (e) => {
            const id = e.target.dataset.place;
            if (e.target.value) visitTimes[id] = e.target.value;
            else delete visitTimes[id];
            refreshAll();
        });
    });

    container.querySelectorAll('.route-item-time-clear').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            const id = btn.dataset.place;
            delete visitTimes[id];
            refreshAll();
        });
    });
}

function refreshRoute() {
    if (!map) return;

    markers.forEach(m => m.remove());
    markers = [];
    if (routeLine) { routeLine.remove(); routeLine = null; }
    if (startMarker) { startMarker.remove(); startMarker = null; }

    const start = getStartCoords();
    const selected = PLACES.filter(p => selectedIds.has(p.id) && p.coords);
    const summary = document.getElementById('route-summary');

    if (!start && selected.length === 0) {
        summary.innerHTML = '<div class="route-summary-hint">Čaká sa na polohu… a výber miest.</div>';
        return;
    }
    if (!start) {
        summary.innerHTML = '<div class="route-summary-hint">Čaká sa na polohu…</div>';
        return;
    }
    if (selected.length === 0) {
        summary.innerHTML = '<div class="route-summary-hint">Vyber miesta, ktoré chceš navštíviť.</div>';
        return;
    }

    const orderedRoute = planRoute(start, selected);
    const stops = computeTimes(start, orderedRoute, getStartTimeMin());

    // Start marker
    const startIcon = L.divIcon({
        html: `<div class="route-pin route-pin-start">🏁</div>`,
        className: 'map-pin-wrapper',
        iconSize: [36, 36], iconAnchor: [18, 18],
    });
    startMarker = L.marker([start.lat, start.lon], { icon: startIcon }).addTo(map);
    startMarker.bindPopup(`<strong>Štart:</strong> ${start.label || ''}<br>${minToTime(getStartTimeMin())}`);

    const latlngs = [[start.lat, start.lon]];
    orderedRoute.forEach((place, idx) => {
        const stop = stops[idx];
        const isAnchored = !!visitTimes[place.id];
        const isLate = stop.lateMin > 1;
        const cls = isAnchored ? (isLate ? 'route-pin-late' : 'route-pin-anchor') : 'route-pin-num';
        const icon = L.divIcon({
            html: `<div class="route-pin ${cls}">${idx + 1}</div>`,
            className: 'map-pin-wrapper',
            iconSize: [36, 36], iconAnchor: [18, 18],
        });
        const marker = L.marker([place.coords.lat, place.coords.lon], { icon }).addTo(map);
        marker.bindPopup(`<strong>${idx + 1}. ${place.name}</strong><br>Príchod: ${minToTime(stop.arrival)}${isAnchored ? ` (rezervácia ${visitTimes[place.id]})` : ''}`);
        markers.push(marker);
        latlngs.push([place.coords.lat, place.coords.lon]);
    });

    if (latlngs.length >= 2) {
        routeLine = L.polyline(latlngs, {
            color: '#e94560', weight: 4, opacity: 0.75, dashArray: '8 6',
        }).addTo(map);
    }
    if (latlngs.length) {
        map.fitBounds(latlngs, { padding: [40, 40], maxZoom: 15 });
    }

    const totalDist = stops.reduce((s, x) => s + x.distM, 0);
    const walkingMin = (totalDist / 1000) * WALK_MIN_PER_KM;
    const lastStop = stops[stops.length - 1];
    const totalEndMin = lastStop.departure;

    const gmapsUrl = buildGoogleMapsUrl(start, orderedRoute);
    const hasLate = stops.some(s => s.lateMin > 1);

    summary.innerHTML = `
        <div class="route-summary-stats">
            <span class="route-stat"><strong>${orderedRoute.length}</strong> zastávok</span>
            <span class="route-stat"><strong>${formatDist(totalDist)}</strong></span>
            <span class="route-stat">chôdza <strong>${formatDur(walkingMin)}</strong></span>
            <span class="route-stat">koniec <strong>${minToTime(totalEndMin)}</strong></span>
        </div>
        ${hasLate ? '<div class="route-warning">⚠️ Niektoré rezervované časy nestíhaš — uprav výber alebo štart.</div>' : ''}
        <a class="route-gmaps-btn" href="${gmapsUrl}" target="_blank" rel="noopener">
            🧭 Otvoriť trasu v Google Maps
        </a>
        <div class="route-stops">
            <div class="route-stop route-stop-start">
                <span class="route-stop-time">${minToTime(getStartTimeMin())}</span>
                <span class="route-stop-marker">🏁</span>
                <span class="route-stop-name">${start.label || 'Štart'}</span>
            </div>
            ${stops.map(s => `
                <div class="route-stop ${s.anchor ? (s.lateMin > 1 ? 'route-stop-late' : 'route-stop-anchor') : ''}">
                    <span class="route-stop-time">${minToTime(s.arrival)}${s.anchor ? ' 🎫' : ''}</span>
                    <span class="route-stop-marker">${s.place === orderedRoute[orderedRoute.length-1] ? orderedRoute.length : orderedRoute.indexOf(s.place) + 1}</span>
                    <span class="route-stop-name">${s.place.name}${s.lateMin > 1 ? ` <em>(−${Math.round(s.lateMin)} min)</em>` : ''}</span>
                    <span class="route-stop-dist">+${formatDist(s.distM)}</span>
                </div>
            `).join('')}
        </div>
    `;
}

function buildGoogleMapsUrl(start, route) {
    if (!route.length) return '#';
    const origin = `${start.lat},${start.lon}`;
    const destination = `${route[route.length - 1].coords.lat},${route[route.length - 1].coords.lon}`;
    const waypoints = route.slice(0, -1).slice(0, 9)
        .map(p => `${p.coords.lat},${p.coords.lon}`)
        .join('|');
    let url = `https://www.google.com/maps/dir/?api=1&origin=${origin}&destination=${destination}&travelmode=walking`;
    if (waypoints) url += `&waypoints=${encodeURIComponent(waypoints)}`;
    return url;
}

export function cleanupRoute() {
    if (map) { map.remove(); map = null; }
    markers = [];
    routeLine = null;
    startMarker = null;
}
