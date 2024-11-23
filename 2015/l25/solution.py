from advent import Advent

_, row, _, column = Advent().read().rsplit(" ", 3)
row = int(row[:-1])
column = int(column[:-1])


def index(x: int, y: int) -> int:
    s = x + y
    return (s * (s - 1)) // 2 - y + 1


c = 20151125
for i in range(index(column, row) - 1):
    c *= 252533
    c %= 33554393
print(c)
