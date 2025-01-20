"""Day 16: Permutation Promenade"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

from functools import cache

N_CYCLES = 1000000000
N_PROGRAMS = 16


def main():
    """Solve day 16 puzzles."""
    with open("data/day_16.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.read().rstrip()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    moves = puzzle_input.split(",")
    programs = [chr(97 + i) for i in range(N_PROGRAMS)]

    return "".join(dance_full(programs, moves))


def star_2(puzzle_input):
    """Solve second puzzle."""
    moves = puzzle_input.split(",")
    programs = [chr(97 + i) for i in range(N_PROGRAMS)]
    states = [programs]

    for _ in range(N_CYCLES):
        programs = dance_full(programs, moves)

        if programs in states:
            break

        states.append(programs)

    i = states.index(programs)
    print(len(states))

    return "".join(states[(N_CYCLES - i) % (len(states) - i)])


@cache
def dance(programs, move):
    """Perform a single dance movement."""
    programs = list(programs)

    match move[0]:
        case "s":
            x = int(move[1:]) % len(programs)
            return programs[-x:] + programs[:-x]

        case "x":
            a, b = (int(position) for position in move[1:].split("/"))

        case "p":
            a, b = (programs.index(program) for program in move[1:].split("/"))

    programs[a], programs[b] = programs[b], programs[a]

    return programs


def dance_full(programs, moves):
    """Perform a full dance routine."""
    for move in moves:
        programs = dance(tuple(programs), move)

    return programs


if __name__ == "__main__":
    main()
