"""Day 18: Duet"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

from collections import defaultdict, deque


def main():
    """Solve day 18 puzzles."""
    with open("data/day_18.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    registers = defaultdict(int)
    sound = 0
    i = 0

    while i < len(puzzle_input):
        i, registers, sound, recover = execute_instruction(
            i, puzzle_input[i], registers, sound
        )

        if recover:
            break

    return sound


def star_2(puzzle_input):
    """Solve second puzzle."""
    registers_0 = defaultdict(lambda: 0)
    registers_1 = defaultdict(lambda: 1)
    queue_0_to_1 = deque()
    queue_1_to_0 = deque()
    i = j = 0
    counter = 0

    while i < len(puzzle_input) or j < len(puzzle_input):
        if queue_1_to_0 or not "rcv" in puzzle_input[i]:
            i, registers_0, queue_1_to_0, queue_0_to_1 = (
                execute_instruction_parallel(
                    i, puzzle_input[i], registers_0, queue_1_to_0, queue_0_to_1
                )
            )

        if queue_0_to_1 or not "rcv" in puzzle_input[j]:
            queue_1_to_0_old = queue_1_to_0.copy()
            j, registers_1, queue_0_to_1, queue_1_to_0 = (
                execute_instruction_parallel(
                    j, puzzle_input[j], registers_1, queue_0_to_1, queue_1_to_0
                )
            )

            if queue_1_to_0 != queue_1_to_0_old:
                counter += 1

        if (
            "rcv" in puzzle_input[i]
            and "rcv" in puzzle_input[j]
            and not queue_0_to_1
            and not queue_1_to_0
        ):
            break

    return counter


def execute_instruction(i, instruction, registers, sound):
    """Execute a single instruction."""
    chunks = instruction.split()
    recover = False
    i += 1

    match chunks[0]:
        case "snd":
            sound = registers[chunks[1]]

        case "set":
            registers[chunks[1]] = get_value(chunks[2], registers)

        case "add":
            registers[chunks[1]] += get_value(chunks[2], registers)

        case "mul":
            registers[chunks[1]] *= get_value(chunks[2], registers)

        case "mod":
            registers[chunks[1]] %= get_value(chunks[2], registers)

        case "rcv":
            if get_value(chunks[1], registers):
                recover = True

        case "jgz":
            if get_value(chunks[1], registers) > 0:
                i += get_value(chunks[2], registers) - 1

    return i, registers, sound, recover


def execute_instruction_parallel(
    i, instruction, registers, queue_in, queue_out
):
    """Execute a single parallel instruction."""
    chunks = instruction.split()
    i += 1

    match chunks[0]:
        case "snd":
            queue_out.append(get_value(chunks[1], registers))

        case "rcv":
            registers[chunks[1]] = queue_in.popleft()

        case _:
            i -= 1
            i, registers, _, _ = execute_instruction(
                i, instruction, registers, None
            )

    return i, registers, queue_in, queue_out


def get_value(x, registers):
    """Get value of register or of integer."""
    return registers[x] if x.islower() else int(x)


if __name__ == "__main__":
    main()
