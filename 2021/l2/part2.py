from ..advent import Advent

advent = Advent(2, 2)

hor = 0
dep = 0

aim = 0

for cmd, n in advent.read.lines(lambda x: x.split()):
    n = int(n)

    if cmd == "forward":
        hor += n

        dep += aim * n
    elif cmd == "down":
        aim += n
    elif cmd == "up":
        aim -= n

advent.solution(hor * dep)
