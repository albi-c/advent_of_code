from advent import Advent, Grid


grid = Grid(Advent().read(), lambda ch: 0 if ch == '.' else 1 if ch == '>' else 2)


def step() -> bool:
    global grid
    moved = False
    new_grid = Grid([[0 for _ in range(grid.width)] for _ in range(grid.height)])
    for x in range(grid.width):
        for y in range(grid.height):
            if grid[(x, y)] == 1:
                dx = (x + 1) % grid.width
                if grid[(dx, y)] == 0:
                    new_grid[(dx, y)] = 1
                    moved = True
                else:
                    new_grid[(x, y)] = 1
    for x in range(grid.width):
        for y in range(grid.height):
            if grid[(x, y)] == 2:
                dy = (y + 1) % grid.height
                if grid[(x, dy)] != 2 and new_grid[(x, dy)] != 1:
                    new_grid[(x, dy)] = 2
                    moved = True
                else:
                    new_grid[(x, y)] = 2
    grid = new_grid
    return moved


steps = 0
while True:
    steps += 1
    if not step():
        print(steps)
        break
