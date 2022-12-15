from ..advent import Advent, vec2

from itertools import chain

advent = Advent(15)

SEARCH_RANGE = 4000000  # 20 for test input
SIGNAL_MULTIPLY = 4000000

data = advent.read.lines(lambda ln:
                         [vec2(int(part.split("=")[1].split(",")[0]),
                               int(part.split("=")[2])) for part in ln.split(": ")])

for pair in data:
    pair.append(pair[0].manhattan(pair[1]))


def check(pos: vec2):
    if pos.x < 0 or pos.y < 0 or pos.x > SEARCH_RANGE or pos.y > SEARCH_RANGE:
        return

    for se, _, si in data:
        if pos.manhattan(se) < si:
            return

    advent.solution(p.x * SIGNAL_MULTIPLY + p.y)


for sensor, _, size in data:
    p = vec2(sensor.x, sensor.y - size - 1)
    check(p)
    while p.y != sensor.y:
        p.x += 1
        p.y += 1
        check(p)
    while p.x != sensor.x:
        p.x -= 1
        p.y += 1
        check(p)
    while p.y != sensor.y:
        p.x -= 1
        p.y -= 1
        check(p)
    while p.x != sensor.x:
        p.x += 1
        p.y -= 1
        check(p)
