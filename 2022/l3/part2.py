from ..advent import Advent

advent = Advent(3)

data = advent.util.chunks(advent.read.lines(set), 3)


def calc_priority(item: str) -> int:
    if item.islower():
        return ord(item) - ord("a") + 1

    return ord(item) - ord("A") + 27


priorities = 0
for b1, b2, b3 in data:
    common = b1 & b2 & b3
    for i in common:
        priorities += calc_priority(i)

advent.solution(priorities)
