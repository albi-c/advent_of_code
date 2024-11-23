from advent import Advent

from z3 import *


type Ingredient = tuple[int, int, int, int, int]

data: list[Ingredient] = Advent().read.lines().map(
    lambda ln: tuple(int(seg.split(" ")[1]) for seg in ln.split(" ", 1)[1].split(", ")))()


def solve(part: int) -> int:
    solver = Optimize()

    score = Int("score")
    ps = [Int(f"p{i}") for i in range(5)]
    cps = [If(p < 0, 0, p) for p in ps]
    solver.add(score == cps[0] * cps[1] * cps[2] * cps[3])
    if part == 2:
        solver.add(ps[4] == 500)
    ins = [Int(f"i{i}") for i in range(len(data))]
    for i in ins:
        solver.add(0 <= i)
        solver.add(i <= 100)
    solver.add(sum(ins) == 100)
    for i in range(5):
        solver.add(ps[i] == sum(ins[j] * params[i] for j, params in enumerate(data)))
    solver.maximize(score)
    assert solver.check() == sat
    return solver.model().evaluate(score)


print(solve(1))
print(solve(2))
