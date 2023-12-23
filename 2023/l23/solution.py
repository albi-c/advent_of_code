from advent import Advent

import sys
from dataclasses import dataclass


sys.setrecursionlimit(100000)


@dataclass(unsafe_hash=True)
class ivec2:
    x: int
    y: int

    def __add__(self, other):
        return ivec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return ivec2(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def copy(self):
        return ivec2(self.x, self.y)


DIRECTIONS = {
    ">": ivec2(1, 0),
    "<": ivec2(-1, 0),
    "^": ivec2(0, -1),
    "v": ivec2(0, 1)
}


grid: list[str] = Advent().read.lines()()
size = ivec2(len(grid[0]), len(grid))
start = ivec2(1, 0)
end = size - ivec2(2, 1)


def pathfind(pos: ivec2, seen: set[ivec2], distance: int, disable_slopes: bool) -> int:
    ch = grid[pos.y][pos.x]

    if ch == "#" or pos in seen:
        return 0

    if pos == end:
        return distance

    if disable_slopes or ch == ".":
        seen.add(pos)
        m = 0
        for d in DIRECTIONS.values():
            m = max(m, pathfind(pos + d, seen, distance + 1, disable_slopes))
        seen.remove(pos)
        return m
    else:
        seen.add(pos)
        m = pathfind(pos + DIRECTIONS[ch], seen, distance + 1, disable_slopes)
        seen.remove(pos)
        return m


print(pathfind(start, set(), 0, False))
print(pathfind(start, set(), 0, True))
