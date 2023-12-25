from advent import Advent, vec2

import numpy as np
import sympy
import glm
from dataclasses import dataclass
import itertools
from fractions import Fraction


@dataclass
class ivec3:
    x: int
    y: int
    z: int


@dataclass
class ray3:
    s: ivec3
    d: ivec3


def parse_line(ln: str) -> ray3:
    spl = ln.replace(" ", "").split("@")
    return ray3(ivec3(*map(int, spl[0].split(","))), ivec3(*map(int, spl[1].split(","))))


data: list[ray3] = Advent().read.lines().map(parse_line)()

# bounds = (7, 21)
bounds = (200000000000000, 400000000000000)

intersections = 0
for a, b in itertools.combinations(data, 2):
    d = a.d.x * b.d.y - a.d.y * b.d.x
    if d == 0:
        continue
    t = Fraction((b.s.x - a.s.x) * b.d.y - (b.s.y - a.s.y) * b.d.x, d)
    u = Fraction((b.s.x - a.s.x) * a.d.y - (b.s.y - a.s.y) * a.d.x, d)
    if (t >= 0 and u >= 0 and bounds[0] <= a.s.x + t * a.d.x <= bounds[1] and
            bounds[0] <= a.s.y + t * a.d.y <= bounds[1]):
        intersections += 1
print(intersections)


array = np.array([line.replace(" ", "").replace("@", ",").split(",") for line in Advent().read.lines()()], int)
p, v, t = (sympy.symbols(f"{ch}(:3)") for ch in "pvt")
equations = [
    array[i, j] + t[i] * array[i, 3 + j] - p[j] - v[j] * t[i]
    for i in range(3) for j in range(3)
]
print(sum(sympy.solve(equations, (*p, *v, *t))[0][:3]))
