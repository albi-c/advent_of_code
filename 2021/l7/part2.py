from ..advent import Advent

advent = Advent(7, 2)

crabs = advent.read.separated(",", int)

best = 1000000000
for i in range(min(crabs), max(crabs) + 1):
    fuel = 0
    for crab in crabs:
        dist = abs(crab - i)
        fuel += (dist * dist + dist) / 2
    if fuel < best:
        best = fuel

advent.solution(best)
