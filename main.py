#!/usr/bin/env python3
"""One Emoji, One Dream Vacation.

Writes exactly one emoji to /output/entry.txt: a beach with umbrella,
the whole dream vacation in one glyph - sun, sand, shade, and nowhere
else to be.
"""

import os

EMOJI = "\U0001f3d6"  # beach with umbrella

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
