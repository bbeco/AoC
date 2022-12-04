#!/usr/bin/env python

from __future__ import annotations
import sys
from typing import Tuple


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)


def parse(line: str) -> Vector:
    cmd, length = line.split(" ")
    if cmd == "forward":
        return Vector(int(length), 0)
    if cmd == "down":
        return Vector(0, int(length))
    if cmd == "up":
        return Vector(0, -1 * int(length))
    else:
        raise RuntimeError("Unrecognized command")


def parse2(line: str, aim: int) -> Tuple[int, Vector]:
    cmd, arg = line.split(" ")
    length = int(arg)
    v = Vector(0, 0)
    dAim: int = 0
    if cmd == "down":
        dAim += length
    elif cmd == "up":
        dAim -= length
    elif cmd == "forward":
        v += Vector(length, aim * length)
    return dAim, v


def main() -> int:
    if len(sys.argv) < 2:
        return 1

    with open(sys.argv[1]) as f:
        lines = f.readlines()

    # part 1
    finalPos = sum([parse(s) for s in lines], start=Vector(0, 0))
    print(finalPos.x * finalPos.y)

    # part 2
    finalPos = Vector(0, 0)
    aim = 0
    for line in lines:
        da, v = parse2(line, aim)
        finalPos += v
        aim += da

    print(finalPos.x * finalPos.y)
    return 0


if __name__ == "__main__":
    sys.exit(main())
