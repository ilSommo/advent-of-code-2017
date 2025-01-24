"""Day 21: Fractal Art"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

import itertools

PATTERN = (
    ".#.",
    "..#",
    "###",
)


def main():
    """Solve day 21 puzzles."""
    with open("data/day_21.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    pattern = list(PATTERN)
    rules = load_rules(puzzle_input)

    for _ in range(5):
        pattern = enhance(pattern, rules)

    return sum(line.count("#") for line in pattern)


def star_2(puzzle_input):
    """Solve second puzzle."""
    pattern = list(PATTERN)
    rules = load_rules(puzzle_input)

    for _ in range(18):
        pattern = enhance(pattern, rules)

    return sum(line.count("#") for line in pattern)


def break_up(pattern):
    """Breaak up pattern in squares."""
    size = 2 if len(pattern) % 2 == 0 else 3
    squares = [
        [["" for _ in range(size)] for _ in range(len(pattern) // size)]
        for _ in range(len(pattern) // size)
    ]

    for i, line in enumerate(pattern):
        for j, char in enumerate(line):
            squares[i // size][j // size][i % size] += char

    for i, j in itertools.product(range(len(squares)), repeat=2):
        squares[i][j] = "/".join(squares[i][j])

    return squares


def compose(squares):
    """Compose squares into a pattern."""
    pattern = []

    for i, j in itertools.product(range(len(squares)), repeat=2):
        squares[i][j] = squares[i][j].split("/")

    for i, row in enumerate(squares):
        for j, _ in enumerate(row[0]):
            pattern.append("".join(square[j] for square in row))

    return pattern


def enhance(pattern, rules):
    """Enhance pattern according to rules."""
    squares = break_up(pattern)

    for i, row in enumerate(squares):
        for j, square in enumerate(row):
            squares[i][j] = rules[square]

    return compose(squares)


def generate_equivalent(pattern):
    """Generate all equivalent patterns."""
    lines = [list(line) for line in pattern.split("/")]
    patterns = set()

    for _ in range(4):
        lines = ["".join(row) for row in zip(*reversed(lines))]
        patterns.add("/".join("".join(row) for row in lines))
        patterns.add("/".join("".join(row) for row in reversed(lines)))

    return patterns


def load_rules(puzzle_input):
    """Load rules from input."""
    rules = {}

    for line in puzzle_input:
        chunks = line.split(" => ")
        patterns = generate_equivalent(chunks[0])

        for pattern in patterns:
            rules[pattern] = chunks[1]

    return rules


if __name__ == "__main__":
    main()
