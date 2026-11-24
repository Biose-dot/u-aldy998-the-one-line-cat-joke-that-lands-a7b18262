#!/usr/bin/env python3
"""Writes the competition entry text to entry.txt."""
import os


ENTRY = "My cat knocked my laptop off the table, and my agent's incident report read: 'User's cat has identified a critical flaw in gravity. Patch scheduled for never.'"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
