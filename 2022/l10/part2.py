from ..advent import Advent

advent = Advent(10)

instructions = advent.read.lines(lambda ln: ln.split())

x = 1
image = [["" for _ in range(40)] for _ in range(6)]
cycle = 0
ins = 0
step = 0
while ins < len(instructions):
    i = instructions[ins]

    image[cycle // 40][cycle % 40] = abs(cycle % 40 - x) < 2

    cycle += 1

    if i[0] == "noop":
        ins += 1
    elif i[0] == "addx":
        if step == 0:
            step = 1
        else:
            step = 0
            ins += 1
            x += int(i[1])

print("\n".join("".join(["#" if ch else "."  for ch in row]) for row in image))
