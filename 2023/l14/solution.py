from advent import Advent, ivec2


advent = Advent()

data = [[1 if ch == "O" else 2 if ch == "#" else 0 for ch in ln] for ln in advent.read.lines()()]


grid_ = {ivec2(x, y): val for y, row in enumerate(data) for x, val in enumerate(row)}


def move(grid: dict[ivec2, int], dirs: tuple[ivec2, ...]) -> dict[ivec2, int]:
    for d in dirs:
        moved = True
        while moved:
            moved = False

            for pos in grid.keys():
                pos = ivec2(pos)
                while pos + d in grid and grid[pos] == 1 and grid[pos + d] == 0:
                    grid[pos] = 0
                    grid[pos + d] = 1
                    moved = True
                    pos += d

    return grid


def get_weight(grid: dict[ivec2, int]) -> int:
    height = max(p.y for p in grid.keys())
    return sum(height - p.y + 1 for p, v in grid.items() if v == 1)


print(get_weight(move(grid_.copy(), (ivec2(0, -1),))))


seen = {}
i = 0
count = 1000000000
while True:
    state = "".join(map(str, grid_.values()))
    if state in seen:
        p = seen[state]
        if (count - p) % (i - p) == 0:
            break
    seen[state] = i
    grid_ = move(grid_, (ivec2(0, -1), ivec2(-1, 0), ivec2(0, 1), ivec2(1, 0)))
    i += 1
print(get_weight(grid_))
