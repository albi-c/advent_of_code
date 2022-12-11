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

segments = [vec2(0, 0) for _ in range(10)]
positions = {vec2(0, 0)}
for move in moves:
    segments[0] += move
    for s1, s2 in advent.util.pairs_overlay(segments):
        if abs(s1.x - s2.x) > 1 or abs(s1.y - s2.y) > 1:
            diff = s1 - s2
            s2.x += diff.x // abs(diff.x) if diff.x else 0
            s2.y += diff.y // abs(diff.y) if diff.y else 0

    positions.add(copy(segments[-1]))

advent.solution(len(positions))
