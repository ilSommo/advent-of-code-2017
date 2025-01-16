"""Day 5: A Maze of Twisty Trampolines, All Alike"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"


def main():
    """Solve day 5 puzzles."""
    with open("data/day_5.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    instructions = load_instructions(puzzle_input)
    step = 0
    i = 0

    while 0 <= i < len(instructions):
        old_i = i
        i += instructions[i]
        instructions[old_i] += 1
        step += 1

    return step


def star_2(puzzle_input):
    """Solve second puzzle."""
    instructions = load_instructions(puzzle_input)
    step = 0
    i = 0

    while 0 <= i < len(instructions):
        old_i = i
        i += instructions[i]
        instructions[old_i] = (
            instructions[old_i] - 1
            if instructions[old_i] >= 3
            else instructions[old_i] + 1
        )
        step += 1

    return step


def load_instructions(puzzle_input):
    """Load instructions from input."""
    return [int(line) for line in puzzle_input]


if __name__ == "__main__":
    main()
