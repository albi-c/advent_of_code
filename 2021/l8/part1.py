from ..advent import Advent

advent = Advent(8, 1)

displays = list(map(lambda x: list(map(lambda y: y.split(), x.split(" | "))), advent.read.lines()))

count = 0
for _, numbers in displays:
    for n in numbers:
        if len(n) in (2, 3, 4, 7):
            count += 1

advent.solution(count)
