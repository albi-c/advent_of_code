from ..advent import Advent, vec2

advent = Advent(21, 2)

p1, p2 = advent.read.lines(lambda x: int(x.split(" ")[-1]))
p1s, p2s = 0, 0

def roll(n: int, turn: int, p1: int, p2: int, p1s: int, p2s: int) -> vec2:
    p1 += n
    while p1 > 10:
        p1 -= 10
    
    p1s += p1
    
    p1, p2 = p2, p1
    p1s, p2s = p2s, p1s
    
    if p1s >= 21:
        return vec2(1, 0)
    elif p2s >= 21:
        return vec2(0, 1)
    
    wins = vec2()
    for i in range(1, 4):
        wins += roll(i, 1 - turn, p1, p2, p1s, p2s)
    
    return wins

wins = vec2()
for i in range(1, 4):
    wins += roll(i, 0, p1, p2, p1s, p2s)

print(p1s, p2s)
advent.solution(max(p1s, p2s))
