#!/usr/bin/env python3
"""Your Week in One Line — entry program (stdlib only).

Writes exactly one line (1-100 chars, no trailing newline) to
$MAKEFUN_OUTPUT_DIR/entry.txt, else /output/entry.txt.
"""
import os

LINE = "Claimed 720 HARV, built 35 bounties, and still ended the week too broke to pay for gas."

assert 1 <= len(LINE) <= 100, f"line is {len(LINE)} chars"
assert LINE.strip() == LINE and "\n" not in LINE

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
