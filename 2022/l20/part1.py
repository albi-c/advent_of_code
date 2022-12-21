from ..advent import Advent

advent = Advent(20)

values: list[tuple[int, int]] = [(int(ln), i) if ln != "0" else (0, 0) for i, ln in enumerate(advent.read.lines())]
moved: list[tuple[int, ...]] = values.copy()

for val, i in values:
    i = moved.index((val, i))
    ni = (i + val) % len(values) + (val > 0)
    if ni == 0:
        ni = len(moved)

    print(val)
    print(list(p[0] for p in moved), i, ni)
    moved.insert(ni, (val,))
    print(list(p[0] for p in moved))
    moved.pop(i + (ni < i))
    print(list(p[0] for p in moved), end="\n\n")

offset = moved.index((0, 0))
advent.solution(moved[(1000 + offset) % len(values)][0] +
                moved[(2000 + offset) % len(values)][0] +
                moved[(3000 + offset) % len(values)][0])
