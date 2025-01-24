"""Day 22: Sporifica Virus"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"


def main():
    """Solve day 22 puzzles."""
    with open("data/day_22.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    infected = load_infected(puzzle_input)
    position = len(puzzle_input) // 2 + len(puzzle_input[0]) // 2 * 1j
    direction = -1 + 0j
    counter = 0

    for _ in range(10000):
        position, direction, infected, counter = burst(
            position, direction, infected, counter
        )

    return counter


def star_2(puzzle_input):
    """Solve second puzzle."""
    infected = load_infected(puzzle_input)
    sets = (set(), infected, set())
    position = len(puzzle_input) // 2 + len(puzzle_input[0]) // 2 * 1j
    direction = -1 + 0j
    counter = 0

    for _ in range(10000000):
        position, direction, sets, counter = evolved_burst(
            position, direction, sets, counter
        )

    return counter


def burst(position, direction, infected, counter):
    """Execute a burst."""
    direction *= -1j if position in infected else 1j

    if position in infected:
        infected.remove(position)

    else:
        infected.add(position)
        counter += 1

    return position + direction, direction, infected, counter


def evolved_burst(position, direction, sets, counter):
    """Execute an evolved burst."""
    weakened, infected, flagged = sets

    if position in weakened:
        weakened.remove(position)
        infected.add(position)
        counter += 1

    elif position in infected:
        direction *= -1j
        infected.remove(position)
        flagged.add(position)

    elif position in flagged:
        direction *= -1
        flagged.remove(position)

    else:
        direction *= 1j
        weakened.add(position)

    return (
        position + direction,
        direction,
        (weakened, infected, flagged),
        counter,
    )


def load_infected(puzzle_input):
    """Load infected nodes from input."""
    return {
        i + j * 1j
        for i, line in enumerate(puzzle_input)
        for j, node in enumerate(line)
        if node == "#"
    }


if __name__ == "__main__":
    main()
