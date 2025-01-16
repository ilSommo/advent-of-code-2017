"""Day 4: High-Entropy Passphrases"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

import itertools


def main():
    """Solve day 4 puzzles."""
    with open("data/day_4.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    valid = len(puzzle_input)

    for phrase in puzzle_input:
        for word_0, word_1 in itertools.combinations(phrase.split(), 2):
            if word_0 == word_1:
                valid -= 1
                break

    return valid


def star_2(puzzle_input):
    """Solve second puzzle."""
    valid = len(puzzle_input)

    for phrase in puzzle_input:
        for word_0, word_1 in itertools.combinations(phrase.split(), 2):
            if sorted(word_0) == sorted(word_1):
                valid -= 1
                break

    return valid


if __name__ == "__main__":
    main()
