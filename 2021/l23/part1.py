from advent import Advent

import functools
from dataclasses import dataclass


NEIGHBORS_B2T = (2, 4, 6, 8)
TOP_ROW_TARGETS = tuple(i for i in range(11) if i not in NEIGHBORS_B2T)


@dataclass(frozen=True, slots=True)
class Amphipod:
    ch: str
    cost: int = None
    target: int = None

    def __post_init__(self):
        object.__setattr__(self, "cost", 10 ** (ord(self.ch) - ord('A')))
        object.__setattr__(self, "target", ord(self.ch) - ord('A'))

    def __hash__(self):
        return self.cost

    def __eq__(self, other):
        return isinstance(other, Amphipod) and self.cost == other.cost


class HashableSet[T](set[T]):
    def __hash__(self):
        return id(self)


data = tuple(tuple(Amphipod(ch) for ch in ln.strip("# ").split("#")) for ln in Advent().read.lines()()[2:4])


def tuple_with[T](t: tuple[T, ...], i: int, v: T) -> tuple[T, ...]:
    return t[:i] + (v,) + t[i+1:]


def tiles_to_top_row_neighbor(pos: int, target_room: int) -> int:
    return abs(pos - NEIGHBORS_B2T[target_room])


TopRow = tuple[Amphipod | None, ...]
Rows = tuple[tuple[Amphipod | None, ...], ...]
Position = tuple[TopRow, Rows]


def top_row_move(top_row: TopRow, pos: int, target: int) -> int | None:
    if target < pos:
        pos, target = target, pos
    if any(a is not None for a in top_row[pos:target+1]):
        return None
    return target - pos


@functools.cache
def solve(top_row: TopRow, rows: Rows, energy: int, seen: HashableSet[Position]) -> int:
    if all(all(a is not None and a.target == i for i, a in enumerate(row)) for row in rows):
        return energy

    position = (top_row, rows)
    if position in seen:
        return 1 << 30
    seen.add(position)

    best = 1 << 30

    for i, a in enumerate(top_row):
        if a is not None and rows[0][a.target] is None:
            if rows[1][a.target] is None:
                top_row_changed = tuple_with(top_row, i, None)
                if (cost := top_row_move(top_row_changed, i, NEIGHBORS_B2T[a.target])) is not None:
                    cost += 2
                    rows_changed = tuple_with(rows, 1, tuple_with(rows[1], a.target, a))
                    best = min(best, solve(top_row_changed, rows_changed, energy + a.cost * cost, seen))
            elif rows[1][a.target] == a:
                top_row_changed = tuple_with(top_row, i, None)
                if (cost := top_row_move(top_row_changed, i, NEIGHBORS_B2T[a.target])) is not None:
                    cost += 1
                    rows_changed = tuple_with(rows, 0, tuple_with(rows[0], a.target, a))
                    best = min(best, solve(top_row_changed, rows_changed, energy + a.cost * cost, seen))

    for i in range(4):
        if all(row[i] is not None and row[i].target == i for row in rows):
            continue

        pos = NEIGHBORS_B2T[i]

        if (a := rows[0][i]) is not None:
            for target in TOP_ROW_TARGETS:
                if (cost := top_row_move(top_row, pos, target)) is not None:
                    cost += 1
                    top_row_changed = tuple_with(top_row, target, a)
                    rows_changed = tuple_with(rows, 0, tuple_with(rows[0], i, None))
                    best = min(best, solve(top_row_changed, rows_changed, energy + a.cost * cost, seen))

        elif (a := rows[1][i]) is not None:
            for target in TOP_ROW_TARGETS:
                if (cost := top_row_move(top_row, pos, target)) is not None:
                    cost += 2
                    top_row_changed = tuple_with(top_row, target, a)
                    rows_changed = tuple_with(rows, 1, tuple_with(rows[1], i, None))
                    best = min(best, solve(top_row_changed, rows_changed, energy + a.cost * cost, seen))

    return best


print(solve(tuple(None for _ in range(11)), data, 0, HashableSet()))
