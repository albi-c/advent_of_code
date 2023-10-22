from advent import Advent, ivec2, Stream

DIRECTIONS = {
    "^": ivec2(0, 1),
    "v": ivec2(0, -1),
    "<": ivec2(-1, 0),
    ">": ivec2(1, 0)
}

advent = Advent()

data = list(advent.read())

pos = ivec2(0)
visited = {(0, 0)}
for d in data:
    pos += DIRECTIONS[d]
    visited.add(tuple(pos))
print(len(visited))

santa, robo = ivec2(0), ivec2(0)
visited = {(0, 0)}
for s, r in Stream(data).chunks(2):
    santa += DIRECTIONS[s]
    robo += DIRECTIONS[r]
    visited.add(tuple(santa))
    visited.add(tuple(robo))
print(len(visited))
