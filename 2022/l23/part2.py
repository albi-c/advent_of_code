from ..advent import Advent, vec2

advent = Advent(23)

DIRECTIONS: list[vec2] = [
    vec2(0, -1),
    vec2(0, 1),
    vec2(-1, 0),
    vec2(1, 0)
]

NEIGHBORS: list[vec2] = [
    vec2(-1, -1), vec2(0, -1), vec2(1, -1),
    vec2(-1, 0),               vec2(1, 0),
    vec2(-1, 1),  vec2(0, 1),  vec2(1, 1)
]

MOVE_OPTIONS: dict[vec2, tuple[vec2, vec2, vec2]] = {
    vec2(0, -1): (vec2(-1, -1), vec2(0, -1), vec2(1, -1)),
    vec2(0, 1): (vec2(-1, 1), vec2(0, 1), vec2(1, 1)),
    vec2(-1, 0): (vec2(-1, -1), vec2(-1, 0), vec2(-1, 1)),
    vec2(1, 0): (vec2(1, -1), vec2(1, 0), vec2(1, 1))
}

elves: set[vec2] = {vec2(x, y) for y, ln in enumerate(advent.read.lines()) for x, ch in enumerate(ln) if ch == "#"}
proposals: dict[vec2, vec2] = {}
conflicts: set[vec2] = set()


def get_elf_bounds() -> tuple[vec2, vec2]:
    return vec2(min(elves, key=lambda e: e.x).x, min(elves, key=lambda e: e.y).y), \
           vec2(max(elves, key=lambda e: e.x).x, max(elves, key=lambda e: e.y).y)


i = 0
while True:
    directions = DIRECTIONS[i % len(DIRECTIONS):] + DIRECTIONS[:i % len(DIRECTIONS)]

    for elf in elves:
        if not any(elf + n in elves for n in NEIGHBORS):
            continue

        for d in directions:
            if not any(elf + mo in elves for mo in MOVE_OPTIONS[d]):
                np = elf + d

                if np in proposals:
                    conflicts.add(np)
                    break

                proposals[np] = elf
                break

    if len(proposals) == 0:
        break

    for np, p in proposals.items():
        if np not in conflicts:
            elves.remove(p)
            elves.add(np)

    proposals = {}
    conflicts = set()

    i += 1

advent.solution(i + 1)
