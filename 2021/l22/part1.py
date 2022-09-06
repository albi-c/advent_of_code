from ..advent import Advent

advent = Advent(22, 1)

steps = [(s[0], [list(map(int, p.split("=")[1].split(".."))) for p in s[1].split(",")]) for s in advent.read.lines(lambda x: x.split(" "))]

cubes = set()

for s, r in steps:
    for x in range(max(r[0][0], -50), min(r[0][1] + 1, 51)):
        for y in range(max(r[1][0], -50), min(r[1][1] + 1, 51)):
            for z in range(max(r[2][0], -50), min(r[2][1] + 1, 51)):
                if s == "on":
                    cubes.add((x, y, z))
                else:
                    if (x, y, z) in cubes:
                        cubes.remove((x, y, z))

advent.solution(len(cubes))
