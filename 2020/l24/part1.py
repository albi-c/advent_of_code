from advent import Advent

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
print(len(black_tiles))
