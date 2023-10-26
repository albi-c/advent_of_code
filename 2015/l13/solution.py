from advent import Advent, Util

import itertools
from collections import defaultdict

advent = Advent()

data = [(ln[0][0], (1 if ln[2] == "gain" else -1) * int(ln[3]), ln[-1][0]) for ln in advent.read.lines().split(" ")()]

sitting: dict[str, dict[str, int]] = defaultdict(dict)

for a, g, b in data:
    sitting[a][b] = g

def calc_gain(people: tuple[str, ...]) -> int:
    return sum(sitting[x][y] + sitting[y][x] for x, y in Util.window(people, 2)) \
           + sitting[people[0]][people[-1]]  + sitting[people[-1]][people[0]]

gain = -(1 << 20)
for p in itertools.permutations(sitting.keys()):
    gain = max(gain, calc_gain(p))
print(gain)

sitting["Me"] = {p: 0 for p in sitting.keys()}
for p in sitting.values():
    p["Me"] = 0

gain = -(1 << 20)
for p in itertools.permutations(sitting.keys()):
    gain = max(gain, calc_gain(p))
print(gain)
