# Audiosprievodca — Rím a Nórsko

Offline-first **PWA audiosprievodca** v slovenčine. Pôvodne sprievodca po Ríme a Vatikáne,
dnes **viacmestný** — popri Ríme obsahuje aj západné Nórsko (Bergen, Stavanger, fjordy).

Aplikácia je čisté **vanilla JS** (žiadny framework), s offline cachovaním cez `sw.js`
a inštaláciou na plochu cez `manifest.json`. Pre každé miesto ponúka text v troch dĺžkach
(30 s / 1 min / 3 min), legendy a zaujímavosti, predgenerované MP3 (alebo `speechSynthesis`
fallback), mapu, plánovač trasy a tipy na kávu/jedlo v okolí.

## Štruktúra

```
index.html            – shell, načítava ES moduly
manifest.json, sw.js  – PWA (inštalácia + offline cache)
css/style.css         – téma #1a1a2e / #e94560
js/
  data.js             – PLACES, DESTINATIONS, CATEGORY_LABELS + helpery destinácií
  food.js             – kaviarne/podniky (pole `destination`)
  audio.js            – prehrávač MP3 + fallback na speechSynthesis
  proximity.js        – notifikácie pri priblížení k miestu
  app.js              – hash router
  views/
    list.js           – zoznam + prepínač destinácií + filtre kategórií
    detail.js         – detail miesta, audio, legendy, jedlo v okolí
    map.js            – Leaflet mapa (markery aktívnej destinácie)
    route.js          – plánovač trasy s časmi vstupu
    add.js            – formulár na pridanie vlastného miesta
audio/                – predgenerované MP3 (`<id>-30s.mp3`, …, `<id>-legend-<lid>.mp3`)
img/places/           – obrázky miest (`<id>.jpg`)
scripts/              – Python nástroje (obsah, obrázky, audio)
```

## Destinácie

Destinácia zoskupuje niekoľko kategórií miest. Definované sú v `js/data.js`:

```js
const DESTINATIONS = [
  { id: "rome",   name: "Rím a Vatikán",  emoji: "🇮🇹", categories: ["vatikan","rim"], … },
  { id: "norway", name: "Nórsko — fjordy", emoji: "🇳🇴", categories: ["bergen","stavanger","fjordy"], … },
];
```

Aktívna destinácia sa drží v `localStorage` (`activeDestination`, default `"rome"`).
Prepína sa tlačidlami v zozname; všetky zobrazenia (zoznam, mapa, trasa, detail, jedlo)
sa filtrujú podľa `getActiveDestination()`.

## Pridanie miesta / mesta

1. **Obsah** priprav v Python súbore v `scripts/` v rovnakom formáte ako
   `scripts/norway_places_data.py` (dict s `id, name, category, coords (tuple), emoji,
   info, texts{short,medium,long}, legends[]`).
2. Ak ide o **novú destináciu/kategóriu**, doplň ju do `DESTINATIONS` a `CATEGORY_LABELS`
   v `js/data.js` a pridaj farbu pinu do `css/style.css` (`.map-pin-<kategória>`).
3. **Injektni** miesta do `data.js`:
   ```bash
   python3 scripts/inject_norway.py      # nórske miesta
   python3 scripts/inject_new_places.py  # rímske miesta
   ```
   Skript vkladá pred uzatváracie `];` poľa `PLACES` a preskakuje existujúce `id`.
   `long` a `legends` možno dopĺňať aj z modulov `scripts/_fills_*.py`
   (dict `FILLS = { id: {"long": …, "legends": […]} }`) — užitočné pri paralelnom písaní.
4. **Obrázky**: doplň `IMAGES` v `scripts/download_images.py` (názvy súborov z Wikimedia
   Commons — over, že existujú) a spusti `python3 scripts/download_images.py`.
5. **Audio**: `python3 scripts/generate_audio.py` (hlas `sk-SK-LukasNeural`, vyžaduje sieť;
   generuje len chýbajúce MP3). Nórske názvy číta slovenský hlas v origináli.
6. **PWA**: zvýš `CACHE_NAME` v `sw.js`, ak treba uprav `name`/`description` v `manifest.json`.

### Pridanie miesta priamo v appke

Bez úpravy kódu sa dá miesto pridať aj z mobilu: v zozname tlačidlo
**„➕ Pridať vlastné miesto"** (alebo `#/pridat`). Vyplní sa názov, destinácia,
kategória, emoji, voliteľné súradnice (alebo „Použiť moju polohu") a popis.
Miesto sa uloží do `localStorage` (kľúč `customPlaces`), hneď sa zobrazí v zozname,
na mape aj v trase a v detaile sa dá zmazať. Audio sa pri vlastných miestach číta
cez `speechSynthesis` (žiadne MP3 netreba).

## Lokálne spustenie

```bash
python3 server.py     # alebo: python3 -m http.server 8000
```

Otvor `http://localhost:8000`. Na mobile: otvoriť hosted URL → „Pridať na plochu" →
beží ako standalone appka, offline (po prvom načítaní sa assety, obrázky aj audio cachujú).

## Závislosti skriptov

`scripts/requirements.txt` (`edge-tts`, `requests`, `Pillow`). Mapové dlaždice (OpenStreetMap)
a Leaflet sa načítavajú z CDN; offline funguje appka aj bez mapy (fallback hláška).
