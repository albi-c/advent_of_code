from advent import Advent

from collections import defaultdict
import sys
sys.setrecursionlimit(10000)


orbits = defaultdict(list)
connections = defaultdict(list)
for a, b in Advent().read.lines().map(lambda ln: ln.split(")"))():
    orbits[a].append(b)
    connections[a].append(b)
    connections[b].append(a)


def solve_1(obj: str, level: int) -> int:
    return level + sum(solve_1(o, level + 1) for o in orbits[obj])


def solve_2(obj: str, target: str, distance: int, visited: set[str]) -> int:
    if obj == target:
        return distance

    if obj in visited:
        return 1 << 30

    return min(solve_2(n, target, distance + 1, visited | {obj}) for n in connections[obj])


print(solve_1("COM", 0))
print(solve_2(connections["SAN"][0], connections["YOU"][0], 0, set()))
