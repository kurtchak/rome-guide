import { PLACES } from './data.js';

const PROXIMITY_RADIUS = 200; // metrov
const COOLDOWN = 10 * 60 * 1000; // 10 minút medzi notifikáciami pre to isté miesto
const CHECK_INTERVAL = 15000; // kontrola každých 15 sekúnd

let watchId = null;
let notifiedPlaces = {}; // { placeId: timestamp }
let toastContainer = null;
let permissionGranted = false;

function getDistance(lat1, lon1, lat2, lon2) {
    const R = 6371000;
    const dLat = (lat2 - lat1) * Math.PI / 180;
    const dLon = (lon2 - lon1) * Math.PI / 180;
    const a = Math.sin(dLat / 2) ** 2 +
        Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *
        Math.sin(dLon / 2) ** 2;
    return R * 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
}

function ensureToastContainer() {
    if (toastContainer) return toastContainer;
    toastContainer = document.createElement('div');
    toastContainer.className = 'toast-container';
    document.body.appendChild(toastContainer);
    return toastContainer;
}

function showToast(place, distance) {
    const container = ensureToastContainer();
    const distText = distance < 100 ? 'menej ako 100 m' : `${Math.round(distance)} m`;

    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.innerHTML = `
        <div class="toast-icon">${place.emoji}</div>
        <div class="toast-body">
            <div class="toast-title">${place.name}</div>
            <div class="toast-dist">${distText} od vás</div>
        </div>
        <div class="toast-action">Otvoriť</div>
    `;

    toast.addEventListener('click', () => {
        location.hash = `/miesto/${place.id}`;
        toast.classList.add('toast-hide');
        setTimeout(() => toast.remove(), 300);
    });

    container.appendChild(toast);
    requestAnimationFrame(() => toast.classList.add('toast-show'));

    setTimeout(() => {
        toast.classList.add('toast-hide');
        setTimeout(() => toast.remove(), 300);
    }, 8000);
}

async function sendBrowserNotification(place, distance) {
    if (!('Notification' in window) || Notification.permission !== 'granted') return;

    const distText = distance < 100 ? 'menej ako 100 m' : `${Math.round(distance)} m`;
    const reg = await navigator.serviceWorker?.ready;

    if (reg) {
        reg.showNotification(place.name, {
            body: `Ste ${distText} od ${place.name}. Ťuknite pre audio sprievodcu.`,
            icon: 'img/icons/icon-192.png',
            badge: 'img/icons/icon-192.png',
            tag: `proximity-${place.id}`,
            data: { placeId: place.id },
            vibrate: [200, 100, 200],
        });
    } else {
        new Notification(place.name, {
            body: `Ste ${distText} od ${place.name}. Ťuknite pre audio sprievodcu.`,
            icon: 'img/icons/icon-192.png',
            tag: `proximity-${place.id}`,
        });
    }
}

function checkProximity(position) {
    const { latitude, longitude } = position.coords;
    const now = Date.now();

    for (const place of PLACES) {
        if (!place.coords) continue;
        const dist = getDistance(latitude, longitude, place.coords.lat, place.coords.lon);

        if (dist <= PROXIMITY_RADIUS) {
            const lastNotified = notifiedPlaces[place.id] || 0;
            if (now - lastNotified > COOLDOWN) {
                notifiedPlaces[place.id] = now;
                showToast(place, dist);
                if (document.hidden) {
                    sendBrowserNotification(place, dist);
                }
            }
        }
    }
}

async function requestNotificationPermission() {
    if (!('Notification' in window)) return false;
    if (Notification.permission === 'granted') return true;
    if (Notification.permission === 'denied') return false;
    const result = await Notification.requestPermission();
    return result === 'granted';
}

export async function startTracking() {
    if (!('geolocation' in navigator)) return;
    if (watchId !== null) return;

    permissionGranted = await requestNotificationPermission();

    watchId = navigator.geolocation.watchPosition(
        checkProximity,
        (err) => {
            if (err.code === err.PERMISSION_DENIED) {
                console.log('Geolokácia zamietnutá');
            }
        },
        {
            enableHighAccuracy: true,
            maximumAge: CHECK_INTERVAL,
            timeout: 30000,
        }
    );
}

export function stopTracking() {
    if (watchId !== null) {
        navigator.geolocation.clearWatch(watchId);
        watchId = null;
    }
}

export function isTracking() {
    return watchId !== null;
}
