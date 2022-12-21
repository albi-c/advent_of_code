from ..advent import Advent

import operator

advent = Advent(21)

OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv
}


def parse_calculation(calc: str):
    spl = calc.split()

    if len(spl) == 1:
        def inner(_) -> int:
            return int(spl[0])

        return inner

    else:
        def inner(m: dict) -> int:
            return OPERATORS[spl[1]](m[spl[0]](m), m[spl[2]](m))

        return inner


monkeys = {name: parse_calculation(calc) for name, calc in advent.read.lines(lambda ln: ln.split(": "))}


advent.solution(monkeys["root"](monkeys))
