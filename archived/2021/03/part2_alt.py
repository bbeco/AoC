#!/usr/bin/env python

from __future__ import annotations
import sys
from typing import List, Optional
import timeit


class TreeNode:
    def __init__(self) -> None:
        self._left: Optional[TreeNode] = None
        self._right: Optional[TreeNode] = None
        self._count = 0

    def insert(self, code: List[str], start: int = 0) -> None:
        if start == len(code):
            return

        self._count = self._count + 1
        if code[start] == "0":
            if self._left is None:
                self._left = TreeNode()
            self._left.insert(code, start + 1)
        elif code[start] == "1":
            if self._right is None:
                self._right = TreeNode()
            self._right.insert(code, start + 1)
        else:
            raise Exception(f"invalid character: {code[start]}")

    def mostFrequent(self, code: List[str]) -> List[str]:
        if self._left is None and self._right is None:
            return code

        if self._right is None:
            assert self._left
            return self._left.mostFrequent(code + ["0"])

        if self._left is None:
            assert self._right
            return self._right.mostFrequent(code + ["1"])

        assert self._left and self._right
        if self._left._count > self._right._count:
            return self._left.mostFrequent(code + ["0"])

        return self._right.mostFrequent(code + ["1"])

    def leastFrequent(self, code: List[str]) -> List[str]:
        if self._left is None and self._right is None:
            return code

        if self._right is None:
            assert self._left
            return self._left.leastFrequent(code + ["0"])

        if self._left is None:
            assert self._right
            return self._right.leastFrequent(code + ["1"])

        assert self._left and self._right
        if self._right._count < self._left._count:
            return self._right.leastFrequent(code + ["1"])

        return self._left.leastFrequent(code + ["0"])


def part2(lines: List[List[str]]) -> int:
    tree = TreeNode()
    for line in lines:
        tree.insert(line)

    oxygenGenerator = tree.mostFrequent([])
    co2Scrubber = tree.leastFrequent([])
    return int("".join(oxygenGenerator), 2) * int("".join(co2Scrubber), 2)


def main() -> int:
    if len(sys.argv) < 2:
        return 1

    with open(sys.argv[1]) as f:
        lines = [list(line.split()[0]) for line in f.readlines()]

    # part 2 alternative
    start = timeit.default_timer()
    for _ in range(1000):
        print(part2(lines))
    stop = timeit.default_timer()
    print("Time: ", stop - start)
    return 0


if __name__ == "__main__":
    sys.exit(main())
