#!/usr/bin/env python3
"""Make the Judge Laugh in One Line.

Writes one original one-liner to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when the variable is unset).
"""

import os

LINE = "I told the barista I needed something strong, and she slid me her resignation letter."


def main() -> None:
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError("line must be 1-200 non-blank characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
