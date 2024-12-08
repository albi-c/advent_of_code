from advent import Advent, Grid, ivec2


import itertools
from collections import defaultdict


positions: defaultdict[str, list[ivec2]] = defaultdict(list)
width = 0
height = 0
for y, ln in enumerate(Advent().read.lines()()):
    width = len(ln)
    height += 1
    for x, ch in enumerate(ln):
        if ch != ".":
            positions[ch].append(ivec2(x, y))


marked = set()
marked2 = set()
for poss in positions.values():
    for a, b in itertools.permutations(poss, r=2):
        pos = a - (b - a)
        if 0 <= pos.x < width and 0 <= pos.y < height:
            marked.add(pos)

        diff = b - a
        for i in itertools.count():
            pos = a - i * diff
            if not (0 <= pos.x < width and 0 <= pos.y < height):
                break
            marked2.add(pos)

print(len(marked))
print(len(marked2))
