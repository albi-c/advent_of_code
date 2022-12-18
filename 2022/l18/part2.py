from ..advent import Advent, vec3

advent = Advent(18)

NEIGHBORS = [
    vec3(1, 0, 0), vec3(-1, 0, 0),
    vec3(0, 1, 0), vec3(0, -1, 0),
    vec3(0, 0, 1), vec3(0, 0, -1)
]

cubes: set[vec3] = set(advent.read.lines(lambda ln: vec3([int(val) for val in ln.split(",")])))


def open_sides(c: vec3) -> int:
    return sum(c + n not in cubes for n in NEIGHBORS)


def find_pocket(c: vec3, s: set[vec3]):
    if min(c.tuple()) < 0 or max(c.tuple()) > 20:
        return None

    pocket = {c}
    for n in NEIGHBORS:
        m = c + n
        if m not in cubes and m not in s:
            p = find_pocket(m, s | pocket)
            if p is None:
                return None
            pocket |= p

    return pocket


sides = 0
trapped = set()

for cube in cubes:
    sides += open_sides(cube)

    for neighbor in NEIGHBORS:
        moved = cube + neighbor
        if moved not in cubes and moved not in trapped:
            pock = find_pocket(moved, set())
            if pock is not None:
                trapped |= pock

for cube in trapped:
    sides -= 6 - open_sides(cube)

advent.solution(sides)
