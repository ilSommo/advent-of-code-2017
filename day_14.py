"""Day 14: Disk Defragmentation"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

from functools import reduce

DENSE_SIZE = 16
SIZE = 256


def main():
    """Solve day 14 puzzles."""
    with open("data/day_14.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.read().rstrip()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    squares = get_squares(puzzle_input)

    return len(squares)


def star_2(puzzle_input):
    """Solve second puzzle."""
    squares = get_squares(puzzle_input)
    regions = []

    while squares:
        square_0 = squares.pop()
        regions.append({square_0})

        for i in range(len(regions) - 2, -1, -1):
            for square_1 in regions[i]:
                if abs(square_1 - square_0) == 1:
                    regions[-1].update(regions.pop(i))
                    break

    return len(regions)


def compute_hash(string):
    """Compute knot hash of string."""
    marks = list(range(SIZE))
    position = 0
    skip = 0
    lengths = tuple(ord(char) for char in string) + (17, 31, 73, 47, 23)

    for _ in range(64):
        marks, position, skip = run_round(marks, position, skip, lengths)

    dense_hash = [
        reduce(
            lambda x, y: x ^ y, marks[i * DENSE_SIZE : (1 + i) * DENSE_SIZE]
        )
        for i in range(SIZE // DENSE_SIZE)
    ]

    return "".join(f"{digit:02x}" for digit in dense_hash)


def get_squares(string):
    """Get coordinates of all squares from string."""
    squares = set()

    for i in range(128):
        knot_hash = compute_hash(f"{string}-{i}")

        for j, char in enumerate(
            "".join((f"{int(char,16):04b}" for char in knot_hash))
        ):
            if char == "1":
                squares.add(i + j * 1j)

    return squares


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
