from ..advent import Advent, vec3

advent = Advent(18)

NEIGHBORS = [
    vec3(1, 0, 0), vec3(-1, 0, 0),
    vec3(0, 1, 0), vec3(0, -1, 0),
    vec3(0, 0, 1), vec3(0, 0, -1)
]

cubes = set(advent.read.lines(lambda ln: vec3([int(val) for val in ln.split(",")])))

sides = 0
for cube in cubes:
    sides += sum(cube + n not in cubes for n in NEIGHBORS)

advent.solution(sides)
