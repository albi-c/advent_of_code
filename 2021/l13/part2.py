from ..advent import Advent, Grid

advent = Advent(13, 2)

points, folds = advent.read.blocks()
points = [list(map(int, point.split(","))) for point in points.splitlines()]
folds = [(x[0], int(x[1])) for x in [y.split()[2].split("=") for y in folds.splitlines()]]

for axis, n in folds:
    if axis == "x":
        points = [[n - (p[0] - n) if p[0] > n else p[0], p[1]] for p in points if p[0] != n]
    elif axis == "y":
        points = [[p[0], n - (p[1] - n) if p[1] > n else p[1]] for p in points if p[1] != n]

points = advent.util.remove_duplicates(points)

Grid.print(points)

advent.solution(len(points))
