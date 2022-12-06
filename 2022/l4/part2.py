from ..advent import Advent

advent = Advent(4)

data = advent.read.lines(lambda ln: tuple(tuple(map(int, x.split("-"))) for x in ln.split(",")))


def range_overlaps(a: tuple[int, int], b: tuple[int, int]):
    return a[0] <= b[1] and a[1] >= b[0]


advent.solution(sum(range_overlaps(a, b) or range_overlaps(b, a) for a, b in data))
