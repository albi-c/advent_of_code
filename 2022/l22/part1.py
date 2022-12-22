from ..advent import Advent, vec2

advent = Advent(22)

TILES = {
    " ": 0,
    "#": 1,
    ".": -1
}

DIRECTIONS = [
    vec2(1, 0),
    vec2(0, 1),
    vec2(-1, 0),
    vec2(0, -1)
]

raw_map, raw_moves = advent.read.blocks()

m: list[tuple[list[int], int, int]] = [([TILES[t] for t in ln], ln.count(" "), len(ln)) for ln in raw_map.splitlines()]

moves: list[str] = []
move = ""
for ch in raw_moves:
    if ch in "RL":
        if move:
            moves.append(move)
            move = ""
        moves.append(ch)
    else:
        move += ch
if move:
    moves.append(move)


def get(position: vec2) -> int:
    if position.y < 0 or position.x < 0 or position.y >= len(m) or position.x >= m[position.y][2]:
        return 0

    return m[position.y][0][position.x]


def wrap(coord: int, direction: int) -> tuple[int, vec2]:
    if direction & 1:
        pos = vec2(
            coord,
            0 if direction == 1 else len(m) - 1
        )

    else:
        pos = vec2(
            0 if direction == 0 else m[coord][2] - 1,
            coord
        )

    while not (t := get(pos)):
        pos += DIRECTIONS[direction]

    return t, pos


p = vec2(m[0][1], 0)
d = 0

for move in moves:
    if move in "RL":
        d = (d + (1 if move == "R" else -1)) % 4

    else:
        for _ in range(int(move)):
            t = get(p + DIRECTIONS[d])
            if t == 1:
                break
            elif t == -1:
                p += DIRECTIONS[d]
            else:
                t, np = wrap(p.x if d & 1 else p.y, d)
                if t == 1:
                    break
                elif t == -1:
                    p = np
                else:
                    raise RuntimeError("Invalid wrap-around")

advent.solution((p.y + 1) * 1000 + (p.x + 1) * 4 + d)
