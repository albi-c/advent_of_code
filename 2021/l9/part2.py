from ..advent import Advent, Grid

advent = Advent(9, 2)

grid = Grid(advent.read.lines(lambda line: list(map(int, list(line)))))

def find_basin(grid, position, basin = None):
    basin = basin if basin is not None else set()

    if grid[position] == 9:
        return set()
    
    basin.add(position)

    for pos, _ in grid.neighbors(position):
        if pos not in basin:
            find_basin(grid, pos, basin)
    
    return basin

basins = []
for pos, _ in grid.items():
    basin = find_basin(grid, pos)
    basins.append(basin)

basins = list(map(len, advent.util.remove_duplicates(basins)))
basins.sort()

print(basins[-1] * basins[-2] * basins[-3])
