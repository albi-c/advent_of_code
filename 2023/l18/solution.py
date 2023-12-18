from advent import Advent, ivec2

import itertools


DIRECTIONS = {
    "R": ivec2(1, 0),
    "L": ivec2(-1, 0),
    "D": ivec2(0, 1),
    "U": ivec2(0, -1)
}


HEX_DIRECTIONS = {
    "0": "R",
    "1": "D",
    "2": "L",
    "3": "U"
}


def parse_line(ln: str) -> tuple[str, int, int, str]:
    spl = ln.split()
    return spl[0], int(spl[1]), int(spl[2][2:-2], base=16), HEX_DIRECTIONS[spl[2][-2]]


instructions: list[tuple[str, int, int, str]] = Advent().read.lines().map(parse_line)()


def part1():
    pos = ivec2(0, 0)
    vertices = [(0, 0)]
    num_points = 0
    for d, n, _, _ in instructions:
        pos += DIRECTIONS[d] * n
        vertices.append((pos.x, pos.y))
        num_points += n

    assert vertices[0] == vertices[-1]

    area = 0
    for a, b in itertools.pairwise(vertices):
        area += a[0] * b[1]
        area -= b[0] * a[1]
    area = abs(area) // 2

    return area + num_points // 2 + 1


def part2():
    pos = ivec2(0, 0)
    vertices = [(0, 0)]
    num_points = 0
    for _, _, n, d in instructions:
        pos += DIRECTIONS[d] * n
        vertices.append((pos.x, pos.y))
        num_points += n

    assert vertices[0] == vertices[-1]

    area = 0
    for a, b in itertools.pairwise(vertices):
        area += a[0] * b[1]
        area -= b[0] * a[1]
    area = abs(area) // 2

    return area + num_points // 2 + 1


print(part1())
print(part2())
