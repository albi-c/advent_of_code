from advent import Advent, ivec2


NEIGHBORS = (
    ivec2(1, 0),
    ivec2(-1, 0),
    ivec2(0, 1),
    ivec2(0, -1)
)


grid: list[str] = Advent().read.lines()()
size = ivec2(len(grid[0]), len(grid))
start_pos = None
for y, row in enumerate(grid):
    for x, ch in enumerate(row):
        if ch == "S":
            grid[y] = row[:x] + "." + row[x+1:]
            start_pos = ivec2(y, x)
assert start_pos is not None


def index_grid(pos: ivec2, repeat_grid: bool) -> str | None:
    if not in_grid(pos):
        if repeat_grid:
            pos = pos % size
        else:
            return None

    return grid[pos.y][pos.x]


def in_grid(pos: ivec2) -> bool:
    return 0 <= pos.x < size.x and 0 <= pos.y < size.y


def pathfind(seen_states: set[tuple[tuple[int, int], int]], reachable: set[tuple[int, int]],
             goal_distance: int, pos: ivec2, distance: int, repeat_grid: bool):

    if index_grid(pos, repeat_grid) != ".":
        return

    if distance == goal_distance:
        reachable.add((pos.x, pos.y))
        return

    state = ((pos.x, pos.y), distance)
    if state in seen_states:
        return
    seen_states.add(state)

    for n in NEIGHBORS:
        pathfind(seen_states, reachable, goal_distance, pos + n, distance + 1, repeat_grid)


def count_steps(goal_distance: int, repeat_grid: bool = False) -> int:
    reachable = set()
    pathfind(set(), reachable, goal_distance, start_pos, 0, repeat_grid)
    return len(reachable)


print(count_steps(64))

print(count_steps(65 + 0*131, True))
print(count_steps(65 + 1*131, True))
print(count_steps(65 + 2*131, True))
