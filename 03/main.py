#!/usr/bin/env python

import sys
from typing import List


def getPriority(c: str) -> int:
    if c.islower():
        return ord(c) - 96
    return ord(c) - 38


def part1(lines: List[str]) -> int:
    return sum(
        getPriority(next(iter(_c)))
        for _c in (
            s0 & s1
            for (s0, s1) in (
                ({x for x in _l[0:_m]}, {x for x in _l[_m:]})
                for (_l, _m) in zip(
                    lines, (len(_l) >> 1 for _l in (_l.rstrip() for _l in lines))
                )
            )
        )
    )


def part2(lines: List[str]) -> int:
    return sum(
        getPriority(next(iter(_c)))
        for _c in (
            s0 & s1 & s2
            for (s0, s1, s2) in (
                (set(_l) for _l in _t)
                for _t in (
                    (_l.rstrip() for _l in _t)
                    for _t in zip(lines[::3], lines[1::3], lines[2::3])
                )
            )
        )
    )


def main(filePath: str) -> int:
    with open(filePath, "r") as f:
        lines = f.readlines()
    print(part1(lines))
    print(part2(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
