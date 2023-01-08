#!/usr/bin/env python3
"""topic-roulette — random GS topic spinner."""

from __future__ import print_function
import os, random, sys

WHEEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "wheel.txt")

PEPS = [
    "No renegotiation. 45 minutes. Go.",
    "The optional subject is watching.",
    "Future you will thank present you. Maybe.",
    "UPSC rewards boring consistency.",
]


def main():
    items = []
    with open(WHEEL) as f:
        for line in f:
            line = line.strip()
            if line:
                items.append(line)
    if not items:
        print("wheel.txt empty")
        return 1
    print("*** REVISION ROULETTE ***")
    print(random.choice(items))
    print()
    print(random.choice(PEPS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
