from advent import Advent, ivec2, VarGrid
import math
import itertools

robots: list[list[ivec2]] = [[ivec2(*map(int, part[2:].split(","))) for part in ln.split(" ")]
                             for ln in Advent().read.lines()()]
grid_size = ivec2(11, 7) if len(robots) == 12 else ivec2(101, 103)
half_grid = grid_size // 2

quadrant_counts = [0 for _ in range(4)]
for pos, vel in robots:
    final = pos + 100 * vel
    final.x %= grid_size.x
    final.y %= grid_size.y
    qx = 0
    if final.x > half_grid.x:
        qx = 1
    elif final.x == half_grid.x:
        continue
    qy = 0
    if final.y > half_grid.y:
        qy = 2
    elif final.y == half_grid.y:
        continue
    quadrant_counts[qx | qy] += 1
print(math.prod(quadrant_counts))

for time in itertools.count(1):
    grid = VarGrid()
    positions = set()
    for pos, vel in robots:
        pos.x = (pos.x + vel.x) % grid_size.x
        pos.y = (pos.y + vel.y) % grid_size.y
        grid[pos] = "#"
        positions.add(ivec2(pos))
    if len(positions) == len(robots):
        grid.draw()
        print(time)
        break
