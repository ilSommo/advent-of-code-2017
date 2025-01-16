"""Day 6: Memory Reallocation"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"


def main():
    """Solve day 6 puzzles."""
    with open("data/day_6.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.read().rstrip()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    blocks = load_blocks(puzzle_input)
    configurations = []

    while blocks not in configurations:
        configurations.append(blocks)
        blocks = redistribute(blocks)

    return len(configurations)


def star_2(puzzle_input):
    """Solve second puzzle."""
    blocks = load_blocks(puzzle_input)
    configurations = []

    while blocks not in configurations:
        configurations.append(blocks)
        blocks = redistribute(blocks)

    return len(configurations) - configurations.index(blocks)


def load_blocks(puzzle_input):
    """Load memory blocks from input."""
    return tuple(int(block) for block in puzzle_input.split())


def redistribute(blocks):
    """Redistribute memory."""
    blocks = list(blocks)
    memory = max(blocks)
    i_block = blocks.index(memory)
    blocks[i_block] = 0

    for i, _ in enumerate(blocks):
        blocks[i] += memory // len(blocks)

        if 1 <= (i - i_block) % len(blocks) < memory % len(blocks) + 1:
            blocks[i] += 1

    return tuple(blocks)


if __name__ == "__main__":
    main()
