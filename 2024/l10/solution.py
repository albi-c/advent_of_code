from advent import Advent, Grid, ivec2


grid = Grid(Advent().read(), int)


def find_paths(pos: ivec2) -> set[ivec2]:
    if grid[pos] == 9:
        return {pos}

    paths = set()
    for p in grid.neighbors(pos, False):
        if grid[p] == grid[pos] + 1:
            paths |= find_paths(p)
    return paths


def find_distinct_paths(pos: ivec2, path: tuple[ivec2, ...]) -> set[tuple[ivec2, ...]]:
    if grid[pos] == 9:
        return {path}

    paths = set()
    for p in grid.neighbors(pos, False):
        if grid[p] == grid[pos] + 1:
            paths |= find_distinct_paths(p, path + (p,))
    return paths


score = 0
score2 = 0
for x in range(grid.width):
    for y in range(grid.height):
        if grid[x, y] == 0:
            score += len(find_paths(ivec2(x, y)))
            score2 += len(find_distinct_paths(ivec2(x, y), ()))
print(score)
print(score2)
