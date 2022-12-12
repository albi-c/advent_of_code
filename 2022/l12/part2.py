from ..advent import Advent, Grid

e_value = ord("z") - ord("a") + 1

advent = Advent(12)

grid = advent.read.grid(lambda ch: 0 if ch == "S" else e_value if ch == "E" else ord(ch) - ord("a"))

starts = []
end = (0, 0)

for k, v in grid.items():
    if v == 0:
        starts.append(k)
    if v == e_value:
        end = k

distances = []
for i, start in enumerate(starts):
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

    distances.append(distance[end])

advent.solution(min(distances))
