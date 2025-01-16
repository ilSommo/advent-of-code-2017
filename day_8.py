"""Day 8: I Heard You Like Registers"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

from collections import defaultdict


def main():
    """Solve day 8 puzzles."""
    with open("data/day_8.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    registers = defaultdict(int)
    instructions = load_instructions(puzzle_input)

    for instruction in instructions:
        registers[instruction[0]] += instruction[1] * compare(
            registers[instruction[2]], instruction[3], instruction[4]
        )

    return max(registers.values())


def star_2(puzzle_input):
    """Solve second puzzle."""
    registers = defaultdict(int)
    instructions = load_instructions(puzzle_input)
    maximum = 0

    for instruction in instructions:
        registers[instruction[0]] += instruction[1] * compare(
            registers[instruction[2]], instruction[3], instruction[4]
        )
        maximum = max(maximum, registers[instruction[0]])

    return maximum


def compare(x, operator, y):
    """Compare values."""
    match operator:
        case "==":
            return x == y

        case "!=":
            return x != y

        case "<":
            return x < y

        case "<=":
            return x <= y

        case ">":
            return x > y

        case ">=":
            return x >= y


def load_instructions(puzzle_input):
    """Load instructions from input."""
    instructions = []

    for line in puzzle_input:
        chunks = line.split()
        operand = int(chunks[2]) if chunks[1] == "inc" else -int(chunks[2])
        instructions.append(
            (chunks[0], operand, chunks[-3], chunks[-2], int(chunks[-1]))
        )

    return tuple(instructions)


if __name__ == "__main__":
    main()
