from advent import Advent, Grid, ivec2
from collections import defaultdict

DIRECTIONS = (
    ivec2(1, 0),
    ivec2(0, 1),
    ivec2(-1, 0),
    ivec2(0, -1)
)

grid = Grid.parse(Advent().read())
start = next(grid.search("S"))
grid[start] = "."
end = next(grid.search("E"))
grid[end] = "."
start_dir = 0

dist = defaultdict(lambda: 1 << 60)
prev = defaultdict(set)
q = set()
for pos, val in grid.enumerate():
    if val == ".":
        for i in range(4):
            q.add((pos, i))
dist[(start, start_dir)] = 0
while q:
    u = min(q, key=lambda pair: dist[pair])
    q.remove(u)
    pos, dir_ = u
    for v in ((pos + DIRECTIONS[dir_], dir_), (pos, (dir_ + 1) & 3), (pos, (dir_ - 1) & 3)):
        if grid[pos] == "#":
            continue
        if v not in q:
            continue
        alt = dist[u] + (1000 if v[1] != dir_ else 1)
        if alt < dist[v]:
            dist[v] = alt
            prev[v] = {u}
            q.add(v)
        elif alt == dist[v]:
            prev[v].add(u)
print(min(dist[(end, i)] for i in range(4)))

seats = set()
seat_positions = set()
for i in range(4):
    seats.add((end, i))
    stack = [(end, i)]
    while stack:
        state = stack.pop(-1)
        for s in prev[state]:
            if s not in seats:
                seats.add(s)
                stack.append(s)
                seat_positions.add(s[0])
print(len(seat_positions))
