from advent import Advent

advent = Advent()

print(advent.read().count("(") - advent.read().count(")"))

f = 0
for i, ch in enumerate(advent.read()):
    if ch == "(":
        f += 1
    else:
        f -= 1
    if f == -1:
        print(i + 1)
        break
