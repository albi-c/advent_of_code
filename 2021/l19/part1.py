from ..advent import Advent, vec3

advent = Advent(19, 1)

scanners = [[vec3(list(map(int, line.split(",")))) for line in block.splitlines()[1:]] for block in advent.read.blocks()]

aligned = {}

for s in scanners:
    for s_ in scanners:
        if s == s_:
            continue
            
        for b in s:
            for b_ in s:
                if b == b_:
                    continue

                for r in b_.rotations():
                    diff = b - r
                    if diff in aligned:
                        aligned[diff] += 1
                    else:
                        aligned[diff] = 1

for k, v in aligned.items():
    if v >= 12:
        print(k, v)
