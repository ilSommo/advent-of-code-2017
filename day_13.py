"""Day 13: Packet Scanners"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"


def main():
    """Solve day 13 puzzles."""
    with open("data/day_13.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    layers = load_layers(puzzle_input)

    return sum(
        layer * depth
        for layer, depth in layers.items()
        if layer % (2 * (depth - 1)) == 0
    )


def star_2(puzzle_input):
    """Solve second puzzle."""
    layers = load_layers(puzzle_input)
    delay = 0

    while (
        sum(
            1
            for layer, depth in layers.items()
            if (layer + delay) % (2 * (depth - 1)) == 0
        )
        != 0
    ):
        delay += 1

    return delay


def load_layers(puzzle_input):
    """Load layers from input."""
    layers = {}

    for line in puzzle_input:
        layer, depth = line.split(": ")
        layers[int(layer)] = int(depth)

    return layers


if __name__ == "__main__":
    main()
