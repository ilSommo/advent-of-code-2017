"""Day 9: Stream Processing"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

import re


def main():
    """Solve day 9 puzzles."""
    with open("data/day_9.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.read().rstrip()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    string = re.sub(r"!.", "", puzzle_input)
    string = re.sub(r"<[^>]*>", "", string)
    string = re.sub(r"[^{}]", "", string)
    total = 0
    depth = 0

    for char in string:
        if char == "{":
            depth += 1

        else:
            total += depth
            depth -= 1

    return total


def star_2(puzzle_input):
    """Solve second puzzle."""
    string = re.sub(r"!.", "", puzzle_input)
    matches = re.findall(r"(?<=<)[^>]*(?=>)", string)

    return sum(len(match_) for match_ in matches)


if __name__ == "__main__":
    main()
