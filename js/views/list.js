import { PLACES } from '../data.js';

let currentFilter = 'all';

export function renderList(container) {
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

    // Filter buttons
    container.querySelectorAll('.filter-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            currentFilter = btn.dataset.filter;
            renderList(container);
        });
    });

    // Card clicks
    container.querySelectorAll('.card').forEach(card => {
        card.addEventListener('click', () => {
            location.hash = `/miesto/${card.dataset.id}`;
        });
    });
}

function getFilteredPlaces() {
    if (currentFilter === 'all') return PLACES;
    return PLACES.filter(p => p.category === currentFilter);
}
