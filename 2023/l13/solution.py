from advent import Advent, Stream


advent = Advent()


Grid = tuple[tuple[bool, ...], ...]


def rotate_grid(grid: Grid) -> Grid:
    return tuple(zip(*grid))


def parse_block(block: str) -> tuple[Grid, Grid]:
    grid = tuple(tuple(ch == "#" for ch in row) for row in block.splitlines())
    return grid, rotate_grid(grid)


def get_reflection(grid: Grid) -> int:
    for i, row in Stream(grid).enumerate().slice(len(grid) - 1):
        if all(grid[a] == grid[b] for a, b in zip(range(i + 1, len(grid)), range(i, -1, -1))):
            return i + 1

    return 0


def check_smudge(a: tuple[int, ...], b: tuple[int, ...]) -> int:
    return sum(x - y != 0 for x, y in zip(a, b))


def get_reflection_2(grid: Grid) -> int:
    for i, row in Stream(grid).enumerate().slice(len(grid) - 1):
        if sum(check_smudge(grid[a], grid[b]) for a, b in zip(range(i + 1, len(grid)), range(i, -1, -1))) == 1:
            return i + 1

    return 0


data: list[tuple[Grid, Grid]] = advent.read.blocks().map(parse_block)()


print(sum(get_reflection(a) * 100 + get_reflection(b) for a, b in data))

print(sum(get_reflection_2(a) * 100 + get_reflection_2(b) for a, b in data))
