from ..advent import Advent, vec2

advent = Advent(17)

WIDTH = 7

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
    if len(rocks) == 0:
        return 0

    return max(rock[1] for rock in rocks) + 1


def run(moves: list[vec2]) -> int:
    rocks = set()

    move_i = 0
    for i in range(1000000000000):
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

    return highest_rock(rocks)


advent.solution(run(moves_))
