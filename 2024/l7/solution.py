from advent import Advent

import itertools


equations = [(int(a), list(map(int, b.split(" ")))) for a, b in Advent().read.lines().split(": ")()]


def solve(concat: bool):
    operations = [lambda a, b: a + b, lambda a, b: a * b]
    if concat:
        operations.append(lambda a, b: int(str(a) + str(b)))
    count = 0
    for result, inputs in equations:
        for ops in itertools.product(operations, repeat=len(inputs)-1):
            value = inputs[0]
            for op, x in zip(ops, inputs[1:]):
                value = op(value, x)
            if value == result:
                count += result
                break
    print(count)


solve(False)
solve(True)
