from ..advent import Advent, Grid

s_value = 1000
e_value = ord("z") - ord("a") + 1

advent = Advent(12)

grid = advent.read.grid(lambda ch: s_value if ch == "S" else e_value if ch == "E" else ord(ch) - ord("a"))

start = (0, 0)
end = (0, 0)

for k, v in grid.items():
    if v == s_value:
        start = k
    if v == e_value:
        end = k


vertices = set()
distance = {}
previous = {}

for k, _ in grid.items():
    distance[k] = 1 << 30
    previous[k] = None
    vertices.add(k)

distance[start] = 0

while len(vertices) > 0:
    u = min(vertices, key=lambda x: distance[x])
    vertices.remove(u)

    for n, v in grid.neighbors(u):
        if v > grid[u] + 1:
            continue

        if n in vertices:
            alt = distance[u] + 1
            if alt < distance[n]:
                distance[n] = alt
                previous[n] = u


advent.solution(distance[end])
