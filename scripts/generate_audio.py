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


def _decode_js_string(raw):
    """Dekóduje JS string literal: \\n, \\\", \\\\, \\uXXXX."""
    text = raw.replace("\\n", "\n").replace('\\"', '"').replace("\\\\", "\\")
    return re.sub(r"\\u([0-9a-fA-F]{4})", lambda m: chr(int(m.group(1), 16)), text)


def parse_places(filepath):
    """Parsuje data.js a extrahuje place ID, texty a legendy."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    places = []
    blocks = re.split(r'\{\s*\n\s*id:', content)

    for block in blocks[1:]:
        id_match = re.search(r'^\s*"([^"]+)"', block)
        if not id_match:
            continue
        place_id = id_match.group(1)

        # Texty (short/medium/long)
        texts = {}
        for tier in ("short", "medium", "long"):
            pattern = rf'{tier}:\s*"((?:[^"\\]|\\.)*)"'
            match = re.search(pattern, block, re.DOTALL)
            if match:
                texts[tier] = _decode_js_string(match.group(1))

        # Legendy: legends: [ { id: "...", title: "...", text: "..." }, ... ]
        legends = []
        legends_match = re.search(r'legends:\s*\[(.*?)\n\s*\]', block, re.DOTALL)
        if legends_match:
            legends_block = legends_match.group(1)
            # Každá legenda je samostatný { ... } objekt
            legend_objs = re.findall(r'\{([^{}]*?)\}', legends_block, re.DOTALL)
            for lo in legend_objs:
                lid_m = re.search(r'id:\s*"((?:[^"\\]|\\.)*)"', lo)
                ltext_m = re.search(r'text:\s*"((?:[^"\\]|\\.)*)"', lo, re.DOTALL)
                if lid_m and ltext_m:
                    legends.append({
                        "id": lid_m.group(1),
                        "text": _decode_js_string(ltext_m.group(1)),
                    })

        if texts or legends:
            places.append({"id": place_id, "texts": texts, "legends": legends})

    return places


async def generate_tier(place_id, tier_key, text, force=False):
    """Vygeneruje jeden MP3 pre tier (30s/1min/3min)."""
    filename = f"{place_id}-{TIER_MAP[tier_key]}.mp3"
    filepath = os.path.join(AUDIO_DIR, filename)

    if os.path.exists(filepath) and not force:
        print(f"  Preskakujem {filename} (už existuje)")
        return

    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(filepath)
    print(f"  Hotovo: {filename}")


async def generate_legend(place_id, legend_id, text, force=False):
    """Vygeneruje jeden MP3 pre legendu."""
    filename = f"{place_id}-legend-{legend_id}.mp3"
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
    tier_count = sum(len(p["texts"]) for p in places)
    legend_count = sum(len(p["legends"]) for p in places)
    total = tier_count + legend_count
    print(f"Nájdených {len(places)} miest, {tier_count} tier textov, {legend_count} legiend\n")

    done = 0
    semaphore = asyncio.Semaphore(CONCURRENCY)

    async def limited_tier(place_id, tier_key, text):
        nonlocal done
        async with semaphore:
            await generate_tier(place_id, tier_key, text, force)
            done += 1
            print(f"  [{done}/{total}]")

    async def limited_legend(place_id, legend_id, text):
        nonlocal done
        async with semaphore:
            await generate_legend(place_id, legend_id, text, force)
            done += 1
            print(f"  [{done}/{total}]")

    tasks = []
    for place in places:
        for tier_key, text in place["texts"].items():
            tasks.append(limited_tier(place["id"], tier_key, text))
        for legend in place["legends"]:
            tasks.append(limited_legend(place["id"], legend["id"], legend["text"]))

    print(f"Generujem {total} audio súborov (hlas: {VOICE})...\n")
    await asyncio.gather(*tasks)
    print(f"\nHotovo! Vygenerovaných {total} MP3 súborov v {AUDIO_DIR}")


if __name__ == "__main__":
    asyncio.run(main())
