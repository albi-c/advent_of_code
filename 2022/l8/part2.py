from ..advent import Advent, Grid

advent = Advent(8)

data = advent.read.grid(int)


def best_visibility(grid: Grid) -> int:
    best = 0

    for x in range(grid.width):
        for y in range(grid.height):
            up = grid.col(x)[:y][::-1]
            up = next((i + 1 for i, h in enumerate(up) if h >= grid[x, y]), y)

            down = grid.col(x)[y+1:]
            down = next((i + 1 for i, h in enumerate(down) if h >= grid[x, y]), grid.height - y - 1)

            left = grid[y, 0:][:x][::-1]
            left = next((i + 1 for i, h in enumerate(left) if h >= grid[x, y]), x)

            right = grid[y, 0:][x+1:]
            right = next((i + 1 for i, h in enumerate(right) if h >= grid[x, y]), grid.width - x - 1)

            best = max(best, up * down * left * right)

    return best


advent.solution(best_visibility(data))
