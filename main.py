"""Real-Life Patch Notes — v2 entry.

Writes one patch-note line for the Make.fun bounty
"Real-Life Patch Notes: The Comedy Changelog".
Standard library only; no third-party packages.
"""

import os

ENTRY = (
    "v2.6.9: fixed a bug where the brain replayed an embarrassing "
    "moment from 2014 at 3 AM. The memory cache now clears before bedtime."
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    line = ENTRY.strip()
    assert 1 <= len(line) <= 160, "entry must be 1-160 characters"
    assert "\n" not in line, "entry must be a single line"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    print(f"Wrote {len(line)} characters to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
