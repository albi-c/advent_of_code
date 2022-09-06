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

def find_paths(caves: dict, pos: str, visited: set):
    for cave in caves[pos]:
        if cave == "end":
            yield [pos, "end"]

            continue

        if cave.islower() and cave in visited:
            continue

        for path in find_paths(caves, cave, visited | {pos}):
            yield [pos] + path

advent.solution(len(list(find_paths(caves, "start", {"start"}))))
