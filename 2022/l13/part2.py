from ..advent import Advent

from functools import cmp_to_key

advent = Advent(13)

packets = [eval(ln) for ln in advent.read.lines() if ln] + [[[2]], [[6]]]


def compare(a: list | int, b: list | int) -> int:
    if isinstance(a, int) and isinstance(b, int):
        return b - a

    elif isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])

    elif isinstance(a, int) and isinstance(b, list):
        return compare([a], b)

    else:
        for x, y in zip(a, b):
            cmp = compare(x, y)

            if cmp > 0:
                return 1

            elif cmp < 0:
                return -1

        if len(a) == len(b):
            return 0

        if len(a) > len(b):
            return -1

        return 1


packets.sort(key=cmp_to_key(compare), reverse=True)

advent.solution((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
