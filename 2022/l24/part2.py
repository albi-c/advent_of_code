from ..advent import Advent, vec2

import itertools

advent = Advent(24)

DIRECTIONS = {
    ">": vec2(1, 0),
    "v": vec2(0, 1),
    "<": vec2(-1, 0),
    "^": vec2(0, -1)
}

raw_map = advent.read.lines()

blizzards: list[tuple[vec2, vec2]] = [(vec2(x, y), DIRECTIONS[ch]) for y, ln in enumerate(raw_map[1:-1])
                                                                   for x, ch in enumerate(ln[1:-1]) if ch != "."]

map_size = vec2(len(raw_map[0]) - 2, len(raw_map) - 2)

y_blizzards = [[(b, d) for b, d in blizzards if b.x == x and d.y] for x in range(map_size.x)]
x_blizzards = [[(b, d) for b, d in blizzards if b.y == y and d.x] for y in range(map_size.y)]

blizzard_cache: dict[int, tuple[set[vec2], set[vec2]]] = {}


def is_empty(pos: vec2, step: int) -> bool:
    if (pos.y == -1 and pos.x == 0) or (pos.y == map_size.y and pos.x == map_size.x - 1):
        return True

    if pos.y < 0 or pos.y >= map_size.y or pos.x < 0 or pos.x >= map_size.x:
        return False

    if step in blizzard_cache:
        if pos in blizzard_cache[step][0]:
            return True

        if pos in blizzard_cache[step][1]:
            return False

    if step not in blizzard_cache:
        blizzard_cache[step] = (set(), set())

    for b, d in itertools.chain(y_blizzards[pos.x], x_blizzards[pos.y]):
        # matmul is modulo
        if (b + d * vec2(step, step)) @ map_size == pos:
            blizzard_cache[step][1].add(pos.copy())
            return False

    free = pos not in blizzard_cache[step][1]
    if free:
        blizzard_cache[step][0].add(pos.copy())

    return free


def find_best(step: int, start_pos: vec2, target: vec2) -> int:
    queue: set[vec2] = {start_pos}

    while True:
        new_queue: set[vec2] = set()

        for pos in queue:
            if pos == target:
                return step

            for d in DIRECTIONS.values():
                new_queue.add(pos + d)

        step += 1

        queue = {pos for pos in queue | new_queue if is_empty(pos, step)}

        if len(queue) == 0:
            raise RuntimeError(f"Stuck [step={step}]")


start = vec2(0, -1)
end = map_size - vec2(1, 0)

advent.solution(
    find_best(
        find_best(
            find_best(
                0,
                start,
                end
            ),
            end,
            start
        ),
        start,
        end
    )
)
