#!/usr/bin/env python

import sys


def main():
    if len(sys.argv) < 2:
        return 1

    with open(sys.argv[1]) as f:
        values = [int(s) for s in f.readlines()]

    # part 1
    res = 0
    for i in range(1, len(values)):
        if (values[i] > values[i - 1]):
            res = res + 1

    print(res)

    # part 2
    res = 0
    prev = sum(values[:3])
    for i in range(3, len(values)):
        curr = prev - values[i - 3] + values[i]
        res = res + ((curr - prev) > 0)
        prev = curr

    print(res)

    return 0


if __name__ == "__main__":
    sys.exit(main())
