const audioEl = new Audio();
let currentPlaceId = null;
let currentTier = null;
let currentLegendId = null;
let onUpdateCb = null;
let onEndedCb = null;
let usingSpeech = false;
let speechUtterance = null;

audioEl.addEventListener('timeupdate', () => {
    if (onUpdateCb) onUpdateCb(getState());
});

audioEl.addEventListener('ended', () => {
    if (onEndedCb) onEndedCb();
});

audioEl.addEventListener('error', () => {
    if (!usingSpeech && currentPlaceId && (currentTier || currentLegendId)) {
        playSpeechFallback();
    }
});

function getState() {
    if (usingSpeech) {
        return {
            playing: speechSynthesis.speaking && !speechSynthesis.paused,
            currentTime: 0,
            duration: 0,
            placeId: currentPlaceId,
            tier: currentTier,
            legendId: currentLegendId
        };
    }
    return {
        playing: !audioEl.paused,
        currentTime: audioEl.currentTime,
        duration: audioEl.duration || 0,
        placeId: currentPlaceId,
        tier: currentTier,
        legendId: currentLegendId
    };
}

function playSpeechFallback() {
    usingSpeech = true;
    const places = window.__PLACES_DATA || [];
    const place = places.find(p => p.id === currentPlaceId);
    if (!place) return;

    let text;
    if (currentLegendId) {
        const legend = (place.legends || []).find(l => l.id === currentLegendId);
        text = legend ? legend.text : '';
    } else {
        const tierKey = currentTier === '30s' ? 'short' : currentTier === '1min' ? 'medium' : 'long';
        text = place.texts[tierKey];
    }
    if (!text) return;

    speechSynthesis.cancel();
    speechUtterance = new SpeechSynthesisUtterance(text);
    speechUtterance.lang = 'sk-SK';
    speechUtterance.rate = 0.95;
    speechUtterance.onend = () => {
        if (onEndedCb) onEndedCb();
    };
    speechSynthesis.speak(speechUtterance);
    if (onUpdateCb) onUpdateCb(getState());
}

export function play(placeId, tier) {
    stop();
    currentPlaceId = placeId;
    currentTier = tier;
    currentLegendId = null;
    usingSpeech = false;

    const src = `audio/${placeId}-${tier}.mp3`;
    audioEl.src = src;
    audioEl.play().catch(() => {});
}

export function playLegend(placeId, legendId) {
    stop();
    currentPlaceId = placeId;
    currentTier = null;
    currentLegendId = legendId;
    usingSpeech = false;

    const src = `audio/${placeId}-legend-${legendId}.mp3`;
    audioEl.src = src;
    audioEl.play().catch(() => {});
}

export function stop() {
    audioEl.pause();
    audioEl.src = '';
    speechSynthesis.cancel();
    usingSpeech = false;
    currentPlaceId = null;
    currentTier = null;
    currentLegendId = null;
}

export function toggle() {
    if (usingSpeech) {
        if (speechSynthesis.paused) {
            speechSynthesis.resume();
        } else if (speechSynthesis.speaking) {
            speechSynthesis.pause();
        }
        if (onUpdateCb) onUpdateCb(getState());
        return;
    }
    if (audioEl.paused) {
        audioEl.play().catch(() => {});
    } else {
        audioEl.pause();
    }
}

export function skip(seconds) {
    if (usingSpeech) return;
    audioEl.currentTime = Math.max(0, Math.min(audioEl.duration || 0, audioEl.currentTime + seconds));
}

export function seekTo(fraction) {
    if (usingSpeech) return;
    audioEl.currentTime = (audioEl.duration || 0) * fraction;
}

export function onTimeUpdate(cb) {
    onUpdateCb = cb;
}

export function onEnded(cb) {
    onEndedCb = cb;
}

export { getState };
