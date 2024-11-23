from advent import Advent

import functools
import itertools


class HashableList[T](list[T]):
    def __hash__(self):
        return id(self)


sizes: HashableList[int] = HashableList(Advent().read.lines().map(int)())

starting_amount = 150


@functools.cache
def solve(amount: int, index: int, containers: HashableList[int]) -> int:
    if amount == 0:
        return 1
    if index >= len(containers):
        return 0
    size = containers[index]
    return solve(amount - size, index + 1, containers) + solve(amount, index + 1, containers)


@functools.cache
def solve_2(amount: int, index: int, used: int, containers: HashableList[int]) -> int:
    if amount == 0:
        return used
    if index >= len(containers):
        return 1 << 30
    size = containers[index]
    return min(solve_2(amount - size, index + 1, used + 1, containers),
               solve_2(amount, index + 1, used, containers))


print(solve(150, 0, sizes))
min_length = solve_2(150, 0, 0, sizes)
print(sum(sum(comb) == 150 for comb in itertools.combinations(sizes, min_length)))
