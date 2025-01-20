"""Day 17: Spinlock"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"


def main():
    """Solve day 17 puzzles."""
    with open("data/day_17.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.read().rstrip()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    steps = int(puzzle_input)
    buffer = [0]
    position = 0

    for i in range(1, 2018):
        position = (position + steps) % i + 1
        buffer.insert(position, i)

    return buffer[position + 1]


def star_2(puzzle_input):
    """Solve second puzzle."""
    steps = int(puzzle_input)
    position = 0
    answer = 0

    for i in range(1, 50000001):
        position = (position + steps) % i + 1

        if position == 1:
            answer = i

    return answer


if __name__ == "__main__":
    main()
