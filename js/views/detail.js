import { PLACES } from '../data.js';
import * as audio from '../audio.js';

const TIERS = [
    { key: '30s', label: '30s', desc: 'Krátky' },
    { key: '1min', label: '1 min', desc: 'Stredný' },
    { key: '3min', label: '3 min', desc: 'Podrobný' }
];

const TIER_TEXT_MAP = { '30s': 'short', '1min': 'medium', '3min': 'long' };

let currentTier = '30s';
let currentLegendId = null;
let isPlaying = false;

export function renderDetail(container, placeId) {
    const place = PLACES.find(p => p.id === placeId);
    if (!place) {
        container.innerHTML = '<div class="loading">Miesto nenájdené</div>';
        return;
    }

    currentTier = '30s';
    currentLegendId = null;
    isPlaying = false;

    const legends = place.legends || [];
    const legendsSection = legends.length ? `
        <div class="legends-section">
            <h2 class="legends-title">Legendy a zaujímavosti</h2>
            <div class="legends-list">
                ${legends.map(l => `
                    <div class="legend-item" data-legend="${l.id}">
                        <div class="legend-play">&#9654;</div>
                        <div class="legend-title">${l.title}</div>
                    </div>
                `).join('')}
            </div>
        </div>
    ` : '';

    container.innerHTML = `
        <button class="detail-back" id="back-btn">&#8592;</button>
        <img class="detail-hero"
             src="${place.image}"
             alt="${place.name}"
             onerror="this.style.display='none';this.nextElementSibling.style.display='flex';">
        <div class="detail-hero-placeholder" style="display:none">${place.emoji}</div>
        <div class="detail-content">
            <h1>${place.name}</h1>
            <table class="info-table">
                ${Object.entries(place.info).map(([key, val]) => `
                    <tr><td>${key}</td><td>${val}</td></tr>
                `).join('')}
            </table>
            <div class="tier-selector">
                ${TIERS.map(t => `
                    <button class="tier-btn ${t.key === currentTier ? 'active' : ''}" data-tier="${t.key}">
                        ${t.label}<span>${t.desc}</span>
                    </button>
                `).join('')}
            </div>
            <div class="guide-text" id="guide-text">${place.texts.short}</div>
            ${legendsSection}
        </div>
        <div class="audio-bar">
            <div class="audio-progress" id="audio-progress">
                <div class="audio-progress-fill" id="audio-progress-fill" style="width:0%"></div>
            </div>
            <div class="audio-controls">
                <span class="audio-time" id="audio-time-current">0:00</span>
                <button class="audio-btn" id="btn-back10" title="Dozadu 10s">&#9194;</button>
                <button class="audio-btn audio-btn-play" id="btn-play">&#9654;</button>
                <button class="audio-btn" id="btn-fwd10" title="Dopredu 10s">&#9193;</button>
                <span class="audio-time" id="audio-time-total">0:00</span>
            </div>
        </div>
    `;

    document.getElementById('back-btn').addEventListener('click', () => {
        audio.stop();
        location.hash = '/';
    });

    container.querySelectorAll('.tier-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            currentTier = btn.dataset.tier;
            currentLegendId = null;
            container.querySelectorAll('.tier-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            container.querySelectorAll('.legend-item').forEach(li => li.classList.remove('active'));
            document.getElementById('guide-text').textContent = place.texts[TIER_TEXT_MAP[currentTier]];
            audio.play(place.id, currentTier);
            isPlaying = true;
            updatePlayButton();
        });
    });

    container.querySelectorAll('.legend-item').forEach(item => {
        item.addEventListener('click', () => {
            const legendId = item.dataset.legend;
            currentLegendId = legendId;
            container.querySelectorAll('.legend-item').forEach(li => li.classList.remove('active'));
            item.classList.add('active');
            container.querySelectorAll('.tier-btn').forEach(b => b.classList.remove('active'));
            audio.playLegend(place.id, legendId);
            isPlaying = true;
            updatePlayButton();
        });
    });

    document.getElementById('btn-play').addEventListener('click', () => {
        if (!isPlaying && !audio.getState().playing) {
            const state = audio.getState();
            const matchesMain = state.placeId === place.id && state.tier === currentTier && !currentLegendId;
            const matchesLegend = state.placeId === place.id && state.legendId === currentLegendId && currentLegendId;
            if (matchesMain || matchesLegend) {
                audio.toggle();
            } else if (currentLegendId) {
                audio.playLegend(place.id, currentLegendId);
            } else {
                audio.play(place.id, currentTier);
            }
            isPlaying = true;
        } else {
            audio.toggle();
            isPlaying = audio.getState().playing;
        }
        updatePlayButton();
    });

    document.getElementById('btn-back10').addEventListener('click', () => {
        audio.skip(-10);
    });

    document.getElementById('btn-fwd10').addEventListener('click', () => {
        audio.skip(10);
    });

    document.getElementById('audio-progress').addEventListener('click', (e) => {
        const rect = e.currentTarget.getBoundingClientRect();
        const fraction = (e.clientX - rect.left) / rect.width;
        audio.seekTo(Math.max(0, Math.min(1, fraction)));
    });

    audio.onTimeUpdate((state) => {
        const fill = document.getElementById('audio-progress-fill');
        const timeCurrent = document.getElementById('audio-time-current');
        const timeTotal = document.getElementById('audio-time-total');
        if (fill && state.duration > 0) {
            fill.style.width = `${(state.currentTime / state.duration) * 100}%`;
            timeCurrent.textContent = formatTime(state.currentTime);
            timeTotal.textContent = formatTime(state.duration);
        }
        isPlaying = state.playing;
        updatePlayButton();
    });

    audio.onEnded(() => {
        isPlaying = false;
        updatePlayButton();
        const fill = document.getElementById('audio-progress-fill');
        if (fill) fill.style.width = '100%';
    });

    setTimeout(() => {
        audio.play(place.id, '30s');
        isPlaying = true;
        updatePlayButton();
    }, 500);
}

function updatePlayButton() {
    const btn = document.getElementById('btn-play');
    if (btn) {
        btn.textContent = isPlaying ? '\u23F8' : '\u25B6';
    }
}

function formatTime(seconds) {
    const m = Math.floor(seconds / 60);
    const s = Math.floor(seconds % 60);
    return `${m}:${s.toString().padStart(2, '0')}`;
}
