from ..advent import Advent, vec2

advent = Advent(17)

WIDTH = 7
STEPS = 1_000_000_000_000

ROCK_SHAPES = [
    (vec2(0, 0), vec2(1, 0), vec2(2, 0), vec2(3, 0)),
    (vec2(0, 1), vec2(1, 0), vec2(1, 1), vec2(1, 2), vec2(2, 1)),
    (vec2(0, 0), vec2(1, 0), vec2(2, 0), vec2(2, 1), vec2(2, 2)),
    (vec2(0, 0), vec2(0, 1), vec2(0, 2), vec2(0, 3)),
    (vec2(0, 0), vec2(0, 1), vec2(1, 0), vec2(1, 1))
]

moves_ = [vec2(1, 0) if ch == ">" else vec2(-1, 0) for ch in advent.read()]


def move_rock(rock: tuple[vec2, ...], move: vec2) -> tuple[vec2, ...]:
    return tuple(part + move for part in rock)


def collide_rock(rock: tuple[vec2, ...], rocks: set[tuple[int, int]]) -> bool:
    if rock[0].x < 0 or rock[-1].x >= WIDTH:
        return True

    return any(part.y < 0 or part.tuple() in rocks for part in rock)


def highest_rock(rocks: set[tuple[int, int]]) -> int:
    return max((rock[1] for rock in rocks), default=-1) + 1


def get_top_pattern(rocks: set[tuple[int, int]], max_y: int) -> tuple[int, ...]:
    return tuple(max((rock[1] - max_y for rock in rocks if rock[0] == i), default=0) for i in range(WIDTH))


def run(moves: list[vec2]) -> int:
    rocks = set()
    cache = {}

    offset = 0

    move_i = 0
    i = 0
    while i < STEPS:
        y = highest_rock(rocks)
        rock = move_rock(ROCK_SHAPES[i % len(ROCK_SHAPES)], vec2(2, y + 3))

        while True:
            moved = move_rock(rock, moves[move_i % len(moves)])
            move_i += 1

            if not collide_rock(moved, rocks):
                rock = moved

            moved = move_rock(rock, vec2(0, -1))
            if collide_rock(moved, rocks):
                rocks |= {part.tuple() for part in rock}
                break
            rock = moved

        highest = highest_rock(rocks)

        if offset == 0:
            state = (i % len(ROCK_SHAPES), move_i % len(moves)) + get_top_pattern(rocks, highest)
            if state in cache:
                l_h, l_i = cache[state]
                offset = (STEPS - i) // (i - l_i) * (highest - l_h)
                i = STEPS - (STEPS - i) % (i - l_i)

            cache[state] = (highest, i)

        i += 1

    return highest_rock(rocks) + offset


advent.solution(run(moves_))
