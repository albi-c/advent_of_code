from advent import Advent, Grid, ivec2

grid = Grid(Advent().read(), lambda ch: 1 if ch == "#" else 2 if ch == "^" else 0)


def get_start_pos() -> ivec2:
    guard_pos = None
    for x in range(grid.width):
        for y in range(grid.height):
            if grid[x, y] == 2:
                grid[x, y] = 0
                guard_pos = ivec2(x, y)
                break
        if guard_pos is not None:
            break
    assert guard_pos is not None
    return guard_pos


guard_start_pos = get_start_pos()


def part1():
    guard_pos = guard_start_pos
    guard_dir = ivec2(0, -1)
    visited = set()
    while True:
        visited.add(guard_pos)
        moved = guard_pos + guard_dir
        if not grid.inside(moved):
            break
        if grid[moved] == 1:
            guard_dir = ivec2(-guard_dir.y, guard_dir.x)
        else:
            guard_pos = moved
    print(len(visited))


part1()


def check_loop() -> bool:
    guard_pos = guard_start_pos
    guard_dir = ivec2(0, -1)
    visited = set()
    while True:
        state = (guard_pos, guard_dir)
        if state in visited:
            return True
        visited.add((guard_pos, guard_dir))
        moved = guard_pos + guard_dir
        if not grid.inside(moved):
            return False
        if grid[moved] == 1:
            guard_dir = ivec2(-guard_dir.y, guard_dir.x)
        else:
            guard_pos = moved


def part2():
    count = 0
    for x in range(grid.width):
        for y in range(grid.height):
            if grid[x, y] == 0 and ivec2(x, y) != guard_start_pos:
                grid[x, y] = 1
                if check_loop():
                    count += 1
                grid[x, y] = 0
    print(count)


part2()
