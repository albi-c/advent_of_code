from ..advent import Advent

advent = Advent(7, 1)

crabs = advent.read.separated(",", int)

best = 1000000000
for i in range(min(crabs), max(crabs) + 1):
    fuel = 0
    for crab in crabs:
        fuel += abs(crab - i)
    if fuel < best:
        best = fuel

advent.solution(best)
