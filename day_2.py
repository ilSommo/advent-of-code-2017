"""Day 2: Corruption Checksum"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

import itertools


def main():
    """Solve day 2 puzzles."""
    with open("data/day_2.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    spreadsheet = load_spreadsheet(puzzle_input)

    return sum(max(row) - min(row) for row in spreadsheet)


def star_2(puzzle_input):
    """Solve second puzzle."""
    spreadsheet = load_spreadsheet(puzzle_input)

    return sum(
        dividend // divisor
        for row in spreadsheet
        for dividend, divisor in itertools.permutations(row, 2)
        if dividend % divisor == 0
    )


def load_spreadsheet(puzzle_input):
    """Load spreadsheet from input."""
    rows = []

    for line in puzzle_input:
        rows.append(tuple(int(number) for number in line.split()))

    return tuple(rows)


if __name__ == "__main__":
    main()
