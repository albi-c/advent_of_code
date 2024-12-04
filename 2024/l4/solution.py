from advent import Advent, Grid, ivec2


DIRECTIONS = (
    ivec2(1, 0),
    ivec2(1, 1),
    ivec2(1, -1),
    ivec2(0, 1),
    ivec2(0, -1),
    ivec2(-1, 0),
    ivec2(-1, 1),
    ivec2(-1, -1)
)

grid = Grid(Advent().read())

count = 0
for x in range(grid.width):
    for y in range(grid.height):
        pos = ivec2(x, y)
        if grid[pos] != "X":
            continue
        for d in DIRECTIONS:
            if not grid.inside(pos + 3 * d):
                continue
            fail = False
            for i, ch in enumerate("MAS", start=1):
                if grid[pos + i * d] != ch:
                    fail = True
                    break
            if not fail:
                count += 1
print(count)

count = 0
for x in range(grid.width):
    for y in range(grid.height):
        pos = ivec2(x, y)
        if grid[pos] != "A":
            continue
        fail = False
        for o in (ivec2(1, 1), ivec2(-1, 1)):
            if not grid.inside(pos + o) or not grid.inside(pos - o):
                fail = True
                break
            if {grid[pos + o], grid[pos - o]} != set("MS"):
                fail = True
                break
        if not fail:
            count += 1
print(count)
