from advent import Advent

import re


data = Advent().read()

print(sum(int(a) * int(b) for a, b in re.findall(r"mul\((\d+),(\d+)\)", data)))

result = 0
enabled = True
for a, b, c in re.findall(r"mul\((\d+),(\d+)\)|(do\(\)|don't\(\))", data):
    if c == "do()":
        enabled = True
    elif c == "don't()":
        enabled = False
    elif enabled:
        result += int(a) * int(b)
print(result)
