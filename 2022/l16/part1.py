from ..advent import Advent, Graph, GraphNode

advent = Advent(16)


class Valve(GraphNode):
    flow: int
    open: bool

    def __init__(self, name: str, rate: int):
        super().__init__(name)

        self.flow = rate
        self.open = False


valves = advent.read.lines(lambda ln: (Valve(ln[6:8], int(ln.split(";")[0].split("=")[1])),
                                       ln.split("valve")[1][1:].strip().split(", ")))


def make_graph(data: list[tuple[Valve, list[str]]]) -> Graph[Valve]:
    graph = Graph()

    for valve, _ in data:
        graph.add(valve)

    for valve, connections in data:
        for connection in connections:
            valve.connect(graph[connection])

    return graph


def remove_zero_nodes(graph: Graph[Valve]) -> Graph[Valve]:
    to_remove = set()

    for name, valve in graph.items():
        if valve.name == "AA":
            continue

        if valve.flow == 0:
            for conn, dist in valve.connections.items():
                for conn_, dist_ in valve.connections.items():
                    if conn == conn_ or conn.connected(conn_):
                        continue

                    conn.connect(conn_, dist + dist_)

            to_remove.add(name)

    for name in to_remove:
        del graph[name]

    return graph


def calc_distances(graph: Graph[Valve]) -> Graph[Valve]:
    changed = True

    while changed:
        changed = False

        connections = []

        for _, valve1 in graph.items():
            for valve2, cost2 in valve1.connections.items():
                for valve3, cost3 in valve2.connections.items():
                    if not valve1.connected(valve3):
                        if valve1 == valve3:
                            continue

                        connections.append((valve1, valve3, cost2 + cost3))
                        changed = True

        for v1, v2, c in connections:
            v1.connect(v2, c)

    return graph


def find_best(graph: Graph[Valve], curr: Valve, time: int) -> int:
    if time <= 1:
        return 0

    best = 0

    for _, valve in graph.items():
        if valve.flow == 0 or valve.open or valve == curr:
            continue

        valve.open = True

        rest = time - 1 - curr.connections[valve]
        best = max(best, valve.flow * rest + find_best(graph, valve, rest))

        valve.open = False

    return best


graph_ = calc_distances(remove_zero_nodes(make_graph(valves)))
advent.solution(find_best(graph_, graph_["AA"], 30))
