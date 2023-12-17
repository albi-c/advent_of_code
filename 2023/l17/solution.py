from advent import Advent, ivec2

import heapq
from typing import Callable, Iterable


Vec = tuple[int, int]
Path = tuple[Vec, Vec | None, int]


DIRECTIONS: tuple[ivec2, ...] = (ivec2(1, 0), ivec2(0, 1), ivec2(-1, 0), ivec2(0, -1))

grid: list[list[int]] = [[int(val) for val in row] for row in Advent().read.lines()()]
size = ivec2(len(grid[0]), len(grid))
end: Vec = (size.x - 1, size.y - 1)


def in_grid(pos: ivec2 | Vec) -> bool:
    return 0 <= pos[0] < size.x and 0 <= pos[1] < size.y


def pathfind(get_neighbors_: Callable[[Path], Iterable[tuple[int, Path]]]) -> int:
    visited: set[Path] = set()
    costs: dict[Path, int] = {}

    queue: list[tuple[int, Path]] = [(0, ((0, 0), None, 0))]
    while queue:
        cost, path = heapq.heappop(queue)

        if path[0] == end:
            return cost

        if path in visited:
            continue
        visited.add(path)

        for weight, neighbor in get_neighbors_(path):
            prev_cost = costs.get(neighbor)
            next_cost = cost + weight

            if prev_cost is None or next_cost < prev_cost:
                costs[neighbor] = next_cost
                heapq.heappush(queue, (next_cost, neighbor))

    assert False


def get_neighbors(path: Path):
    pos, direction, run = path
    if direction is not None:
        direction = ivec2(direction)

    for off in DIRECTIONS:
        next_pos: ivec2 = off + pos
        if not in_grid(next_pos):
            continue

        next_dir: ivec2 = next_pos - pos
        if direction is not None and next_dir == -direction:
            continue

        turning = direction is not None and next_dir != direction
        next_run = 1 if turning else run + 1

        if next_run > 3:
            continue

        yield grid[next_pos.y][next_pos.x], ((next_pos.x, next_pos.y), (next_dir.x, next_dir.y), next_run)


def get_neighbors_2(path: Path):
    pos, direction, run = path
    if direction is not None:
        direction = ivec2(direction)

    for off in DIRECTIONS:
        next_pos: ivec2 = off + pos
        if not in_grid(next_pos):
            continue

        next_dir: ivec2 = next_pos - pos
        if direction is not None and next_dir == -direction:
            continue

        turning = direction is not None and next_dir != direction
        next_run = 1 if turning else run + 1

        if next_run > 10 or (turning and run < 4) or (next_pos == end and next_run < 4):
            continue

        yield grid[next_pos.y][next_pos.x], ((next_pos.x, next_pos.y), (next_dir.x, next_dir.y), next_run)


print(pathfind(get_neighbors))
print(pathfind(get_neighbors_2))
