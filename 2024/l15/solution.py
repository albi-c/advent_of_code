from advent import Advent, Grid, ivec2

MOVE_DIRS = {
    ">": ivec2(1, 0),
    "<": ivec2(-1, 0),
    "v": ivec2(0, 1),
    "^": ivec2(0, -1)
}

grid_data, moves = Advent().read.blocks()()
grid = Grid.parse(grid_data)
robot_pos = next(grid.search("@"))
grid[robot_pos] = "."

for move in moves:
    if (off := MOVE_DIRS.get(move)) is None:
        continue
    n = 1
    while grid[robot_pos + n * off] == "O":
        n += 1
    if grid[robot_pos + n * off] == "#":
        continue
    elif n > 1:
        grid[robot_pos + n * off] = "O"
        grid[robot_pos + off] = "."
    robot_pos += off
print(sum(pos.x + 100 * pos.y for pos in grid.search("O")))

grid = Grid([[c for ch in ln for c in ((ch, ch) if ch != "O" else "[]")] for ln in grid_data.splitlines()])
robot_pos = next(grid.search("@"))
grid[robot_pos] = "."
grid[robot_pos + (1, 0)] = "."


def can_move(p: ivec2, o: ivec2) -> bool:
    if grid[p] == "#":
        return False
    elif grid[p] == ".":
        return True
    elif grid[p] == "[":
        return can_move(p + o, o) and can_move(p + ivec2(1, 0) + o, o)
    elif grid[p] == "]":
        return can_move(p + o, o) and can_move(p - ivec2(1, 0) + o, o)
    else:
        raise ValueError("Invalid grid value")


def make_move_set(p: ivec2, o: ivec2) -> set[ivec2]:
    if grid[p] == "[":
        return {p, p + ivec2(1, 0)} | make_move_set(p + o, o) | make_move_set(p + ivec2(1, 0) + o, o)
    elif grid[p] == "]":
        return {p, p - ivec2(1, 0)} | make_move_set(p + o, o) | make_move_set(p - ivec2(1, 0) + o, o)
    else:
        return set()


def do_move(p: ivec2, o: ivec2):
    move_set = list(make_move_set(p, o))
    move_set.sort(key=lambda pos: pos.y * -o.y)
    for mov in move_set:
        grid[mov + o] = grid[mov]
        grid[mov] = "."


for move in moves:
    if (off := MOVE_DIRS.get(move)) is None:
        continue
    if off.x != 0:
        n = 1
        while grid[robot_pos + n * off] in "[]":
            n += 1
        if grid[robot_pos + n * off] == "#":
            continue
        for i in range(n, 0, -1):
            grid[robot_pos + i * off] = grid[robot_pos + (i - 1) * off]
        robot_pos += off
    else:
        if can_move(robot_pos + off, off):
            do_move(robot_pos + off, off)
            robot_pos += off
print(sum(pos.x + 100 * pos.y for pos in grid.search("[")))
