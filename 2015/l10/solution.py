from advent import Advent

import itertools

advent = Advent()

data = advent.read()

def apply(s: str) -> str:
    n = ""
    for ch, l in ((c, len(list(g))) for c, g in itertools.groupby(s)):
        n += str(l)
        n += ch
    return n

d = data
for _ in range(40):
    d = apply(d)
print(len(d))

for _ in range(10):
    d = apply(d)
print(len(d))
