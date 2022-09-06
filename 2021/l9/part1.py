from ..advent import Advent, Grid

advent = Advent(9, 1)

grid = Grid(advent.read.lines(lambda line: list(map(int, list(line)))))

danger = 0

for pos, val in grid.items():
    if all([x > val for _, x in grid.neighbors(pos)]):
        danger += 1 + val

advent.solution(danger)
