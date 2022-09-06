from ..advent import Advent

advent = Advent(12, 1)

data = advent.read.lines(lambda x: x.split("-"))

caves = {}

for k, v in data:
    caves[k] = set()
    caves[v] = set()

for k, v in data:
    caves[k].add(v)
    caves[v].add(k)

def find_paths(caves: dict, pos: str, visited: set, end: str = "end"):
    for cave in caves[pos]:
        if cave == end:
            yield [pos, end]

            continue

        if cave.islower() and cave in visited:
            continue

        for path in find_paths(caves, cave, visited | {pos}, end):
            yield [pos] + path

paths = list(find_paths(caves, "start", {"start"}))
npaths = []

for path in paths:
    for i, cave in enumerate(path[1:-1]):
        if cave.islower():
            for loop in find_paths(caves, cave, set(path), cave):
                p = path.copy()
                for j, c in enumerate(loop):
                    p.insert(1 + i + j, c)
                npaths.append(p)

paths += npaths

advent.solution(len(paths))
