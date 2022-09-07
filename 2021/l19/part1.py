from ..advent import Advent, vec3, mat3

from collections import defaultdict

advent = Advent(19, 1)

scanners = [[vec3(list(map(int, line.split(",")))) for line in block.splitlines()[1:]] for block in advent.read.blocks()]

scanners = [
    [
        vec3(0, 2, 0),
        vec3(4, 1, 0),
        vec3(3, 3, 0)
    ],
    [
        vec3(-1, -1, 0),
        vec3(-5, 0, 0),
        vec3(-2, 1, 0)
    ]
]

aligns = defaultdict(set)

for rot in vec3.rotation_matrices():
    for i, s in enumerate(scanners[1:]):
        aligned = defaultdict(int)
        for beacon in scanners[0]:
            for b in s:
                aligned[beacon - b * rot] += 1
        for v in aligned.values():
            if v >= 2:
                aligns[i].add(rot)

print(aligns)

# for s in scanners[1:]:
#     for b in scanners[0]:
#         for rot in vec3.rotation_matrices():
#             for b_ in s:
#                 b_ *= rot
                
#                 if b == b_: continue
                
#                 diff = b - b_
                        
#                 aligned[diff].add((b, b_))

# for k, v in aligned.items():
#     if len(v) >= 1:
#         print(k, v, end="\n\n")
