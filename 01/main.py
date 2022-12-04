#!/usr/bin/env python

import sys
from typing import Iterable, List


def bar(lines: List[str]) -> Iterable[List[str]]:
    def isNumber(x: str) -> bool:
        try:
            int(x)
        except ValueError:
            return False
        return True

    i = 0
    while i < len(lines):
        try:
            start = [isNumber(_l) for _l in lines].index(True, i)
        except ValueError:
            start = len(lines)
        try:
            end = [isNumber(_l) for _l in lines].index(False, start)
        except ValueError:
            end = len(lines)
        yield lines[start:end]
        i = end


def listOfCalories(lines: List[str]) -> Iterable[int]:
    return (sum(_nl) for _nl in ([int(_x) for _x in _l] for _l in bar(lines)))


def part1(lines: List[str]) -> int:
    return max(listOfCalories(lines))


def part2(lines: List[str]) -> int:
    return sum(sorted(list(listOfCalories(lines)))[-3:])


def main(filePath: str) -> int:
    with open(filePath, "r") as f:
        lines = f.readlines()
    print(part1(lines))
    print(part2(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
