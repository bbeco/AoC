#!/usr/bin/env python

import sys
import re
from typing import List, Tuple


LINE_EXPRESSION = "^(\d+)-(\d+),(\d+)-(\d+)$"


def parse(line: str) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    _m = re.match(LINE_EXPRESSION, line)
    assert _m
    _t = _m.groups()
    return (int(_t[0]), int(_t[1])), (int(_t[2]), int(_t[3]))


def fullOverlap(e0: Tuple[int, int], e1: Tuple[int, int]) -> bool:
    return (e0[0] <= e1[0] and e0[1] >= e1[1]) or (e0[0] >= e1[0] and e0[1] <= e1[1])


def partialOverlap(e0: Tuple[int, int], e1: Tuple[int, int]) -> bool:
    return not (e0[1] < e1[0] or e1[1] < e0[0])


def part1(lines: List[str]) -> int:
    return sum(
        _v
        for _v in (int(fullOverlap(e0, e1)) for (e0, e1) in (parse(_l) for _l in lines))
    )


def part2(lines: List[str]) -> int:
    return sum(
        _v
        for _v in (
            int(partialOverlap(e0, e1)) for (e0, e1) in (parse(_l) for _l in lines)
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
