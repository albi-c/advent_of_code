from advent import Advent

import itertools


data: list[list[int]] = Advent().read.lines().split().map(int)()
differences: list[list[int]] = [[a - b for a, b in itertools.pairwise(ln)] for ln in data]

print(sum(
    all(1 <= x <= 3 for x in ln) or
    all(1 <= -x <= 3 for x in ln)
    for ln in differences))

count = 0
for ln in data:
    if all(1 <= x <= 3 for x in ln) or all(1 <= -x <= 3 for x in ln):
        count += 1
        continue
    for i in range(len(ln)):
        diffs = [a - b for a, b in itertools.pairwise(ln[:i] + ln[i+1:])]
        if all(1 <= x <= 3 for x in diffs) or all(1 <= -x <= 3 for x in diffs):
            count += 1
            break
print(count)
