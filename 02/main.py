#!/usr/bin/env python

import sys
from typing import Callable, Dict, List, Optional, Tuple


# code to choice
C = {"A": "R", "B": "P", "C": "S", "X": "R", "Y": "P", "Z": "S"}


def getShapes1(line: str) -> Optional[Tuple[str, str]]:
    # (opponent's, yours)
    try:
        return C[line[0]], C[line[2]]
    except IndexError:
        return None


WHAT_TO_CHOOSE: Dict[Tuple[str, str], str] = {
    ('R', 'X'): 'S',
    ('R', 'Y'): 'R',
    ('R', 'Z'): 'P',

    ('P', 'X'): 'R',
    ('P', 'Y'): 'P',
    ('P', 'Z'): 'S',

    ('S', 'X'): 'P',
    ('S', 'Y'): 'S',
    ('S', 'Z'): 'R',
}


def getShapes2(line: str) -> Optional[Tuple[str, str]]:
    # (opponent's, yours)
    try:
        tmp = getShapes1(line)
        if not tmp:
            return None
        yours = WHAT_TO_CHOOSE[(tmp[0], line[2])]
        return tmp[0], yours
    except IndexError:
        return None


# choice to score
CS = {"R": 1, "P": 2, "S": 3}


# outcome score
OS: Dict[Tuple[str, str], int] = {
    ("R", "R"): 3,
    ("R", "P"): 6,
    ("R", "S"): 0,
    ("P", "R"): 0,
    ("P", "P"): 3,
    ("P", "S"): 6,
    ("S", "R"): 6,
    ("S", "P"): 0,
    ("S", "S"): 3,
}


def foo(lines: List[str], getShapes: Callable[[str], Optional[Tuple[str, str]]]) -> int:
    return sum(
        list(
            OS[(opponent, you)] + CS[you]
            for (opponent, you) in (
                (_s for _s in (getShapes(_l) for _l in lines) if _s)
            )
        )
    )


def main(filePath: str) -> int:
    with open(filePath, "r") as f:
        lines = f.readlines()
    print(foo(lines, getShapes1))
    print(foo(lines, getShapes2))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
