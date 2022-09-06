from ..advent import Advent

advent = Advent(1, 1)

data = advent.read.lines(int)

count = 0

prev = data[0]
for val in data[1:]:
    if val > prev:
        count += 1

    prev = val

advent.solution(count)
