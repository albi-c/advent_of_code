from advent import Advent, Grid, ivec2

from matplotlib.path import Path


DIRECTIONS: dict[str, tuple[ivec2, ivec2]] = {
    "|": (ivec2(0, -1), ivec2(0, 1)),
    "-": (ivec2(-1, 0), ivec2(1, 0)),
    "L": (ivec2(0, -1), ivec2(1, 0)),
    "J": (ivec2(0, -1), ivec2(-1, 0)),
    "7": (ivec2(-1, 0), ivec2(0, 1)),
    "F": (ivec2(1, 0), ivec2(0, 1))
}


advent = Advent()

grid = Grid(advent.read())

pos = None
start_pos = None
for y in range(grid.height):
    for x in range(grid.width):
        if grid[x, y] == "S":
            pos = ivec2(x, y)
            start_pos = ivec2(x, y)
assert pos is not None and start_pos is not None

last_movement = None
visited = [tuple(start_pos)]

for n in grid.neighbors(pos):
    ch = grid[n]
    if ch not in DIRECTIONS:
        continue

    if pos - n in DIRECTIONS[ch]:
        last_movement = pos - n
        pos = n
        break

assert last_movement is not None

while grid[pos] != "S":
    visited.append(tuple(pos))

    ch = grid[pos]
    movement = DIRECTIONS[ch]

    move = movement[0]
    if last_movement == move:
        move = movement[1]

    pos += move
    last_movement = -move

print(len(visited) // 2)


loop_positions = set(visited)

path = Path(visited)
enclosed_tiles = set()
for y in range(grid.height):
    for x in range(grid.width):
        if (x, y) in loop_positions:
            continue

        if path.contains_point((x, y)):
            enclosed_tiles.add((x, y))

print(len(enclosed_tiles))
