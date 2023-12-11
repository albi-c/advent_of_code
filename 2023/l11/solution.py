from advent import Advent, ivec2

import itertools


advent = Advent()

data: list[list[bool]] = [[ch == "#" for ch in row] for row in advent.read.lines()()]

expansions_row: list[int] = []
expansions_col: list[int] = []

for i, row in enumerate(data):
    if not any(row):
        expansions_row.append(i)

for i in range(len(data[0])):
    if not any(row[i] for row in data):
        expansions_col.append(i)


def get_expanded_distance_on_axis(multiplier: int, a: int, b: int, expansion: list[int]) -> int:
    return b - a + multiplier * sum(a < p < b for p in expansion)


def get_expanded_distance(multiplier: int, a: ivec2, b: ivec2) -> int:
    return (get_expanded_distance_on_axis(multiplier, min(a.x, b.x), max(a.x, b.x), expansions_col) +
            get_expanded_distance_on_axis(multiplier, min(a.y, b.y), max(a.y, b.y), expansions_row))


galaxies = [ivec2(x, y) for x, y in itertools.product(range(len(data[0])), range(len(data))) if data[y][x]]


print(sum(get_expanded_distance(1, a, b) for a, b in itertools.combinations(galaxies, 2)))

print(sum(get_expanded_distance(999999, a, b) for a, b in itertools.combinations(galaxies, 2)))
