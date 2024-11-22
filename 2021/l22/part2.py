from __future__ import annotations

from advent import Advent


# on, x1, x2, y1, y2, z1, z2
type Cube = tuple[bool, int, int, int, int, int, int]


def parse_line(ln: str) -> Cube:
    state, ln = ln.split(" ")
    on = state == "on"
    x, y, z = (tuple(int(n) for n in part[2:].split("..")) for part in ln.split(","))
    return on, x[0], x[1], y[0], y[1], z[0], z[1]


def intersect(a: Cube, b: Cube) -> Cube | None:
    x1, x2 = max(a[1], b[1]), min(a[2], b[2])
    y1, y2 = max(a[3], b[3]), min(a[4], b[4])
    z1, z2 = max(a[5], b[5]), min(a[6], b[6])
    if x1 > x2 or y1 > y2 or z1 > z2:
        return None
    return not b[0], x1, x2, y1, y2, z1, z2


data = Advent().read.lines().map(parse_line)()

cubes = []
for cube in data:
    new = [cube] if cube[0] else []
    for c in cubes:
        i = intersect(cube, c)
        if i is not None:
            new.append(i)
    cubes += new

enabled = 0
for cube in cubes:
    enabled += (1 if cube[0] else -1) * (cube[2] - cube[1] + 1) * (cube[4] - cube[3] + 1) * (cube[6] - cube[5] + 1)
print(enabled)
