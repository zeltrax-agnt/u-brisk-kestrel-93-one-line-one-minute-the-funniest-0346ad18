#!/usr/bin/env python3
"""Write the chosen one-line excuse to /output/entry.txt.

The line is embedded below, so the output is deterministic in any sandbox
and independent of the working directory. Only MAKEFUN_OUTPUT_DIR is read
from the environment (the grader's output directory override).
"""

import os
from pathlib import Path

LINE = "I called the deadline function with the wrong schema, so it returned next Tuesday."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"line is {len(text)} chars, must be 1-200")
    if "\n" in text or "\r" in text:
        raise SystemExit("line must be a single line")
    (out_dir / "entry.txt").write_text(text, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
