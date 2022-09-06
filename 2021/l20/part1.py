from ..advent import Advent, vec2

NEIGHBORS = [
    vec2(-1, -1),
    vec2(0, -1),
    vec2(1, -1),
    vec2(-1, 0),
    vec2(0, 0),
    vec2(1, 0),
    vec2(-1, 1),
    vec2(0, 1),
    vec2(1, 1)
]

advent = Advent(20, 1)

ias, image = advent.read.blocks()
ias = [ch == "#" for ch in ias]
img = set()
for y, row in enumerate(image.splitlines()):
    for x, ch in enumerate(row):
        if ch == "#":
            img.add((x, y))

def enhance(ias, img, size=1, inf=False):
    new = set()

    lx = min(img, key=lambda x: x[0])[0]
    mx = max(img, key=lambda x: x[0])[0]
    ly = min(img, key=lambda x: x[1])[1]
    my = max(img, key=lambda x: x[1])[1]

    for x in range(lx - size, mx + 1 + size):
        for y in range(ly - size, my + 1 + size):
            num = 0
            for n in NEIGHBORS:
                nt = (n + vec2(x, y)).tuple()
                num |= nt in img
                num |= (nt[0] < lx or nt[0] > mx or nt[1] < lx or nt[1] > mx) and inf
                num <<= 1
            num >>= 1

            if ias[num]:
                new.add((x, y))
    
    return new, size + 1, not inf

img, size, inf = enhance(ias, img)
img, size, inf = enhance(ias, img, size, inf)

advent.solution(len(img))
