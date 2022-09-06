from ..advent import Advent, Grid

advent = Advent(15, 1)

grid = advent.read.grid(int)

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
