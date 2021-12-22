#!/usr/bin/env python

import sys
from typing import List


def main() -> int:
    if len(sys.argv) < 2:
        return 1

    with open(sys.argv[1]) as f:
        lines = f.readlines()

    # part 1
    ones: List[int] = [0] * (len(lines[0]) - 1)
    for line in lines:
        v = int(line, base=2)

        i = 0
        while v != 0:
            ones[i] = ones[i] + v % 2
            v = v >> 1
            i += 1

    gamma = 0
    for i, m in enumerate(ones):
        if m > len(lines) / 2:
            gamma += pow(2, i)

    print(gamma * (pow(2, len(ones)) - 1 - gamma))

    # TODO part 1 alternative
    return 0


if __name__ == "__main__":
    sys.exit(main())
