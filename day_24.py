"""Day 24: Electromagnetic Moat"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

from collections import deque


def main():
    """Solve day 24 puzzles."""
    with open("data/day_24.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    components = load_components(puzzle_input)
    bridges = deque()
    strongest = 0

    bridges.extend(extend_bridge(([], components)))

    while bridges:
        bridge = bridges.popleft()
        strongest = max(
            strongest,
            sum(component for component in bridge[0]),
        )
        bridges.extend(extend_bridge(bridge))

    return strongest


def star_2(puzzle_input):
    """Solve second puzzle."""
    components = load_components(puzzle_input)
    bridges = deque()
    strongest = 0
    longest = 0

    bridges.extend(extend_bridge(([], components)))

    while bridges:
        bridge = bridges.popleft()

        if len(bridge[0]) > longest:
            longest = len(bridge[0])
            strongest = sum(component for component in bridge[0])
        elif len(bridge[0]) == longest:
            strongest = max(
                strongest,
                sum(component for component in bridge[0]),
            )

        bridges.extend(extend_bridge(bridge))

    return strongest


def extend_bridge(bridge):
    """Create all possible bridge extensions."""
    port = bridge[0][-1] if bridge[0] else 0
    bridges = []

    for component in bridge[1]:
        if port in component:
            new_components = bridge[1].copy()
            new_components.remove(component)
            component = (
                list(component)
                if component[0] == port
                else [component[1], component[0]]
            )

            bridges.append([bridge[0] + component, new_components])

    return bridges


def load_components(puzzle_input):
    """Load components from input."""
    components = []

    for line in puzzle_input:
        ports = line.split("/")
        components.append((int(ports[0]), int(ports[1])))

    return components


if __name__ == "__main__":
    main()
