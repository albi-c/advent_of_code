from ..advent import Advent

advent = Advent(4)

data = advent.read.lines(lambda ln: tuple(tuple(map(int, x.split("-"))) for x in ln.split(",")))


def range_in(a: tuple[int, int], b: tuple[int, int]):
    return b[0] <= a[0] <= b[1] and b[0] <= a[1] <= b[1]


advent.solution(sum(range_in(a, b) or range_in(b, a) for a, b in data))
