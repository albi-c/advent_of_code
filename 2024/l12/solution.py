from advent import Advent, Grid, ivec2

grid = Grid.parse(Advent().read())

result = 0
groups = Grid.of(0, *grid.size)
index = 0
areas = []
for pos, mark in groups.enumerate():
    if mark != 0:
        continue

    index += 1

    ch = grid[pos]
    to_visit = [pos]
    visited = {pos}
    area = 0
    border = 0
    while to_visit:
        new = []
        for p in to_visit:
            area += 1
            groups[p] = index
            for o in Grid.NEIGHBORS:
                n = p + o
                if grid.inside(n) and grid[n] == ch:
                    if n not in visited:
                        new.append(n)
                        visited.add(n)
                else:
                    border += 1
        to_visit = new
    result += area * border
    areas.append(area)
print(result)


def search_cmp(idx: int):
    def inner(a: int, b: int) -> bool:
        return (b == 0 and a != idx) or a == b
    return inner


groups_border = Grid([[groups[x-1, y-1] if groups.inside((x-1, y-1)) else 0
                       for x in range(groups.width + 2)] for y in range(groups.height + 2)])

result2 = 0
for i, area in enumerate(areas, start=1):
    corners = 0
    func = search_cmp(i)

    corners += sum(1 for _ in groups_border.subgrid_search(Grid([[i, i], [i, 0]]), func))
    corners += sum(1 for _ in groups_border.subgrid_search(Grid([[i, i], [0, i]]), func))
    corners += sum(1 for _ in groups_border.subgrid_search(Grid([[i, 0], [i, i]]), func))
    corners += sum(1 for _ in groups_border.subgrid_search(Grid([[0, i], [i, i]]), func))

    corners += sum(1 for _ in groups_border.subgrid_search(Grid([[i, 0], [0, 0]]), func))
    corners += sum(1 for _ in groups_border.subgrid_search(Grid([[0, i], [0, 0]]), func))
    corners += sum(1 for _ in groups_border.subgrid_search(Grid([[0, 0], [i, 0]]), func))
    corners += sum(1 for _ in groups_border.subgrid_search(Grid([[0, 0], [0, i]]), func))

    corners += 2 * sum(1 for _ in groups_border.subgrid_search(Grid([[0, i], [i, 0]]), func))
    corners += 2 * sum(1 for _ in groups_border.subgrid_search(Grid([[i, 0], [0, i]]), func))

    result2 += area * corners

print(result2)
