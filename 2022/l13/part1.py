from ..advent import Advent

advent = Advent(13)

pairs = [list(map(eval, block.splitlines())) for block in advent.read.blocks()]


def compare(a: list | int, b: list | int) -> int:
    if isinstance(a, int) and isinstance(b, int):
        return 1 if a < b else 0 if a > b else -1

    elif isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])

    elif isinstance(a, int) and isinstance(b, list):
        return compare([a], b)

    else:
        for x, y in zip(a, b):
            cmp = compare(x, y)

            if cmp == 1:
                return 1

            elif cmp == 0:
                return 0

        if len(a) == len(b):
            return -1

        if len(a) > len(b):
            return 0

        return 1


advent.solution(sum(i + 1 for i, pair in enumerate(pairs) if compare(*pair) == 1))
