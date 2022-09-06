from ..advent import Advent

advent = Advent(22, 1)

deck1, deck2 = [list(map(int, block.splitlines()[1:])) for block in advent.read.blocks()]

while len(deck1) != 0 and len(deck2) != 0:
    c1 = deck1.pop(0)
    c2 = deck2.pop(0)

    if c1 > c2:
        deck1 += [c1, c2]
    else:
        deck2 += [c2, c1]

if len(deck1) == 0:
    advent.solution(sum([n * (i + 1) for i, n in enumerate(deck2[::-1])]))
else:
    advent.solution(sum([n * (i + 1) for i, n in enumerate(deck1[::-1])]))
