from __future__ import annotations

from ..advent import Advent

import operator

advent = Advent(21)

OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv
}

INVERSE_OPERATORS = {
    "+": operator.sub,
    "-": operator.add,
    "*": operator.floordiv,
    "/": operator.mul
}


Operation = tuple[int | None, str, int | None]


"""
100

* 10
10 /
- 3

x
"""


class Unknown:
    operations: list[Operation]

    def __init__(self, operations: list[Operation]):
        self.operations = operations

    def resolve(self, value: int) -> int:
        for a, op, b in self.operations[::-1]:
            if a is None:
                if op in ("/", "-"):
                    value = OPERATORS[op](value, b)
                else:
                    value = INVERSE_OPERATORS[op](value, b)
            else:
                # if op in ("/", "-"):
                #     value = OPERATORS[op](a, value)
                # else:
                value = INVERSE_OPERATORS[op](a, value)

        return value

    def __add__(self, other: int) -> Unknown:
        return Unknown(self.operations + [(other, "+", None)])

    def __sub__(self, other: int) -> Unknown:
        return Unknown(self.operations + [(other, "-", None)])

    def __mul__(self, other: int) -> Unknown:
        return Unknown(self.operations + [(other, "*", None)])

    def __floordiv__(self, other: int) -> Unknown:
        return Unknown(self.operations + [(other, "/", None)])

    def __radd__(self, other: int) -> Unknown:
        return Unknown(self.operations + [(None, "+", other)])

    def __rsub__(self, other: int) -> Unknown:
        return Unknown(self.operations + [(None, "-", other)])

    def __rmul__(self, other: int) -> Unknown:
        return Unknown(self.operations + [(None, "*", other)])

    def __rfloordiv__(self, other: int) -> Unknown:
        return Unknown(self.operations + [(None, "/", other)])


def root_func(spl: list[str]):
    def inner(m: dict) -> int:
        a = m[spl[0]](m)
        b = m[spl[2]](m)

        if isinstance(a, Unknown):
            return a.resolve(b)

        else:
            return b.resolve(a)

    return inner


def parse_calculation(name: str, calc: str):
    spl = calc.split()

    if name == "humn":
        return lambda _: Unknown([])

    if len(spl) == 1:
        return lambda _: int(spl[0])

    else:
        if name == "root":
            return root_func(spl)

        return lambda m: OPERATORS[spl[1]](m[spl[0]](m), m[spl[2]](m))


monkeys = {name: parse_calculation(name, calc) for name, calc in advent.read.lines(lambda ln: ln.split(": "))}


advent.solution(monkeys["root"](monkeys))
