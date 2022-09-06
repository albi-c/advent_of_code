from ..advent import Advent

advent = Advent(22, 2)

deck1, deck2 = [list(map(int, block.splitlines()[1:])) for block in advent.read.blocks()]

def score(deck):
    return sum([n * (i + 1) for i, n in enumerate(deck[::-1])])

def combat(d1, d2):
    rounds = set()

    while len(d1) != 0 and len(d2) != 0:
        if (tuple(d1), tuple(d2)) in rounds:
            return 1, score(d1)
        
        rounds.add((tuple(d1), tuple(d2)))
        
        c1 = d1.pop(0)
        c2 = d2.pop(0)

        if len(d1) >= c1 and len(d2) >= c2:
            w, _ = combat(d1.copy(), d2.copy())

            if w == 1:
                d1 += [c1, c2]
            else:
                d2 += [c2, c1]
        else:
            if c1 > c2:
                d1 += [c1, c2]
            else:
                d2 += [c2, c1]
    
    if len(d1) == 0:
        return 2, score(d2)
    else:
        return 1, score(d1)

advent.solution(combat(deck1, deck2)[1])
