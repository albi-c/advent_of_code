from advent import Advent, ivec2

from collections import defaultdict

advent = Advent()

data = advent.read.lines()()

enabled = set()

for line in data:
    a, b, c = line.split(",")
    a_s = a.rsplit(" ", 1)
    op = a_s[0]
    b_s = b.split(" ")

    start = ivec2(int(a_s[1]), int(b_s[0]))
    end = ivec2(int(b_s[2]), int(c))

    for y in range(start.y, end.y + 1):
        for x in range(start.x, end.x + 1):
            if op == "turn on":
                enabled.add((x, y))
            elif op == "turn off":
                p = (x, y)
                if p in enabled:
                    enabled.remove(p)
            else:
                p = (x, y)
                if p in enabled:
                    enabled.remove(p)
                else:
                    enabled.add(p)

print(len(enabled))

brightnesses = defaultdict(int)

for line in data:
    a, b, c = line.split(",")
    a_s = a.rsplit(" ", 1)
    op = a_s[0]
    b_s = b.split(" ")

    start = ivec2(int(a_s[1]), int(b_s[0]))
    end = ivec2(int(b_s[2]), int(c))

    for y in range(start.y, end.y + 1):
        for x in range(start.x, end.x + 1):
            if op == "turn on":
                brightnesses[(x, y)] += 1
            elif op == "turn off":
                p = (x, y)
                brightnesses[p] = max(0, brightnesses[p] - 1)
            else:
                brightnesses[(x, y)] += 2

print(sum(brightnesses.values()))
