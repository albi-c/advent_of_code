from ..advent import Advent, vec2

advent = Advent(17, 2)

data = [[int(v) for v in p.split("=")[1].split("..")] for p in advent.read().split(" ", 1)[1].split(", ")]
p1 = vec2(data[0][0], data[1][0])
p2 = vec2(data[0][1], data[1][1])

def simulate(vel: vec2, p1: vec2, p2: vec2):
    pos = vec2()

    ly = min(p1.y, p2.y)
    ux = max(p1.x, p2.x)
    
    hp = 0

    while pos.y > ly:
        pos += vel

        if vel.x > 0:
            vel.x -= 1
        elif vel.x < 0:
            vel.x += 1
        
        vel.y -= 1

        if pos.y > hp:
            hp = pos.y

        if pos.in_bounds(p1, p2):
            return True, hp
        
        if pos.x > ux:
            return False, 0
    
    return False, 0

n = 0
for x in range(1000):
    for y in range(-100, 1000):
        s, h = simulate(vec2(x, y), p1, p2)
        if s:
            n += 1

advent.solution(n)
