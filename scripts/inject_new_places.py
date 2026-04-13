#!/usr/bin/env python3
"""Pridanie 10 nových miest z new_places_data.py do data.js.

Vloží JS objekty pred uzatváraciu `];` PLACES poľa.
Preskočí miesta, ktoré už v data.js existujú (podľa id).
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from new_places_data import NEW_PLACES

DATA_JS = os.path.join(os.path.dirname(__file__), "..", "js", "data.js")


def js_escape(s):
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")


def format_place(place):
    lat, lon = place["coords"]
    image = place.get("image", f"img/places/{place['id']}.jpg")

    info_lines = ",\n".join(
        f'            "{js_escape(k)}": "{js_escape(v)}"' for k, v in place["info"].items()
    )

    texts = place["texts"]
    text_lines = ",\n".join(
        f'            {key}: "{js_escape(texts[key])}"' for key in ("short", "medium", "long")
    )

    legend_entries = []
    for legend in place.get("legends", []):
        title = js_escape(legend["title"])
        text = js_escape(legend["text"])
        legend_entries.append(
            f'            {{ id: "{legend["id"]}", title: "{title}", text: "{text}" }}'
        )

    legends_block = ""
    if legend_entries:
        legends_block = (
            ",\n        legends: [\n"
            + ",\n".join(legend_entries)
            + "\n        ]"
        )

    return f"""    {{
        id: "{place['id']}",
        name: "{js_escape(place['name'])}",
        category: "{place['category']}",
        coords: {{ lat: {lat}, lon: {lon} }},
        image: "{image}",
        emoji: "{place['emoji']}",
        info: {{
{info_lines}
        }},
        texts: {{
{text_lines}
        }}{legends_block}
    }}"""


def main():
    with open(DATA_JS, "r", encoding="utf-8") as f:
        content = f.read()

    # Identifikuj uzatváracie `]` PLACES poľa (pred `;\n\n// Make available...`)
    closing_pattern = re.compile(r"\n\];\s*\n")
    m = closing_pattern.search(content)
    if not m:
        print("CHYBA: nenájdené uzatváranie PLACES poľa")
        return

    insert_pos = m.start()  # pred `\n];`

    # Zisti, ktoré miesta už existujú
    existing_ids = set(re.findall(r'id:\s*"([^"]+)"', content))

    new_blocks = []
    for place in NEW_PLACES:
        if place["id"] in existing_ids:
            print(f"  Preskakujem {place['id']} (už existuje)")
            continue
        new_blocks.append(format_place(place))
        print(f"  OK: {place['id']}")

    if not new_blocks:
        print("Žiadne nové miesta na pridanie.")
        return

    insertion = ",\n" + ",\n".join(new_blocks)
    content = content[:insert_pos] + insertion + content[insert_pos:]

    with open(DATA_JS, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\nPridaných {len(new_blocks)} miest.")


if __name__ == "__main__":
    main()
