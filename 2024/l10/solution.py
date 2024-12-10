from advent import Advent, Grid, ivec2, any_sum, set_sum


grid = Grid.parse(Advent().read(), int)


def find_paths(pos: ivec2) -> set[ivec2]:
    if grid[pos] == 9:
        return {pos}

    return set_sum(map(find_paths, grid.neighbors_search(pos, grid[pos] + 1)))


def find_distinct_paths(pos: ivec2, path: tuple[ivec2, ...]) -> set[tuple[ivec2, ...]]:
    if grid[pos] == 9:
        return {path}

    return set_sum(find_distinct_paths(p, path + (p,)) for p in grid.neighbors_search(pos, grid[pos] + 1))


result = any_sum(ivec2(len(find_paths(position)),
                       len(find_distinct_paths(position, ())))
                 for position in grid.search(0))
print(result.x)
print(result.y)
