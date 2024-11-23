from advent import Advent

import itertools
import math


packages: list[int] = Advent().read.lines().map(int)()
total_weight = sum(packages)


def solve(target: int) -> int:
    for i in itertools.count(1):
        best = 1 << 62
        for pkgs in itertools.combinations(packages, i):
            if sum(pkgs) == target:
                best = min(best, math.prod(pkgs))
        if best != (1 << 62):
            return best


print(solve(total_weight // 3))
print(solve(total_weight // 4))
