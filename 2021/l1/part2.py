from ..advent import Advent

advent = Advent(1, 2)

data = advent.read.lines(int)

count = 0

prev = data[0] + data[1] + data[2]
prev1 = data[0]
prev2 = data[1]
for val in data[2:]:
    s = prev1 + prev2 + val

    if s > prev:
        count += 1

    prev = s
    prev1 = prev2
    prev2 = val

advent.solution(count)
