from advent import Advent

import functools


advent = Advent()


def parse_line(ln: str) -> tuple[str, list[int]]:
    springs, counts = ln.split(" ")
    return springs, [int(x) for x in counts.split(",")]


data = advent.read.lines().map(parse_line)()


@functools.cache
def get_arrangements(springs: str, counts: tuple[int, ...], num_broken: int = 0) -> int:
    if len(springs) == 0:
        if len(counts) == 0 and num_broken == 0 or len(counts) == 1 and num_broken == counts[0]:
            return 1
        return 0

    spring = springs[0]
    springs = springs[1:]

    count = counts[0]
    new_counts = tuple(counts[1:])
    if len(new_counts) == 0:
        new_counts = (0,)

    if spring == "?":
        return get_arrangements("." + springs, counts, num_broken) + get_arrangements("#" + springs, counts, num_broken)
    elif spring == "#":
        if num_broken > count:
            return 0
        return get_arrangements(springs, counts, num_broken + 1)
    elif spring == ".":
        if num_broken == 0:
            return get_arrangements(springs, counts, 0)
        elif num_broken == count:
            return get_arrangements(springs, new_counts, 0)
        return 0
    else:
        assert False


print(sum(get_arrangements(s, tuple(c)) for s, c in data))

print(sum(get_arrangements("?".join((s,) * 5), tuple(c) * 5) for s, c in data))
