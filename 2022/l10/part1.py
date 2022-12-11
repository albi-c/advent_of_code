from ..advent import Advent

advent = Advent(10)

instructions = advent.read.lines(lambda ln: ln.split())

x = 1
strength = 0
cycle = 0
ins = 0
step = 0
while ins < len(instructions):
    i = instructions[ins]

    cycle += 1

    if (cycle - 20) % 40 == 0:
        strength += x * cycle

    if i[0] == "noop":
        ins += 1
    elif i[0] == "addx":
        if step == 0:
            step = 1
        else:
            step = 0
            ins += 1
            x += int(i[1])

advent.solution(strength)
