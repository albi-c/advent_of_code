from advent import Advent, Grid, ivec2
from collections import defaultdict

coordinates: list[ivec2] = [ivec2(*ln) for ln in Advent().read.lines().split(",").map(int)()]
size = 71
target = ivec2(size, size) - 1


def pathfind(grid: Grid[bool], start: ivec2, end: ivec2) -> int:
    dist = defaultdict(lambda: 1 << 30)
    q = set()
    for pos, val in grid.enumerate():
        if not val:
            q.add(pos)
    dist[start] = 0
    while q:
        u = min(q, key=lambda pos: dist[pos])
        q.remove(u)
        for v in grid.neighbors(u):
            if grid[v] or v not in q:
                continue
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
                q.add(v)
    return dist[end]


def solve1(n):
    grid = Grid.of(False, size, size)
    for coord in coordinates[:n]:
        grid[coord] = True
    print(pathfind(grid, ivec2(0, 0), target))


def solve2():
    grid = Grid.of(False, size, size)
    for i, coord in enumerate(coordinates):
        grid[coord] = True
        # found with binary search by hand
        if i < 2990:
            continue
        if pathfind(grid, ivec2(0, 0), target) == 1 << 30:
            print(f"{coord.x},{coord.y}")
            break


solve1(1024)
solve2()
