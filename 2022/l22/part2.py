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


if advent.is_test:
    def get_face(pos: vec2) -> int:
        x, y = pos.x, pos.y
        if x < 4:
            return 1
        elif x < 8:
            return 2
        elif x > 11:
            return 5
        else:
            if y < 4:
                return 0
            elif y < 8:
                return 3
            return 4

    WRAP = [
        [
            lambda pos: vec2(16, 11 - pos.y),
            lambda pos: vec2(pos.x, 4),
            lambda pos: vec2(pos.y + 4, 4),
            lambda pos: vec2(8 - pos.x, 4),
            lambda d_: 3 if d_ == 0 else 1
        ],
        [
            lambda pos: vec2(4, pos.y),
            lambda pos: vec2(11 - pos.x, 11),
            lambda pos: vec2(19 - pos.y, 11),
            lambda pos: vec2(11 - pos.x, 0),
            lambda d_: 0 if d_ == 0 else 1 if d_ == 3 else 3
        ],
        [
            lambda pos: vec2(8, pos.y),
            lambda pos: vec2(8, 15 - pos.x),
            lambda pos: vec2(3, pos.y),
            lambda pos: vec2(8, pos.x - 4),
            lambda d_: 0 if d_ & 1 else d_
        ],
        [
            lambda pos: vec2(19 - pos.y, 8),
            lambda pos: vec2(pos.x, 8),
            lambda pos: vec2(7, pos.y),
            lambda pos: vec2(pos.x, 3),
            lambda d_: 1 if d_ == 0 else d_
        ],
        [
            lambda pos: vec2(12, pos.y),
            lambda pos: vec2(11 - pos.x, 7),
            lambda pos: vec2(15 - pos.y, 7),
            lambda pos: vec2(pos.x, 7),
            lambda d_: 3 if d_ in (1, 2) else d_
        ],
        [
            lambda pos: vec2(11, 11 - pos.y),
            lambda pos: vec2(0, 19 - pos.x),
            lambda pos: vec2(11, pos.y),
            lambda pos: vec2(11, 19 - pos.x),
            lambda d_: 0 if d_ == 1 else 2
        ]
    ]

else:
    def get_face(pos: vec2) -> int:
        x, y = pos.x, pos.y
        if x < 50:
            return 3 if y < 150 else 5
        elif x < 100:
            if y < 50:
                return 0
            elif y < 100:
                return 2
            return 4
        return 1

    WRAP = [
        [
            lambda pos: vec2(100, pos.y),
            lambda pos: vec2(pos.x, 50),
            lambda pos: vec2(0, 149 - pos.y),
            lambda pos: vec2(0, pos.x + 100),
            lambda d_: 1 if d_ == 1 else 0
        ],
        [
            lambda pos: vec2(99, 149 - pos.y),
            lambda pos: vec2(99, pos.x - 50),
            lambda pos: vec2(99, pos.y),
            lambda pos: vec2(pos.x - 100, 199),
            lambda d_: 3 if d_ == 3 else 2
        ],
        [
            lambda pos: vec2(pos.y + 50, 49),
            lambda pos: vec2(pos.x, 100),
            lambda pos: vec2(pos.y - 50, 100),
            lambda pos: vec2(pos.x, 49),
            lambda d_: 1 if d_ in (1, 2) else 3
        ],
        [
            lambda pos: vec2(50, pos.y),
            lambda pos: vec2(pos.x, 150),
            lambda pos: vec2(50, 149 - pos.y),
            lambda pos: vec2(50, pos.x + 50),
            lambda d_: 1 if d_ == 1 else 0
        ],
        [
            lambda pos: vec2(149, 149 - pos.y),
            lambda pos: vec2(49, pos.x + 100),
            lambda pos: vec2(49, pos.y),
            lambda pos: vec2(pos.x, 99),
            lambda d_: 3 if d_ == 3 else 2
        ],
        [
            lambda pos: vec2(pos.y - 100, 149),
            lambda pos: vec2(pos.x + 100, 0),
            lambda pos: vec2(pos.y - 100, 0),
            lambda pos: vec2(pos.x, 149),
            lambda d_: 1 if d_ in (1, 2) else 3
        ]
    ]


def wrap(pos: vec2, direction: int) -> tuple[int, vec2, int]:
    face = get_face(pos)
    new_pos = WRAP[face][direction](pos)
    return get(new_pos), new_pos, WRAP[face][4](direction)


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
                t, np, nd = wrap(p, d)
                if t == 1:
                    break
                elif t == -1:
                    p = np
                    d = nd
                else:
                    raise RuntimeError(f"Invalid wrap-around ({p} -> {np} | {d} -> {nd})")

advent.solution((p.y + 1) * 1000 + (p.x + 1) * 4 + d)
