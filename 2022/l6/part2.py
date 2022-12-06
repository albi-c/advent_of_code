from ..advent import Advent

advent = Advent(6)

data = advent.read()

for i in range(len(data)):
    if i > 13:
        part = data[i-14:i]
        if len(set(part)) == 14:
            advent.solution(i)
            break
