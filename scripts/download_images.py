#!/usr/bin/env python3
"""Stiahnutie obrázkov z Wikimedia Commons a generovanie PWA ikon."""

import os
import sys
import time
from urllib.parse import unquote

import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

# Wikimedia vyžaduje popisný User-Agent s kontaktom — bez neho server
# výrazne agresívnejšie rate-limituje (HTTP 429), najmä z cloud/CI IP adries.
HEADERS = {
    "User-Agent": (
        "RomeGuideBot/1.0 "
        "(https://github.com/kurtchak/rome-guide; kurtcha@gmail.com) "
        "Python-requests"
    )
}

IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "img", "places")
ICON_DIR = os.path.join(os.path.dirname(__file__), "..", "img", "icons")
MAX_WIDTH = 800

# Mapovanie place ID -> Wikimedia Commons filename
# Vybrané public domain / CC obrázky
IMAGES = {
    "bazilika-sv-petra": "Basilica_di_San_Pietro_in_Vaticano_September_2015-1a.jpg",
    "sikstinska-kaplnka": "Sistine_Chapel_ceiling_02_(brightened).jpg",
    "vatikanske-muzea": "Vatican_Museums_Spiral_Staircase_2012.jpg",
    "pieta": "Michelangelo's_Pieta_5450_cropncleaned_edit.jpg",
    "namestie-sv-petra": "St_Peter's_Square,_Vatican_City_-_April_2007.jpg",
    "rafaelove-izby": "Raphael_School_of_Athens.jpg",
    "laokoon": "Laocoon_Pio-Clementino_Inv1059-1064-1067.jpg",
    "koloseum": "Colosseum_in_Rome,_Italy_-_April_2007.jpg",
    "panteon": "Pantheon_Rom_1.jpg",
    "fontana-di-trevi": "Trevi_Fountain,_Rome,_Italy_2_-_May_2007.jpg",
    "spanielske-schody": "Piazza_di_Spagna_(Rome)_0004.jpg",
    "rimske-forum": "Forum_Romanum_panorama_2.jpg",
    "anjelsky-hrad": "Castel_Sant'_Angelo_Between_Leaves.jpg",
    "piazza-navona": "Piazza_Navona,_Roma_-_fontana_fc07.jpg",
    "piazza-venezia": "Vittoriano_Altare_della_Patria_2013-09-16.jpg",
    "bocca-della-verita": "Età_imperiale,_chiusino_a_forma_di_mascherone_di_divinità_fluviale,_detta_bocca_della_verità,_collocata_qui_nel_1632.jpg",
    "campo-de-fiori": "Campo_dei_Fiori.jpg",
    # Nové miesta
    "san-giovanni-laterano": "San_Giovanni_in_Laterano_2021.jpg",
    "santa-maria-maggiore": "Santa_Maria_Maggiore_Front.JPG",
    "san-pietro-in-vincoli": "Moses_San_Pietro_in_Vincoli.jpg",
    "palatin": "Palatine_Hill_Rome.jpg",
    "galeria-borghese": "Galleria_borghese_facade.jpg",
    "kapitolske-muzea": "Piazza_del_Campidoglio.jpg",
    "trastevere": "Santa_Maria_in_Trastevere.jpg",
    "cirkus-maximus": "Circus_Maximus_Rome.jpg",
    "svata-schody": "Scala_Santa_1.jpg",
    "piazza-del-popolo": "Piazza_del_Popolo_Rome.jpg",
    # === Nórsko — Bergen ===
    # Hodnota "search:<dotaz>" => obrázok sa vyhľadá cez Commons fulltext
    # (použité tam, kde presný názov súboru nepoznáme).
    "bryggen": "search:Bryggen Bergen Hanseatic wharf",
    "floyen": "search:Fløyen Bergen view from",
    "fisketorget": "search:Fisketorget Bergen fish market",
    "bergenhus": "search:Bergenhus fortress Bergen",
    "mariakirken": "search:Mariakirken Bergen church",
    "troldhaugen": "search:Troldhaugen Grieg villa",
    "ulriken": "Ulriken_Bergen.jpg",
    "fantoft": "Fantoft_stavkirke.jpg",
    # === Nórsko — Stavanger ===
    "gamle-stavanger": "Gamle_Stavanger.jpg",
    "stavanger-domkirken": "Stavanger_Cathedral.jpg",
    "fargegaten": "search:Øvre Holmegate Stavanger",
    "sverd-i-fjell": "search:Sverd i fjell Hafrsfjord monument",
    "oljemuseet": "search:Norwegian Petroleum Museum Stavanger",
    "preikestolen": "search:Preikestolen Pulpit Rock Lysefjord",
    "lysefjord": "Lysefjorden.jpg",
    "kjerag": "Kjeragbolten.jpg",
    # === Nórsko — fjordy ===
    "geirangerfjord": "Geirangerfjord.jpg",
    "naeroyfjord": "Nærøyfjord.jpg",
    "flam": "search:Flåm Aurlandsfjord",
    "trolltunga": "search:Trolltunga rock formation Norway",
    "voringsfossen": "Vøringsfossen.jpg",
    "trollstigen": "Trollstigen.jpg",
    "briksdal": "Briksdalsbreen.jpg",
    # === Nórsko — popri ceste (nové) ===
    "kossdalen": "Kossdalssvingane.jpg",
    "latefossen": "search:Låtefossen waterfall",
    "roldal-stavkyrkje": "search:Røldal stave church stavkyrkje",
}

WIKI_API = "https://commons.wikimedia.org/w/api.php"


def get_image_url(filename):
    """Získa thumbnail URL obrázka z Wikimedia Commons API (800px šírka)."""
    decoded = unquote(filename)
    params = {
        "action": "query",
        "titles": f"File:{decoded}",
        "prop": "imageinfo",
        "iiprop": "url",
        "iiurlwidth": MAX_WIDTH,
        "format": "json",
    }
    resp = requests.get(WIKI_API, params=params, headers=HEADERS, timeout=30)
    data = resp.json()
    pages = data.get("query", {}).get("pages", {})
    for page in pages.values():
        imageinfo = page.get("imageinfo", [])
        if imageinfo:
            # Preferuj thumbnail URL (predgenerovaný, nie rate-limited)
            return imageinfo[0].get("thumburl") or imageinfo[0]["url"]
    return None


def search_image_url(query):
    """Nájde najvhodnejší obrázok cez Commons fulltext vyhľadávanie.

    Vyberie prvý JPEG/PNG na šírku (landscape) s rozumným rozlíšením,
    vráti jeho thumbnail URL (800px). Použité, keď nepoznáme presný názov.
    """
    params = {
        "action": "query",
        "format": "json",
        "generator": "search",
        "gsrsearch": query,
        "gsrnamespace": 6,  # File:
        "gsrlimit": 15,
        "prop": "imageinfo",
        "iiprop": "url|size|mime",
        "iiurlwidth": MAX_WIDTH,
    }
    resp = requests.get(WIKI_API, params=params, headers=HEADERS, timeout=30)
    data = resp.json()
    pages = data.get("query", {}).get("pages", {})

    # Zachovaj poradie relevancie podľa "index"
    candidates = sorted(pages.values(), key=lambda p: p.get("index", 999))
    best = None
    for page in candidates:
        info = page.get("imageinfo", [{}])[0]
        mime = info.get("mime", "")
        if mime not in ("image/jpeg", "image/png"):
            continue
        w, h = info.get("width", 0), info.get("height", 0)
        url = info.get("thumburl") or info.get("url")
        if not url:
            continue
        # Preferuj landscape s aspoň ~800px šírkou
        if w >= h and w >= 800:
            return url
        if best is None:
            best = url
    return best


def download_and_resize(url, output_path):
    """Stiahne obrázok, zmenší na MAX_WIDTH a uloží ako JPEG."""
    resp = requests.get(url, headers=HEADERS, timeout=60)
    resp.raise_for_status()

    img = Image.open(BytesIO(resp.content))
    img = img.convert("RGB")

    if img.width > MAX_WIDTH:
        ratio = MAX_WIDTH / img.width
        new_height = int(img.height * ratio)
        img = img.resize((MAX_WIDTH, new_height), Image.LANCZOS)

    img.save(output_path, "JPEG", quality=85)
    return img.size


def generate_icons():
    """Generuje PWA ikony."""
    os.makedirs(ICON_DIR, exist_ok=True)

    for size in (512, 192):
        img = Image.new("RGB", (size, size), "#e94560")
        draw = ImageDraw.Draw(img)

        # Kruh v strede
        margin = size // 8
        draw.ellipse(
            [margin, margin, size - margin, size - margin],
            fill="#1a1a2e",
        )

        # Text "R" v strede
        font_size = size // 3
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)
        except (OSError, IOError):
            font = ImageFont.load_default()

        bbox = draw.textbbox((0, 0), "R", font=font)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]
        x = (size - text_w) // 2
        y = (size - text_h) // 2 - bbox[1]
        draw.text((x, y), "R", fill="#e94560", font=font)

        path = os.path.join(ICON_DIR, f"icon-{size}.png")
        img.save(path, "PNG")
        print(f"  Ikona: icon-{size}.png")


def main():
    force = "--force" in sys.argv

    os.makedirs(IMG_DIR, exist_ok=True)

    print("Generujem PWA ikony...\n")
    generate_icons()

    print(f"\nSťahujem {len(IMAGES)} obrázkov z Wikimedia Commons...\n")

    for place_id, wiki_filename in IMAGES.items():
        output_path = os.path.join(IMG_DIR, f"{place_id}.jpg")

        if os.path.exists(output_path) and not force:
            print(f"  Preskakujem {place_id}.jpg (už existuje)")
            continue

        print(f"  Sťahujem {place_id}...", end=" ", flush=True)
        for attempt in range(5):
            try:
                if wiki_filename.startswith("search:"):
                    url = search_image_url(wiki_filename[len("search:"):])
                else:
                    url = get_image_url(wiki_filename)
                if not url:
                    print("CHYBA: URL nenájdená")
                    break

                w, h = download_and_resize(url, output_path)
                size_kb = os.path.getsize(output_path) // 1024
                print(f"OK ({w}x{h}, {size_kb} KB)")
                break
            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 429 and attempt < 4:
                    wait = 20 * (attempt + 1)
                    print(f"rate limited, čakám {wait}s...", end=" ", flush=True)
                    time.sleep(wait)
                else:
                    print(f"CHYBA: {e}")
                    break
            except Exception as e:
                print(f"CHYBA: {e}")
                break
        time.sleep(6)  # pauza medzi requestmi (šetrnejšie k Wikimedia)

    print(f"\nHotovo! Obrázky uložené v {IMG_DIR}")


if __name__ == "__main__":
    main()
