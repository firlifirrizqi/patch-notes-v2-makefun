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
MAX_CHARS = 160


def verify_output():
    """Read back the written file and confirm it matches ENTRY exactly."""
    with open(OUTPUT_FILE, "r", encoding="utf-8") as handle:
        written = handle.read().rstrip("\n")
    assert written == ENTRY.strip(), "entry.txt content does not match ENTRY"
    return written


def main():
    line = ENTRY.strip()
    assert 1 <= len(line) <= MAX_CHARS, "entry must be 1-160 characters"
    assert "\n" not in line, "entry must be a single line"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    print(f"Wrote {len(line)} characters to {OUTPUT_FILE}")
    verify_output()
    print(f"Verified: {OUTPUT_FILE} matches ENTRY ({len(line)} characters)")


if __name__ == "__main__":
    main()
