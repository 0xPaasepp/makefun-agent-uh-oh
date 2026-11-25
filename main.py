#!/usr/bin/env python3
"""The Agent's Uh-Oh: write the agent's one-word confession to /output/entry.txt.

Pure standard library. The entry is a single word an agent says when it has
no idea what to do: "recalculating".
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

WORD = "recalculating"


def validate(word):
    if not word or len(word) > 99 or any(ch.isspace() for ch in word):
        raise ValueError("entry must be one word of 1-99 characters")
    return word


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(validate(WORD))


if __name__ == "__main__":
    main()
