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

grid = Grid.parse(Advent().read())

print(sum(1 for _ in grid.sequence_search("XMAS", True)))

print(sum(sum(1 for _ in grid.subgrid_search(Grid([[a, None, b],
                                                   [None, "A", None],
                                                   [c, None, d]]),
                                             lambda x, y: y is None or x == y))
          for a, b, c, d in ("MMSS", "MSMS", "SSMM", "SMSM")))
