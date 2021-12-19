#!/usr/bin/env python

import sys


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


def parse(line: str) -> Vector:
    cmd, length = line.split(' ')
    if cmd == 'forward':
        return Vector(int(length), 0)
    if cmd == 'down':
        return Vector(0, int(length))
    if cmd == 'up':
        return Vector(0, -1*int(length))
    else:
        raise RuntimeError('Unrecognized command')


def main():
    if len(sys.argv) < 2:
        return 1

    # part 1
    with open(sys.argv[1]) as f:
        values = [parse(s) for s in f.readlines()]

    finalPos = sum(values, start=Vector(0, 0))
    print(finalPos.x * finalPos.y)

    # TODO part 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
