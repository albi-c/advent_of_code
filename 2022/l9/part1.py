from ..advent import Advent

from copy import copy

from glm import vec2

advent = Advent(9)

DIRECTIONS = {
    "R": vec2(1, 0),
    "L": vec2(-1, 0),
    "U": vec2(0, 1),
    "D": vec2(0, -1)
}

moves = advent.util.flatten([DIRECTIONS[ln[0]] for _ in range(int(ln[2:]))] for ln in advent.read.lines())

print(moves)
tail = vec2(0, 0)
head = vec2(0, 0)
positions = {vec2(0, 0)}
for move in moves:
    head += move
    if abs(head.x - tail.x) > 1 or abs(head.y - tail.y) > 1:
        diff = head - tail
        tail.x += diff.x // diff.x if diff.x else 0
        tail.y += diff.y // diff.y if diff.y else 0

    positions.add(copy(tail))

    print(move, head, tail)

advent.solution(len(positions))
