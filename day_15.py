"""Day 15: Dueling Generators"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

DIVISOR = 2147483647


def main():
    """Solve day 15 puzzles."""
    with open("data/day_15.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    a, b = load_generators(puzzle_input)
    pairs = 0

    for _ in range(int(40e6)):
        a = compute_next_a(a)
        b = compute_next_b(b)

        if f"{a:016b}"[-16:] == f"{b:016b}"[-16:]:
            pairs += 1

    return pairs


def star_2(puzzle_input):
    """Solve second puzzle."""
    a, b = load_generators(puzzle_input)
    pairs = 0

    for _ in range(int(5e6)):
        a = compute_next_a(a)
        b = compute_next_b(b)

        while a % 4 != 0:
            a = compute_next_a(a)

        while b % 8 != 0:
            b = compute_next_b(b)

        if f"{a:016b}"[-16:] == f"{b:016b}"[-16:]:
            pairs += 1

    return pairs


def compute_next_a(a):
    """Compute next value for generator A."""
    return (a * 16807) % DIVISOR


def compute_next_b(b):
    """Compute next value for generator B."""
    return (b * 48271) % DIVISOR


def load_generators(puzzle_input):
    """Load generators from puzzle_input."""
    return int(puzzle_input[0].split()[-1]), int(puzzle_input[1].split()[-1])


if __name__ == "__main__":
    main()
