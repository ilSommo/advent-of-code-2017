"""Day 19: A Series of Tubes"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"


def main():
    """Solve day 19 puzzles."""
    with open("data/day_19.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    lines, position = load_diagram(puzzle_input)
    direction = 1 + 0j
    letters = []

    while position in lines:
        position, direction, letters = execute_step(
            position, direction, lines, letters
        )

    return "".join(letters)


def star_2(puzzle_input):
    """Solve second puzzle."""
    lines, position = load_diagram(puzzle_input)
    direction = 1 + 0j
    counter = 0

    while position in lines:
        position, direction, _ = execute_step(position, direction, lines, [])
        counter += 1

    return counter


def execute_step(position, direction, lines, letters):
    """execute a single step."""
    char = lines[position]

    if char.isalpha():
        letters.append(char)

    elif char == "+":
        if position + direction * 1j in lines:
            direction *= 1j

        elif position + direction * -1j in lines:
            direction *= -1j

    return position + direction, direction, letters


def load_diagram(puzzle_input):
    """Load diagram from input."""
    lines = {}
    start = 0 + 0j

    for i, line in enumerate(puzzle_input):
        for j, char in enumerate(line):
            if char != " ":
                lines[i + j * 1j] = char

                if i == 0:
                    start = i + j * 1j

    return lines, start


if __name__ == "__main__":
    main()
