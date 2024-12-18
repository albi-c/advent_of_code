from advent import Advent, Grid, ivec2, pathfind_max_cost, dijkstra, find_threshold
from collections import defaultdict

coordinates: list[ivec2] = [ivec2(*ln) for ln in Advent().read.lines().split(",").map(int)()]
size = 71
target = ivec2(size, size) - 1


def pathfind(grid: Grid[bool]) -> int:
    return dijkstra(ivec2(0, 0), lambda p: (n for n in grid.neighbors(p) if not grid[n]), lambda u, v: 1)[0][target]


def solve(n: int) -> int:
    grid = Grid.of(False, size, size)
    for coord in coordinates[:n]:
        grid[coord] = True
    return pathfind(grid)


print(solve(1024))
result = coordinates[find_threshold(solve, pathfind_max_cost, 1024, len(coordinates) - 1) - 1]
print(f"{result.x},{result.y}")
