from ..advent import Advent

advent = Advent(20)

values: list[tuple[int, int]] = [(int(ln), i) if ln != "0" else (0, 0) for i, ln in enumerate(advent.read.lines())]
moved = values.copy()

for val, i in values:
    i = moved.index((val, i))
    ni = (i + val) % (len(values) - 1)
    moved.insert(ni, moved.pop(i))

zero = moved.index((0, 0))

advent.solution(sum(moved[((i + 1) * 1000 + zero) % len(moved)][0] for i in range(3)))
