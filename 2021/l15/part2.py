from ..advent import Advent, Grid

advent = Advent(15, 1)

def wrap_around(n):
    while n > 9:
        n -= 9
    
    return n

lns = advent.read.lines()
data = "\n".join(["".join([str(wrap_around((int(n) + i + j // len(lns)))) for i in range(5) for n in row.strip()]) for j, row in enumerate(lns * 5)])

grid = Grid([[int(val) for val in row.strip()] for row in data.splitlines()])

def pathfind(grid: Grid, start):
    vertices = set()
    dist = {}
    prev = {}
    
    for k, _ in grid.items():
        dist[k] = 1 << 30
        prev[k] = None
        vertices.add(k)
    
    dist[start] = 0

    while len(vertices) > 0:
        u = min(vertices, key = lambda x: dist[x])
        vertices.remove(u)

        for n, v in grid.neighbors(u):
            if n in vertices:
                alt = dist[u] + v
                if alt < dist[n]:
                    dist[n] = alt
                    prev[n] = u
    
    return dist, prev

dist, _ = pathfind(grid, (0, 0))

advent.solution(dist[(grid.width - 1, grid.height - 1)])
