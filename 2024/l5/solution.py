from advent import Advent, Stream

from collections import defaultdict


constraint_list, orderings = Advent().read.blocks().lines()()
constraint_list: list[tuple[int, int]] = [tuple(map(int, ln.split("|"))) for ln in constraint_list]
constraints: defaultdict[int, set[int]] = defaultdict(set)
for a, b in constraint_list:
    constraints[a].add(b)
orderings: list[list[int]] = [list(map(int, ln.split(","))) for ln in orderings]


class ConstrainedInt(int):
    def __lt__(self, other):
        if isinstance(other, int):
            return other in constraints[self]


result1 = 0
result2 = 0
for ordering in orderings:
    indices: dict[int, int] = dict(Stream(ordering).enumerate().tuple_swap())
    fail = False
    for i, x in enumerate(ordering):
        for after in constraints[x]:
            if (j := indices.get(after)) is not None:
                if i > j:
                    fail = True
                    break
        if fail:
            break
    if not fail:
        result1 += ordering[len(ordering) // 2]
    else:
        ordering.sort(key=ConstrainedInt)
        result2 += ordering[len(ordering) // 2]
print(result1)
print(result2)
