import { PLACES, HOME } from '../data.js';

const ROME_CENTER = [41.902, 12.480];
const DEFAULT_ZOOM = 14;

let map = null;
let userMarker = null;

export function renderMap(container) {
    container.innerHTML = `
        <button class="detail-back" id="back-btn">&#8592;</button>
        <div id="map" class="map-container"></div>
        <button class="map-locate" id="locate-btn" title="Moja poloha">📍</button>
    `;

    if (typeof L === 'undefined') {
        container.innerHTML = '<div class="loading">Mapa nie je dostupná (offline?)</div>';
        return;
    }

    map = L.map('map', {
        zoomControl: true,
        attributionControl: true,
    }).setView(ROME_CENTER, DEFAULT_ZOOM);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap',
    }).addTo(map);

    const bounds = [];
    for (const place of PLACES) {
        if (!place.coords) continue;
        const icon = L.divIcon({
            html: `<div class="map-pin map-pin-${place.category}"><span>${place.emoji}</span></div>`,
            className: 'map-pin-wrapper',
            iconSize: [40, 48],
            iconAnchor: [20, 46],
            popupAnchor: [0, -42],
        });

        const marker = L.marker([place.coords.lat, place.coords.lon], { icon }).addTo(map);

        const popupHtml = `
            <div class="map-popup">
                <img src="${place.image}"
                     alt="${place.name}"
                     onerror="this.style.display='none'">
                <div class="map-popup-body">
                    <div class="map-popup-title">${place.name}</div>
                    <div class="map-popup-cat">${place.category === 'vatikan' ? 'Vatikán' : 'Rím'}</div>
                    <a href="#/miesto/${place.id}" class="map-popup-btn">Otvoriť sprievodcu</a>
                </div>
            </div>
        `;
        marker.bindPopup(popupHtml, { maxWidth: 240 });
        bounds.push([place.coords.lat, place.coords.lon]);
    }

    // Airbnb pin
    if (HOME?.coords) {
        const homeIcon = L.divIcon({
            html: `<div class="map-pin map-pin-home"><span>${HOME.emoji}</span></div>`,
            className: 'map-pin-wrapper',
            iconSize: [44, 52],
            iconAnchor: [22, 50],
            popupAnchor: [0, -46],
        });
        const homeMarker = L.marker([HOME.coords.lat, HOME.coords.lon], { icon: homeIcon }).addTo(map);
        homeMarker.bindPopup(`
            <div class="map-popup">
                <div class="map-popup-body">
                    <div class="map-popup-title">${HOME.name}</div>
                    <div class="map-popup-cat">${HOME.address}</div>
                    <a href="https://www.google.com/maps/dir/?api=1&destination=${HOME.coords.lat},${HOME.coords.lon}&travelmode=walking"
                       target="_blank" rel="noopener" class="map-popup-btn">🧭 Navigovať</a>
                </div>
            </div>
        `, { maxWidth: 240 });
        bounds.push([HOME.coords.lat, HOME.coords.lon]);
    }

    if (bounds.length > 1) {
        map.fitBounds(bounds, { padding: [50, 50] });
    }

    document.getElementById('back-btn').addEventListener('click', () => {
        location.hash = '/';
    });

    document.getElementById('locate-btn').addEventListener('click', locateUser);

    // Try auto-locate silently
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (pos) => showUserLocation([pos.coords.latitude, pos.coords.longitude], false),
            () => {},
            { enableHighAccuracy: true, timeout: 5000, maximumAge: 60000 }
        );
    }
}

function locateUser() {
    if (!navigator.geolocation) return;
    navigator.geolocation.getCurrentPosition(
        (pos) => showUserLocation([pos.coords.latitude, pos.coords.longitude], true),
        (err) => console.log('Geo error:', err.message),
        { enableHighAccuracy: true, timeout: 10000 }
    );
}

function showUserLocation(latlng, centerOn) {
    if (!map) return;
    if (userMarker) {
        userMarker.setLatLng(latlng);
    } else {
        userMarker = L.circleMarker(latlng, {
            radius: 9,
            color: '#ffffff',
            weight: 3,
            fillColor: '#4dabf7',
            fillOpacity: 1,
        }).addTo(map);
        userMarker.bindPopup('Vaša poloha');
    }
    if (centerOn) {
        map.setView(latlng, 16);
    }
}

export function cleanupMap() {
    if (map) {
        map.remove();
        map = null;
        userMarker = null;
    }
}
