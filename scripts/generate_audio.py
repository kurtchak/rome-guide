#!/usr/bin/env python3
"""Generovanie MP3 audio súborov z textov v data.js pomocou edge-tts."""

import asyncio
import os
import re
import sys

import edge_tts

VOICE = "sk-SK-LukasNeural"
DATA_JS = os.path.join(os.path.dirname(__file__), "..", "js", "data.js")
AUDIO_DIR = os.path.join(os.path.dirname(__file__), "..", "audio")
TIER_MAP = {"short": "30s", "medium": "1min", "long": "3min"}
CONCURRENCY = 3


def parse_places(filepath):
    """Parsuje data.js a extrahuje place ID a texty."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    places = []
    # Rozdelíme na bloky podľa id:
    blocks = re.split(r'\{\s*\n\s*id:', content)

    for block in blocks[1:]:  # prvý blok je pred prvým id
        id_match = re.search(r'^\s*"([^"]+)"', block)
        if not id_match:
            continue
        place_id = id_match.group(1)

        texts = {}
        for tier in ("short", "medium", "long"):
            # Hľadáme tier: "..." — text môže obsahovať \n a escaped quotes
            pattern = rf'{tier}:\s*"((?:[^"\\]|\\.)*)"'
            match = re.search(pattern, block, re.DOTALL)
            if match:
                # Dekódujeme escape sekvencie
                text = match.group(1)
                text = text.replace("\\n", "\n")
                text = text.replace('\\"', '"')
                text = text.replace("\\\\", "\\")
                # Nahradíme Unicode escape
                text = re.sub(
                    r"\\u([0-9a-fA-F]{4})",
                    lambda m: chr(int(m.group(1), 16)),
                    text,
                )
                texts[tier] = text

        if texts:
            places.append({"id": place_id, "texts": texts})

    return places


async def generate_one(place_id, tier_key, text, force=False):
    """Vygeneruje jeden MP3 súbor."""
    filename = f"{place_id}-{TIER_MAP[tier_key]}.mp3"
    filepath = os.path.join(AUDIO_DIR, filename)

    if os.path.exists(filepath) and not force:
        print(f"  Preskakujem {filename} (už existuje)")
        return

    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(filepath)
    print(f"  Hotovo: {filename}")


async def main():
    force = "--force" in sys.argv

    os.makedirs(AUDIO_DIR, exist_ok=True)

    print("Parsovanie data.js...")
    places = parse_places(DATA_JS)
    print(f"Nájdených {len(places)} miest\n")

    total = sum(len(p["texts"]) for p in places)
    done = 0
    semaphore = asyncio.Semaphore(CONCURRENCY)

    async def limited(place_id, tier_key, text):
        nonlocal done
        async with semaphore:
            await generate_one(place_id, tier_key, text, force)
            done += 1
            print(f"  [{done}/{total}]")

    tasks = []
    for place in places:
        for tier_key, text in place["texts"].items():
            tasks.append(limited(place["id"], tier_key, text))

    print(f"Generujem {total} audio súborov (hlas: {VOICE})...\n")
    await asyncio.gather(*tasks)
    print(f"\nHotovo! Vygenerovaných {total} MP3 súborov v {AUDIO_DIR}")


if __name__ == "__main__":
    asyncio.run(main())
