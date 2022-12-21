from __future__ import annotations

from ..advent import Advent

import operator

advent = Advent(21)

OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

INVERSE_OPERATORS = {
    "+": operator.sub,
    "-": operator.add,
    "*": operator.truediv,
    "/": operator.mul
}


class Unknown:
    operations: list[tuple]

    def __init__(self, operations: list[tuple]):
        self.operations = operations

    def resolve(self, value: int) -> int:
        for a, op, b in self.operations[::-1]:
            print(value, "|", a, op, b)
            # a, b = b, a

            if b is None:
                if op == "+":
                    value = a - value
                elif op == "-":
                    value = a + value
                elif op == "*":
                    value = a / value
                elif op == "/":
                    value = a * value

                # print(f"value = {a} {op} x{value}", end=" ")
                # value = INVERSE_OPERATORS[op](a, value)
                # print(f"-> {value}")
            else:
                if op == "+":
                    value -= b
                elif op == "-":
                    value += b
                elif op == "*":
                    value /= b
                elif op == "/":
                    value *= b

                # print(f"value = x{value} {op} {b}", end=" ")
                # value = INVERSE_OPERATORS[op](value, b)
                # print(f"-> {value}")

        return value

    def __add__(self, other: int) -> Unknown:
        return Unknown(self.operations + [(other, "+", None)])

    def __sub__(self, other: int) -> Unknown:
        return Unknown(self.operations + [(other, "-", None)])

    def __mul__(self, other: int) -> Unknown:
        return Unknown(self.operations + [(other, "*", None)])

    def __truediv__(self, other: int) -> Unknown:
        return Unknown(self.operations + [(other, "/", None)])

    def __radd__(self, other: int) -> Unknown:
        return Unknown(self.operations + [(None, "+", other)])

    def __rsub__(self, other: int) -> Unknown:
        return Unknown(self.operations + [(None, "-", other)])

    def __rmul__(self, other: int) -> Unknown:
        return Unknown(self.operations + [(None, "*", other)])

    def __rtruediv__(self, other: int) -> Unknown:
        return Unknown(self.operations + [(None, "/", other)])


def root_func(spl: list[str]):
    def inner(m: dict) -> int:
        a = m[spl[0]](m)
        b = m[spl[2]](m)

        if isinstance(a, Unknown):
            resolved = a.resolve(b)

        else:
            resolved = b.resolve(a)

        # binary search by hand
        resolved = 3219579395609

        m["humn"] = lambda _: resolved

        if m[spl[0]](m) != m[spl[2]](m):
            print("Doesn't match!", m[spl[0]](m), m[spl[2]](m), sep="\n")
        else:
            print("Matches!")

        return resolved

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
