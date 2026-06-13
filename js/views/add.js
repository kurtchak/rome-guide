import {
    DESTINATIONS,
    CATEGORY_LABELS,
    getActiveDestination,
    setActiveDestination,
    addCustomPlace,
} from '../data.js';

// Formulár na pridanie vlastného miesta. Uloží sa do localStorage
// a hneď sa zobrazí v zozname, na mape aj v trase.
export function renderAdd(container) {
    const active = getActiveDestination();

    const categoryOptions = (destId) => {
        const dest = DESTINATIONS.find(d => d.id === destId) || DESTINATIONS[0];
        return dest.categories
            .map(c => `<option value="${c}">${CATEGORY_LABELS[c] || c}</option>`)
            .join('');
    };

    container.innerHTML = `
        <button class="detail-back" id="back-btn">&#8592;</button>
        <div class="add-form">
            <h1>Pridať miesto</h1>
            <p class="add-hint">Vlastné miesto sa uloží do tohto zariadenia a zobrazí sa v zozname, na mape aj v trase.</p>

            <label class="add-label">Názov *
                <input type="text" id="f-name" class="add-input" placeholder="napr. Naša obľúbená vyhliadka" maxlength="80">
            </label>

            <label class="add-label">Destinácia
                <select id="f-dest" class="add-input">
                    ${DESTINATIONS.map(d => `<option value="${d.id}" ${d.id === active.id ? 'selected' : ''}>${d.emoji} ${d.name}</option>`).join('')}
                </select>
            </label>

            <label class="add-label">Kategória
                <select id="f-cat" class="add-input">${categoryOptions(active.id)}</select>
            </label>

            <label class="add-label">Emoji (ikona)
                <input type="text" id="f-emoji" class="add-input" placeholder="📍" maxlength="4">
            </label>

            <div class="add-coords">
                <label class="add-label add-label-half">Zem. šírka (lat)
                    <input type="number" id="f-lat" class="add-input" step="any" placeholder="napr. 60.39">
                </label>
                <label class="add-label add-label-half">Zem. dĺžka (lon)
                    <input type="number" id="f-lon" class="add-input" step="any" placeholder="napr. 5.32">
                </label>
            </div>
            <button type="button" class="add-locate-btn" id="f-locate">📍 Použiť moju polohu</button>

            <label class="add-label">Popis (nepovinné)
                <textarea id="f-desc" class="add-input add-textarea" rows="4" placeholder="Pár viet o mieste — prečítajú sa v audiosprievodcovi."></textarea>
            </label>

            <div class="add-error" id="f-error"></div>

            <div class="add-actions">
                <button type="button" class="add-cancel" id="f-cancel">Zrušiť</button>
                <button type="button" class="add-save" id="f-save">Uložiť miesto</button>
            </div>
        </div>
    `;

    const $ = id => container.querySelector(id);

    $('#back-btn').addEventListener('click', () => { location.hash = '/'; });
    $('#f-cancel').addEventListener('click', () => { location.hash = '/'; });

    // Kategórie sa menia podľa zvolenej destinácie
    $('#f-dest').addEventListener('change', (e) => {
        $('#f-cat').innerHTML = categoryOptions(e.target.value);
    });

    $('#f-locate').addEventListener('click', () => {
        if (!navigator.geolocation) {
            $('#f-error').textContent = 'Geolokácia nie je dostupná.';
            return;
        }
        $('#f-locate').textContent = '⏳ Zisťujem polohu…';
        navigator.geolocation.getCurrentPosition(
            (pos) => {
                $('#f-lat').value = pos.coords.latitude.toFixed(5);
                $('#f-lon').value = pos.coords.longitude.toFixed(5);
                $('#f-locate').textContent = '📍 Použiť moju polohu';
            },
            () => {
                $('#f-error').textContent = 'Polohu sa nepodarilo zistiť.';
                $('#f-locate').textContent = '📍 Použiť moju polohu';
            },
            { enableHighAccuracy: true, timeout: 8000 }
        );
    });

    $('#f-save').addEventListener('click', () => {
        const name = $('#f-name').value.trim();
        if (!name) {
            $('#f-error').textContent = 'Zadaj aspoň názov miesta.';
            $('#f-name').focus();
            return;
        }

        const latRaw = $('#f-lat').value.trim();
        const lonRaw = $('#f-lon').value.trim();
        let coords = null;
        if (latRaw !== '' || lonRaw !== '') {
            const lat = parseFloat(latRaw);
            const lon = parseFloat(lonRaw);
            if (!Number.isFinite(lat) || !Number.isFinite(lon) ||
                lat < -90 || lat > 90 || lon < -180 || lon > 180) {
                $('#f-error').textContent = 'Súradnice nie sú platné (lat −90…90, lon −180…180). Nechaj ich prázdne, ak ich nepoznáš.';
                return;
            }
            coords = { lat, lon };
        }

        const destId = $('#f-dest').value;
        const place = addCustomPlace({
            name,
            category: $('#f-cat').value,
            coords,
            emoji: $('#f-emoji').value.trim(),
            short: $('#f-desc').value.trim(),
        });

        // Prepni na destináciu miesta, nech je hneď viditeľné
        setActiveDestination(destId);
        location.hash = `/miesto/${place.id}`;
    });
}
