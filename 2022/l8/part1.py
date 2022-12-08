from ..advent import Advent, Grid

advent = Advent(8)

data = advent.read.grid(int)


def test_visibility(grid: Grid) -> Grid:
    vis = Grid([[0 for _ in range(grid.width)] for _ in range(grid.height)])

    maximums = [-1 for _ in range(grid.width)]
    for y in range(grid.height):
        for x, h in enumerate(grid[y, 0:]):
            if h > maximums[x]:
                vis[x, y] = 1

        maximums = [max(a, b) for a, b in zip(grid[y, 0:], maximums)]

    maximums = [-1 for _ in range(grid.width)]
    for y in range(grid.height):
        y = grid.height - y - 1
        for x, h in enumerate(grid[y, 0:]):
            if h > maximums[x]:
                vis[x, y] = 1

        maximums = [max(a, b) for a, b in zip(grid[y, 0:], maximums)]

    maximums = [-1 for _ in range(grid.height)]
    for x in range(grid.width):
        for y, h in enumerate(grid.col(x)):
            if h > maximums[y]:
                vis[x, y] = 1

        maximums = [max(a, b) for a, b in zip(grid.col(x), maximums)]

    maximums = [-1 for _ in range(grid.height)]
    for x in range(grid.width):
        x = grid.width - x - 1
        for y, h in enumerate(grid.col(x)):
            if h > maximums[y]:
                vis[x, y] = 1

        maximums = [max(a, b) for a, b in zip(grid.col(x), maximums)]

    return vis


advent.solution(sum(advent.util.flatten(test_visibility(data).data)))
