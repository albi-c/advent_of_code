from advent import Advent

NEIGHBORS = (
    (0, -1),
    (-1, 1),
    (-1, 0),
    (1, -1),
    (0, 1),
    (1, 0)
)


def v2a(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return a[0] + b[0], a[1] + b[1]


data: list[str] = Advent().read.lines()()


def get_pos(row: str) -> tuple[int, int]:
    x = 0
    y = 0

    prev = ""
    for ch in row:
        if ch == "w":
            if prev == "s":
                y -= 1
            elif prev == "n":
                x -= 1
                y += 1
            else:
                x -= 1
        elif ch == "e":
            if prev == "s":
                x += 1
                y -= 1
            elif prev == "n":
                y += 1
            else:
                x += 1
        prev = ch

    return x, y


black_tiles: set[tuple[int, int]] = set()
for r in data:
    pos = get_pos(r)
    if pos in black_tiles:
        black_tiles.remove(pos)
    else:
        black_tiles.add(pos)


def count_black_neighbors(tiles: set[tuple[int, int]], tile: tuple[int, int]) -> int:
    return sum(int(v2a(tile, offset) in tiles) for offset in NEIGHBORS)


def flip_tiles(tiles: set[tuple[int, int]]) -> set[tuple[int, int]]:
    result: set[tuple[int, int]] = set()
    white_visited: set[tuple[int, int]] = set()

    for tile in tiles:
        n = count_black_neighbors(tiles, tile)

        if 0 < n <= 2:
            result.add(tile)

        for offset in NEIGHBORS:
            tile_ = v2a(tile, offset)
            if tile_ not in white_visited and tile_ not in tiles:
                white_visited.add(tile_)
                if count_black_neighbors(tiles, tile_) == 2:
                    result.add(tile_)

    return result


for _ in range(100):
    black_tiles = flip_tiles(black_tiles)
print(len(black_tiles))
