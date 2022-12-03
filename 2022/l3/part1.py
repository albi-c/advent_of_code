from ..advent import Advent

advent = Advent(3)

data = advent.read.lines(lambda ln: (set(ln[:len(ln)//2]), set(ln[len(ln)//2:])))


def calc_priority(item: str) -> int:
    if item.islower():
        return ord(item) - ord("a") + 1

    return ord(item) - ord("A") + 27


priorities = 0
for c1, c2 in data:
    common = c1 & c2
    for i in common:
        priorities += calc_priority(i)

advent.solution(priorities)
