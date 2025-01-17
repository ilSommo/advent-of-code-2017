"""Day 12: Digital Plumber"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

from collections import deque


def main():
    """Solve day 12 puzzles."""
    with open("data/day_12.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    programs = load_programs(puzzle_input)
    group = get_group(programs, 0)

    return len(group)


def star_2(puzzle_input):
    """Solve second puzzle."""
    programs = load_programs(puzzle_input)
    groups = 0

    while programs:
        group = get_group(programs, list(programs)[0])
        groups += 1

        for program in group:
            del programs[program]

    return groups


def get_group(programs, program):
    """Get group connected with program."""
    group = {program}
    queue = deque([program])

    while queue:
        program = queue.popleft()

        for connected in programs[program]:
            if connected not in group:
                group.add(connected)
                queue.append(connected)

    return group


def load_programs(puzzle_input):
    """Load programs from input."""
    programs = {}

    for line in puzzle_input:
        program, connected_programs = line.split(" <-> ")
        programs[int(program)] = set(
            int(connected) for connected in connected_programs.split(", ")
        )

    return programs


if __name__ == "__main__":
    main()
