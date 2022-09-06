from ..advent import Advent

advent = Advent(2, 1)

hor = 0
dep = 0

for cmd, n in advent.read.lines(lambda x: x.split()):
    n = int(n)

    if cmd == "forward":
        hor += n
    elif cmd == "down":
        dep += n
    elif cmd == "up":
        dep -= n

advent.solution(hor * dep)
