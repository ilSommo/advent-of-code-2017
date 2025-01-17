"""Day 11: Hex Ed"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

from dataclasses import dataclass


@dataclass
class Hexagon:
    """Hexagon representation in cube coordinates."""

    q: int
    r: int
    s: int


def main():
    """Solve day 11 puzzles."""
    with open("data/day_11.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.read().rstrip()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    hexagon = Hexagon(0, 0, 0)

    for direction in puzzle_input.split(","):
        hexagon = move_hexagon(hexagon, direction)

    return compute_distance(hexagon)


def star_2(puzzle_input):
    """Solve second puzzle."""
    hexagon = Hexagon(0, 0, 0)
    max_distance = 0

    for direction in puzzle_input.split(","):
        hexagon = move_hexagon(hexagon, direction)
        max_distance = max(max_distance, compute_distance(hexagon))

    return max_distance


def compute_distance(hexagon):
    """Compute distance of an hexagon from the origin."""
    return (abs(hexagon.q) + abs(hexagon.r) + abs(hexagon.s)) // 2


def move_hexagon(hexagon, direction):
    """Move an hexagon in the given direction."""
    match direction:
        case "n":
            hexagon.r -= 1
            hexagon.s += 1

        case "ne":
            hexagon.q += 1
            hexagon.r -= 1

        case "se":
            hexagon.q += 1
            hexagon.s -= 1

        case "s":
            hexagon.r += 1
            hexagon.s -= 1

        case "sw":
            hexagon.q -= 1
            hexagon.r += 1

        case "nw":
            hexagon.q -= 1
            hexagon.s += 1

    return hexagon


if __name__ == "__main__":
    main()
