from collections import defaultdict

from ..advent import Advent

advent = Advent(5, 1)

grid = defaultdict(int)

for ln in advent.read.lines():
    p1, p2 = [[int(val) for val in pos.split(",")] for pos in ln.split(" -> ")]

    x1 = p1[0]
    y1 = p1[1]

    x2 = p2[0]
    y2 = p2[1]

    if x1 == x2 or y1 == y2:
        if x1 > x2:
            x1, x2 = x2, x1
        
        if y1 > y2:
            y1, y2 = y2, y1

    if x1 == x2:
        for y in range(y1, y2 + 1):
            grid[(x1, y)] += 1
    
    elif y1 == y2:
        for x in range(x1, x2 + 1):
            grid[(x, y1)] += 1
    
    else:
        x, y = x1, y1

        while x != x2 and y != y2:
            grid[(x, y)] += 1

            if x < x2:
                x += 1
            elif x > x2:
                x -= 1
            
            if y < y2:
                y += 1
            elif y > y2:
                y -= 1
        
        grid[(x, y)] += 1

count = 0

for k, v in grid.items():
    if v >= 2:
        count += 1

advent.solution(count)
