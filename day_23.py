"""Day 23: Coprocessor Conflagration"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"


def main():
    """Solve day 23 puzzles."""
    with open("data/day_23.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    registers = {chr(i): 0 for i in range(97, 97 + 8)}
    counter = 0
    i = 0

    while 0 <= i < len(puzzle_input):
        counter += "mul" in puzzle_input[i]
        registers, i = execute_instruction(registers, puzzle_input, i)

    return counter


def star_2(puzzle_input):
    """Solve second puzzle."""
    registers = {chr(i): 0 for i in range(97, 97 + 8)}
    registers["a"] = 1
    i = 0

    while "set f" not in puzzle_input[i]:
        registers, i = execute_instruction(registers, puzzle_input, i)

    return sum(
        not is_prime(i)
        for i in range(
            registers["b"],
            registers["c"] + 1,
            -int(puzzle_input[-2].split()[-1]),
        )
    )


def execute_instruction(registers, instructions, i):
    """Execute an instructions."""
    chunks = instructions[i].split()
    i += 1

    match chunks[0]:
        case "set":
            registers[chunks[1]] = get_value(registers, chunks[2])

        case "sub":
            registers[chunks[1]] -= get_value(registers, chunks[2])

        case "mul":
            registers[chunks[1]] *= get_value(registers, chunks[2])

        case "jnz":
            i += (
                get_value(registers, chunks[2]) - 1
                if get_value(registers, chunks[1]) != 0
                else 0
            )

    return registers, i


def get_value(registers, string):
    """Get value of register of literal."""
    return registers[string] if string.islower() else int(string)


def is_prime(n):
    """Check if a number is prime"""
    for i in range(2, n // 2):
        if n % i == 0:
            return False

    return True


if __name__ == "__main__":
    main()
