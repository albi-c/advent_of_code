from ..advent import Advent

advent = Advent(6)

data = advent.read()

for i in range(len(data)):
    if i > 3:
        part = data[i-4:i]
        if len(set(part)) == 4:
            advent.solution(i)
            break
