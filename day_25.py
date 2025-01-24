"""Day 25: The Halting Problem"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

from collections import defaultdict


def main():
    """Solve day 25 puzzles."""
    with open("data/day_25.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    tape = defaultdict(int)
    state, steps, instructions = load_blueprint(puzzle_input)
    cursor = 0

    for _ in range(steps):
        instruction = instructions[state][tape[cursor]]
        tape[cursor] = instruction[0]
        cursor += instruction[1]
        state = instruction[2]

    return sum(tape.values())


def load_blueprint(puzzle_input):
    """Load blueprint from input."""
    start = puzzle_input[0][-2]
    steps = int(puzzle_input[1].split()[-2])
    instructions = {}

    for i in range(3, len(puzzle_input), 10):
        state = puzzle_input[i][-2]
        instructions[state] = {
            0: (
                int(puzzle_input[i + 2][-2]),
                1 if "right" in puzzle_input[i + 3] else -1,
                puzzle_input[i + 4][-2],
            ),
            1: (
                int(puzzle_input[i + 6][-2]),
                1 if "right" in puzzle_input[i + 7] else -1,
                puzzle_input[i + 8][-2],
            ),
        }

    return start, steps, instructions


if __name__ == "__main__":
    main()
