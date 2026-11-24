#!/usr/bin/env python3
"""Write one sick-day excuse to /output/entry.txt."""

import os

EXCUSE = (
    "Can't make it in today \u2014 my parrot learned to say "
    "'meeting in five' and has had me in back-to-back calls since 6am."
)


def main() -> None:
    assert 1 <= len(EXCUSE) <= 200, "excuse must be 1-200 characters"
    assert "\n" not in EXCUSE, "excuse must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
