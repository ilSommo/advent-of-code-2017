"""Day 10: Knot Hash"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

from functools import reduce

DENSE_SIZE = 16
SIZE = 256


def main():
    """Solve day 10 puzzles."""
    with open("data/day_10.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.read().rstrip()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    marks = list(range(SIZE))
    position = 0
    skip = 0
    lengths = tuple(int(length) for length in puzzle_input.split(","))

    marks, _, _ = run_round(marks, position, skip, lengths)

    return marks[0] * marks[1]


def star_2(puzzle_input):
    """Solve second puzzle."""
    marks = list(range(SIZE))
    position = 0
    skip = 0
    lengths = tuple(ord(char) for char in puzzle_input) + (17, 31, 73, 47, 23)

    for _ in range(64):
        marks, position, skip = run_round(marks, position, skip, lengths)

    dense_hash = [
        reduce(
            lambda x, y: x ^ y, marks[i * DENSE_SIZE : (1 + i) * DENSE_SIZE]
        )
        for i in range(SIZE // DENSE_SIZE)
    ]

    return "".join(f"{digit:02x}" for digit in dense_hash)


def run_round(marks, position, skip, lengths):
    """Run a single round."""
    for length in lengths:
        for i in range(length // 2):
            (
                marks[(position + i) % SIZE],
                marks[(position + length - i - 1) % SIZE],
            ) = (
                marks[(position + length - i - 1) % SIZE],
                marks[(position + i) % SIZE],
            )
        position = (position + length + skip) % len(marks)
        skip += 1

    return marks, position, skip


if __name__ == "__main__":
    main()
