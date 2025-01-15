"""Day 3: Spiral Memory"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

import itertools


def main():
    """Solve day 3 puzzles."""
    with open("data/day_3.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.read().rstrip()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    square = int(puzzle_input)

    if square == 1:
        return 0

    circle = int((square - 1) ** 0.5 + 1) // 2

    square += circle - (2 * circle - 1) ** 2
    square %= 2 * circle

    return square + circle


def star_2(puzzle_input):
    """Solve second puzzle."""
    threshold = int(puzzle_input)

    squares = {0 + 0j: 1}
    position = 0 + 0j
    direction = 0 - 1j

    while max(squares.values()) <= threshold:
        if position + direction * 1j not in squares:
            direction *= 1j

        position += direction
        squares[position] = sum_neighors(position, squares)

    return max(squares.values())


def sum_neighors(position, squares):
    """Sum neighbors of a square."""
    return sum(
        squares.get(position + i + j * 1j, 0)
        for i, j in itertools.product((-1, 0, 1), repeat=2)
    )


if __name__ == "__main__":
    main()
