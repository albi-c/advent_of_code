from advent import Advent, ivec2

import sys


grid: list[list[str]] = [list(ln) for ln in Advent().read.lines()()]

grid_size = len(grid[0]), len(grid)


Pos = tuple[int, int]


def grid_get(p: Pos) -> str:
    return grid[p[1]][p[0]]


def pos_add(a: Pos, b: Pos) -> Pos:
    return a[0] + b[0], a[1] + b[1]


def propagate_light(state: set[tuple[Pos, Pos]], p: Pos, d: Pos):
    p = pos_add(p, d)

    if not (0 <= p[0] < grid_size[0] and 0 <= p[1] < grid_size[1]):
        return

    st = (p, d)
    if st in state:
        return
    state.add(st)

    ch = grid_get(p)
    if ch == "/":
        match d:
            case (1, 0):
                propagate_light(state, p, (0, -1))
            case (0, 1):
                propagate_light(state, p, (-1, 0))
            case (-1, 0):
                propagate_light(state, p, (0, 1))
            case (0, -1):
                propagate_light(state, p, (1, 0))
            case _:
                raise ValueError()
    elif ch == "\\":
        match d:
            case(1, 0):
                propagate_light(state, p, (0, 1))
            case(0, 1):
                propagate_light(state, p, (1, 0))
            case(-1, 0):
                propagate_light(state, p, (0, -1))
            case(0, -1):
                propagate_light(state, p, (-1, 0))
            case _:
                raise ValueError()
    elif ch == ".":
        propagate_light(state, p, d)
    elif ch == "-":
        match d:
            case (_, 0):
                propagate_light(state, p, d)
            case (0, _):
                propagate_light(state, p, (1, 0))
                propagate_light(state, p, (-1, 0))
            case _:
                raise ValueError()
    elif ch == "|":
        match d:
            case (_, 0):
                propagate_light(state, p, (0, 1))
                propagate_light(state, p, (0, -1))
            case (0, _):
                propagate_light(state, p, d)
            case _:
                raise ValueError()
    else:
        raise ValueError()


sys.setrecursionlimit(10000)


state_ = set()
propagate_light(state_, (-1, 0), (1, 0))

print(len(set(p for p, _ in state_)))

best = 0
for y in range(grid_size[1]):
    state_.clear()
    propagate_light(state_, (-1, y), (1, 0))
    best = max(best, len(set(p for p, _ in state_)))
    state_.clear()
    propagate_light(state_, (grid_size[0], y), (-1, 0))
    best = max(best, len(set(p for p, _ in state_)))
for x in range(grid_size[0]):
    state_.clear()
    propagate_light(state_, (x, -1), (0, 1))
    best = max(best, len(set(p for p, _ in state_)))
    state_.clear()
    propagate_light(state_, (x, grid_size[1]), (0, -1))
    best = max(best, len(set(p for p, _ in state_)))
print(best)
