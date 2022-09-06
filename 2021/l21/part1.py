from ..advent import Advent

advent = Advent(21, 1)

p1, p2 = advent.read.lines(lambda x: int(x.split(" ")[-1]))
p1s, p2s = 0, 0

i = 1
while True:
    p1 += 3 * i + 3
    while p1 > 10:
        p1 -= 10
    
    p1s += p1

    p1, p2 = p2, p1
    p1s, p2s = p2s, p1s

    if p1s >= 1000 or p2s >= 1000:
        advent.solution(min(p1s, p2s) * (i + 2))
        break

    i += 3
