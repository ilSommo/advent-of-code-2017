"""Day 20: Particle Swarm"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

import itertools
import re
from collections import defaultdict, namedtuple
from functools import cache

Particle = namedtuple("Particle", ["p", "v", "a"])


def main():
    """Solve day 20 puzzles."""
    with open("data/day_20.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    particles = load_particles(puzzle_input)
    min_acceleration = float("inf")
    closest_particle = 0

    for i, particle in enumerate(particles):
        abs_acceleration = sum(abs(component) for component in particle.a)

        if abs_acceleration < min_acceleration:
            min_acceleration = abs_acceleration
            closest_particle = i

    return closest_particle


def star_2(puzzle_input):
    """Solve second puzzle."""
    particles = load_particles(puzzle_input)
    collisions = defaultdict(list)

    for i_0, i_1 in itertools.combinations(range(len(particles)), 2):
        p_0 = particles[i_0]
        p_1 = particles[i_1]

        a = (p_1.a[0] - p_0.a[0]) / 2
        b = (p_1.v[0] - p_0.v[0]) + (p_1.a[0] - p_0.a[0]) / 2
        c = p_1.p[0] - p_0.p[0]

        if a == 0 and b != 0:
            t_0 = t_1 = int(-c / b)
        elif a != 0 and b**2 - 4 * a * c >= 0:
            t_0 = int((-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a))
            t_1 = int((-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a))
        else:
            continue

        if t_0 >= 0 and compute_step(p_0, t_0) == compute_step(p_1, t_0):
            collisions[t_0].append((i_0, i_1))
        elif t_1 >= 0 and compute_step(p_0, t_1) == compute_step(p_1, t_1):
            collisions[t_1].append((i_0, i_1))

    destroyed = set()

    for _, collision in sorted(collisions.items()):
        new_destroyed = set()

        for p_0, p_1 in collision:
            if not (p_0 in destroyed or p_1 in destroyed):
                new_destroyed.update({p_0, p_1})

        destroyed.update(new_destroyed)

    return len(particles) - len(destroyed)


@cache
def compute_step(particle, time):
    """Compute the position of a particle at a given time."""
    return tuple(
        particle.p[i]
        + particle.v[i] * time
        + particle.a[i] * time * (time + 1) // 2
        for i in range(3)
    )


def load_particles(puzzle_input):
    """Import particles from input."""
    particles = []

    for line in puzzle_input:
        coordinates = re.findall(r"(?<=<)[^>]*(?=>)", line)
        p = tuple(int(coordinate) for coordinate in coordinates[0].split(","))
        v = tuple(int(coordinate) for coordinate in coordinates[1].split(","))
        a = tuple(int(coordinate) for coordinate in coordinates[2].split(","))
        particles.append(Particle(p, v, a))

    return tuple(particles)


if __name__ == "__main__":
    main()
