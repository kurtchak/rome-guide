#!/usr/bin/env python3
"""Injekcia cien/radov/odkazov z pricing_data.py do js/data.js.

Pre každé miesto nájde blok `info: { ... }` a doplní do neho ďalšie kľúče
(Vstup, Rad, Extra, Poznámka, Web). Existujúce kľúče rovnakého mena nahradí.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from pricing_data import PRICING

DATA_JS = os.path.join(os.path.dirname(__file__), "..", "js", "data.js")


def js_escape(s):
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")


def main():
    with open(DATA_JS, "r", encoding="utf-8") as f:
        content = f.read()

    for place_id, fields in PRICING.items():
        # Nájdi place block — lokalizuj info: { ... } v kontexte id
        id_match = re.search(rf'id:\s*"{re.escape(place_id)}"', content)
        if not id_match:
            print(f"CHYBA: miesto {place_id} nenájdené")
            continue

        # Info block sa nachádza po id — najbližší `info: {` po id_match
        info_match = re.search(r'info:\s*\{([^{}]*)\}', content[id_match.end():], re.DOTALL)
        if not info_match:
            print(f"CHYBA: info block pre {place_id} sa nenašiel")
            continue

        info_start = id_match.end() + info_match.start()
        info_end = id_match.end() + info_match.end()
        info_body = info_match.group(1)

        # Odstráň z existujúceho info telá kľúčov, ktoré budeme nahrádzať
        new_body = info_body
        for key in fields.keys():
            pattern = rf',?\s*"{re.escape(key)}"\s*:\s*"(?:[^"\\]|\\.)*"'
            new_body = re.sub(pattern, "", new_body)

        # Normalizuj konce — odstráň trailing whitespace
        new_body = new_body.rstrip().rstrip(",")

        # Pridaj nové kľúče
        new_entries = []
        for key, value in fields.items():
            new_entries.append(f'            "{js_escape(key)}": "{js_escape(value)}"')

        new_info = "info: {\n" + new_body.strip("\n")
        if new_body.strip():
            new_info += ",\n"
        else:
            new_info += "\n"
        new_info += ",\n".join(new_entries)
        new_info += "\n        }"

        content = content[:info_start] + new_info + content[info_end:]
        print(f"  OK: {place_id} ({len(fields)} polí)")

    with open(DATA_JS, "w", encoding="utf-8") as f:
        f.write(content)

    print("\nHotovo.")


if __name__ == "__main__":
    main()
