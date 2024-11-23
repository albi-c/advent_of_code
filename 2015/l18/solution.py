from advent import Advent, Grid


grid: Grid[bool] = Grid(Advent().read(), lambda ch: ch == "#")


def enable_corners(g: Grid[bool]):
    g[(0, 0)] = True
    g[(-1, 0)] = True
    g[(0, -1)] = True
    g[(-1, -1)] = True


def step(inp: Grid[bool], part: int) -> Grid[bool]:
    new = Grid([[False for _ in range(inp.width)] for _ in range(inp.height)])
    if part == 2:
        enable_corners(inp)
        enable_corners(new)
    for y in range(inp.height):
        for x in range(inp.width):
            pos = (x, y)
            neighbors = sum(inp[off] for off in inp.neighbors(pos, True))
            state = inp[pos]
            if state and (neighbors == 2 or neighbors == 3):
                new[pos] = True
            elif not state and neighbors == 3:
                new[pos] = True
    return new


grid_2 = grid

for _ in range(100):
    grid = step(grid, 1)
print(sum(grid))

for _ in range(100):
    grid_2 = step(grid_2, 2)
print(sum(grid_2))
