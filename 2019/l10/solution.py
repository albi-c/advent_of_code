from advent import Advent, Grid, ivec2, vec2

import math
import glm


grid = Grid(Advent().read(), lambda ch: 1 if ch == "#" else 0)


def step(a: ivec2, b: ivec2) -> ivec2:
    d = b - a
    return d // math.gcd(abs(d.x), abs(d.y))


def find_reachable(pos: ivec2, skip: set[ivec2] = None) -> list[ivec2]:
    reachable = []
    for x in range(grid.width):
        for y in range(grid.height):
            p = ivec2(x, y)
            if p == pos or (skip is not None and p in skip):
                continue
            if grid[p] == 1:
                off = step(pos, p)
                chk = pos + off
                hit = False
                while chk != p:
                    if grid[chk] == 1:
                        hit = True
                    chk += off
                if not hit:
                    reachable.append(p)
    return reachable


def solve() -> tuple[ivec2, list[ivec2]]:
    best = 0
    best_data = None
    for x in range(grid.width):
        for y in range(grid.height):
            pos = ivec2(x, y)
            if grid[pos] == 1:
                reachable = find_reachable(pos)
                if len(reachable) > best:
                    best = len(reachable)
                    best_data = pos, reachable
    return best_data


origin, asteroids = solve()
print(len(asteroids))


def angle(orig: ivec2, vec: ivec2) -> float:
    diff = vec - orig
    deg = math.atan2(-diff.y, diff.x) * 180 / math.pi
    if 0 <= deg <= 90:
        return abs(deg - 90)
    elif deg < 0:
        return abs(deg) + 90
    else:
        return 450 - deg


def solve_2() -> int:
    vaporized = sorted(asteroids, key=lambda asteroid: angle(origin, asteroid))
    while len(vaporized) < 200:
        a = find_reachable(origin, set(vaporized))
        if len(a) == 0:
            break
        vaporized += sorted(a, key=lambda asteroid: angle(origin, asteroid))
    return vaporized[199].x * 100 + vaporized[199].y


print(solve_2())
