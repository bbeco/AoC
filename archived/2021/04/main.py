#!/usr/bin/env python

import sys


def main() -> int:
    if len(sys.argv) < 2:
        return 1

    with open(sys.argv[1]) as f:
        extracted = [int(char) for char in f.readline().split(",")]
        
        f.readline()
        boards = []
        while True:
            line = f.readline()
            if line == "":
                boards.append(board)
                board = []
            board.append(int(char) for char in line)

    while 
    return 0


if __name__ == "__main__":
    sys.exit(main())
