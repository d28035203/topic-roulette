#!/usr/bin/env python3
"""topic-roulette — pick a random study topic."""
from __future__ import annotations

import argparse
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def load(path: str) -> list[str]:
    out = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line and not line.startswith("#"):
                out.append(line)
    return out


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--file", default=os.path.join(HERE, "wheel.txt"))
    p.add_argument("-n", type=int, default=1)
    p.add_argument("--seed", type=int, default=None)
    args = p.parse_args()
    if args.seed is not None:
        random.seed(args.seed)
    topics = load(args.file)
    if not topics:
        print("no topics", file=sys.stderr)
        return 1
    n = min(args.n, len(topics))
    for t in random.sample(topics, n):
        print(t)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
