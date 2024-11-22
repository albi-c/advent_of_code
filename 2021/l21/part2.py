from ..advent import Advent, vec2

import itertools
import functools

advent = Advent(21, 2)

p1, p2 = advent.read.lines(lambda x: int(x.split(" ")[-1]))

ROLLS = tuple(map(sum, itertools.product((1, 2, 3), repeat=3)))


@functools.cache
def rolls(turn: int, p: tuple[int, int], s: tuple[int, int]) -> vec2:
    return sum((roll(r, turn, p, s) for r in ROLLS), start=vec2())


@functools.cache
def roll(n: int, turn: int, p: tuple[int, int], s: tuple[int, int]) -> vec2:
    player = list(p)
    player[turn] += n
    player[turn] = (player[turn] - 1) % 10 + 1
    score = list(s)
    score[turn] += player[turn]
    
    if score[turn] >= 21:
        return vec2(turn, 1 - turn)
    
    return rolls(1 - turn, tuple(player), tuple(score))


wins = rolls(0, (p1, p2), (0, 0))
advent.solution(max(wins.x, wins.y))
