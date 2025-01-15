"""Day 1: Inverse Captcha"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"


def main():
    """Solve day 1 puzzles."""
    with open("data/day_1.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.read().rstrip()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    return sum(
        int(digit)
        for i, digit in enumerate(puzzle_input)
        if digit == puzzle_input[(i + 1) % len(puzzle_input)]
    )


def star_2(puzzle_input):
    """Solve second puzzle."""
    return sum(
        int(digit)
        for i, digit in enumerate(puzzle_input)
        if digit
        == puzzle_input[(i + len(puzzle_input) // 2) % len(puzzle_input)]
    )


if __name__ == "__main__":
    main()
