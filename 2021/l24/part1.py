from advent import Advent, Util

from typing import Generator
from z3 import *


def extract_variables() -> Generator[tuple[int, int, int], None, None]:
    for chunk in Util.chunks(Advent().read.lines()(), 18):
        x_add = int(chunk[5].rsplit(" ", 1)[1])
        y_add = int(chunk[15].rsplit(" ", 1)[1])
        z_div = int(chunk[4].rsplit(" ", 1)[1])

        yield x_add, y_add, z_div


def one_step(inp: int, z: int, x_add: int, y_add: int, z_div: int) -> int:
    if z % 26 + x_add != inp:
        z //= z_div
        z *= 26
        z += inp + y_add
    else:
        z //= z_div

    return z


def solve() -> int:
    solver = Optimize()

    z = IntVal(0)

    ws = [Int(f"w_{i}") for i in range(14)]
    for i in range(14):
        solver.add(And(ws[i] >= 1, ws[i] <= 9))

    result = Int("result")
    solver.add(result == sum((10 ** i) * digit for i, digit in enumerate(reversed(ws))))

    for i, (x_add, y_add, z_div) in enumerate(extract_variables()):
        z = If(z % 26 + x_add == ws[i], z / z_div, z / z_div * 26 + ws[i] + y_add)

    solver.add(z == 0)

    solver.maximize(result)
    assert solver.check() == sat
    return solver.model().eval(result)


print(solve())
