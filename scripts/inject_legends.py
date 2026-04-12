#!/usr/bin/env python3
"""Injekcia legiend z legends_data.py do js/data.js.

Pre každé miesto nájde koniec bloku `texts: { ... }` a vloží za neho
pole `legends: [...]`. Spustí sa raz; opakovaný beh ignoruje miesta,
ktoré už pole `legends` majú.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from legends_data import LEGENDS

DATA_JS = os.path.join(os.path.dirname(__file__), "..", "js", "data.js")


def js_escape(s):
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")


def format_legends(legends):
    lines = ["        legends: ["]
    entries = []
    for l in legends:
        title = js_escape(l["title"])
        text = js_escape(l["text"])
        entries.append(
            f'            {{ id: "{l["id"]}", title: "{title}", text: "{text}" }}'
        )
    lines.append(",\n".join(entries))
    lines.append("        ]")
    return "\n".join(lines)


def main():
    with open(DATA_JS, "r", encoding="utf-8") as f:
        content = f.read()

    for place_id, legends in LEGENDS.items():
        # Preskočiť ak už má legends
        place_match = re.search(
            rf'id:\s*"{re.escape(place_id)}"(.*?)(\n    \}}(?:,|\n\];))',
            content,
            re.DOTALL,
        )
        if not place_match:
            print(f"CHYBA: miesto {place_id} nenájdené")
            continue

        place_body = place_match.group(1)
        if "legends:" in place_body:
            print(f"  Preskakujem {place_id} (už má legends)")
            continue

        # Nájdi koniec bloku `texts: {}` — vzor `\n        }\n    }`
        id_end = place_match.start() + len(place_match.group(0).split("\n")[0])
        end_pattern = re.compile(r"\n        \}\n    \}")
        end_m = end_pattern.search(content, id_end)
        if not end_m:
            print(f"CHYBA: koniec bloku {place_id} sa nenašiel")
            continue

        insert_pos = end_m.start() + len("\n        }")
        legends_js = format_legends(legends)
        new_text = ",\n" + legends_js
        content = content[:insert_pos] + new_text + content[insert_pos:]
        print(f"  OK: {place_id} ({len(legends)} legiend)")

    with open(DATA_JS, "w", encoding="utf-8") as f:
        f.write(content)

    print("\nHotovo.")


if __name__ == "__main__":
    main()
