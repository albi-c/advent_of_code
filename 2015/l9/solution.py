from __future__ import annotations

from advent import Advent

advent = Advent()


class Graph:
    nodes: dict[str, Node]

    class Node:
        name: str
        connections: dict[Node, int]

        def __init__(self, name: str):
            self.name = name
            self.connections = {}

        def connect(self, other: Graph.Node, cost: int):
            self.connections[other] = cost
            other.connections[self] = cost

        def __hash__(self):
            return hash(self.name)

        def __eq__(self, other):
            if isinstance(other, Graph.Node):
                return self.name == other.name

            return NotImplemented

    def __init__(self):
        self.nodes = {}

    def __getitem__(self, name: str) -> Node:
        if name not in self.nodes:
            self.nodes[name] = Graph.Node(name)
        return self.nodes[name]


data = [(l[0].split(" to "), int(l[1])) for l in [ln.split(" = ") for ln in advent.read.lines()()]]

graph = Graph()
for [a, b], distance in data:
    graph[a].connect(graph[b], distance)

def find_shortest(node: Graph.Node, path: list[Graph.Node]) -> int | None:
    if len(path) == len(graph.nodes) - 1:
        return 0

    best = None
    for n, d in node.connections.items():
        if n in path:
            continue
        shortest = find_shortest(n, path + [node])
        if shortest is None:
            continue
        if best is None:
            best = d + shortest
        else:
            best = min(best, d + shortest)
    return best

def find_longest(node: Graph.Node, path: list[Graph.Node]) -> int | None:
    if len(path) == len(graph.nodes) - 1:
        return 0

    best = None
    for n, d in node.connections.items():
        if n in path:
            continue
        shortest = find_longest(n, path + [node])
        if shortest is None:
            continue
        if best is None:
            best = d + shortest
        else:
            best = max(best, d + shortest)
    return best

b = None
for node_ in graph.nodes.values():
    s = find_shortest(node_, [])
    if s is None:
        continue
    if b is None:
        b = s
    else:
        b = min(b, s)
print(b)

b = None
for node_ in graph.nodes.values():
    s = find_longest(node_, [])
    if s is None:
        continue
    if b is None:
        b = s
    else:
        b = max(b, s)
print(b)
