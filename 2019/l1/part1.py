from ..advent import Advent

advent = Advent(1)

modules = advent.read.lines(int)

fuel = 0
for mod in modules:
    fuel += mod // 3 - 2

advent.solution(fuel)
