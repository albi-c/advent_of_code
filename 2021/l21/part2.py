from ..advent import Advent, vec2

import itertools, functools

advent = Advent(21, 2)

p1, p2 = advent.read.lines(lambda x: int(x.split(" ")[-1]))

ROLLS = tuple(map(sum, itertools.product((1, 2, 3), (1, 2, 3), (1, 2, 3))))

@functools.cache
def rolls(turn: int, p: tuple, s: tuple) -> vec2:
    return sum((roll(r, turn, p, s) for r in ROLLS), start=vec2())

@functools.cache
def roll(n: int, turn: int, p: tuple, s: tuple) -> vec2:
    player = list(p)
    player[turn] += n
    player[turn] %= 10
    score = list(s)
    score[turn] += player[turn] + 1
    
    if score[turn] >= 21:
        return vec2(turn, 1 - turn)
    
    return rolls(1 - turn, tuple(player), tuple(score))

wins = rolls(0, (p1, p2), (0, 0))

print(wins)
advent.solution(max(wins.x, wins.y))
