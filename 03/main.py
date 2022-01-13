#!/usr/bin/env python

from __future__ import annotations
import sys
from typing import List, Tuple
from math import floor


def part1(lines: List[str]) -> int:
    ones: List[int] = [0] * (len(lines[0]) - 1)
    for line in lines:
        v = int(line, base=2)

        i = 0
        while v != 0:
            ones[i] = ones[i] + v % 2
            v = v >> 1
            i += 1

    gamma: int = 0
    for i, m in enumerate(ones):
        if m > len(lines) / 2:
            gamma += pow(2, i)

    return gamma * (pow(2, len(ones)) - 1 - gamma)  # type: int


def altPart1(lines: List[str]) -> int:
    binaries: List[List[int]] = [[int(bit) for bit in line[:-1]] for line in lines]

    acc: List[int] = [0] * len(binaries[0])
    for b in binaries:
        curr = [b0 + b1 for b0, b1 in zip(acc, b)]
        acc = curr

    bEpsilon = [0 if b < floor(len(lines) / 2) else 1 for b in acc]
    epsilon = 0
    for i, b in enumerate(bEpsilon[::-1]):
        epsilon += b * pow(2, i)

    return epsilon * (pow(2, len(binaries[0])) - 1 - epsilon)


def step(
    oxygens: List[str], scrubbers: List[str], idx: int
) -> Tuple[List[str], List[str]]:

    nOxygens = oxygens
    nScrubbers = scrubbers
    for i, lines in enumerate((oxygens, scrubbers)):
        if len(lines) == 1:
            continue

        mo = []
        mz = []
        for line in lines:
            if line[idx] == "0":
                mz.append(line)
            else:
                mo.append(line)

        if len(mz) > len(mo):
            if i == 0:
                nOxygens = mz
            else:
                nScrubbers = mo
        else:
            if i == 0:
                nOxygens = mo
            else:
                nScrubbers = mz

    return nOxygens, nScrubbers


def part2(lines: List[str]) -> int:
    oxygens = lines[:]
    scrubbers = lines[:]
    for i in range(len(lines[0]) - 1):
        oxygens, scrubbers = step(oxygens, scrubbers, i)

    assert len(oxygens) == 1
    assert len(scrubbers) == 1
    return int(oxygens[0], 2) * int(scrubbers[0], 2)


def main() -> int:
    if len(sys.argv) < 2:
        return 1

    with open(sys.argv[1]) as f:
        lines = f.readlines()

    # part 1
    print(part1(lines))

    # part 1 alternative
    print(altPart1(lines))

    # part 2
    print(f"\n{part2(lines)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
