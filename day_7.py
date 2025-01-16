"""Day 7: Recursive Circus"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

from collections import Counter


def main():
    """Solve day 7 puzzles."""
    with open("data/day_7.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    graph = load_graph(puzzle_input)
    leaves = [leaf for v in graph.values() for leaf in v[1]]

    for node in graph:
        if node not in leaves:
            return node

    return None


def star_2(puzzle_input):
    """Solve second puzzle."""
    graph = load_graph(puzzle_input)
    weighted_graph = compute_weights(graph)
    bad_node = get_bad_node(weighted_graph, star_1(puzzle_input))

    for v in graph.values():
        if bad_node in v[1]:
            return (
                (
                    weighted_graph[v[1][1]][0]
                    if bad_node == v[1][0]
                    else weighted_graph[v[1][0]][0]
                )
                + graph[bad_node][0]
                - weighted_graph[bad_node][0]
            )

    return None


def compute_weight(node, graph):
    """Compute weight of a node."""
    weight = graph[node][0]

    if graph[node][1]:
        weight += sum(compute_weight(leaf, graph) for leaf in graph[node][1])

    return weight


def compute_weights(graph):
    """Compute total weights for all nodes of graph."""
    new_graph = {}

    for node in graph:
        new_graph[node] = (compute_weight(node, graph), graph[node][1])

    return new_graph


def get_bad_node(graph, bad_node):
    """Get bad node."""
    while True:
        weights = tuple(graph[leaf][0] for leaf in graph[bad_node][1])
        odd_weight = Counter(weights).most_common()[-1][0]

        for node in graph[bad_node][1]:
            if graph[node][0] == odd_weight:
                nodes = graph[node][1]

                if graph[nodes[0]][0] == sum(
                    graph[node_][0] for node_ in nodes
                ) // len(nodes):
                    return node

                bad_node = node
                break


def load_graph(puzzle_input):
    """Load programs graph from input."""
    graph = {}

    for line in puzzle_input:
        chunks = line.split(" -> ")
        program, weight = chunks[0][:-1].split(" (")
        dependencies = tuple() if len(chunks) == 1 else chunks[1].split(", ")
        graph[program] = (int(weight), dependencies)

    return graph


if __name__ == "__main__":
    main()
