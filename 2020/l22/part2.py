import functools

from advent import Advent

deck1, deck2 = (tuple(map(int, block.splitlines()[1:])) for block in Advent().read.blocks()())


type Deck = tuple[int, ...]


def score(deck: Deck) -> int:
    return sum(n * i for i, n in enumerate(reversed(deck), start=1))


@functools.cache
def combat(d1: Deck, d2: Deck) -> tuple[int, Deck]:
    seen: set[tuple[Deck, Deck]] = set()

    while len(d1) != 0 and len(d2) != 0:
        state = (d1, d2)
        if state in seen:
            return 1, d1
        seen.add(state)

        c1 = d1[0]
        d1 = d1[1:]

        c2 = d2[0]
        d2 = d2[1:]

        if len(d1) >= c1 and len(d2) >= c2:
            w, _ = combat(d1[:c1], d2[:c2])

            if w == 1:
                d1 = d1 + (c1, c2)
            else:
                d2 = d2 + (c2, c1)

        else:
            if c1 > c2:
                d1 = d1 + (c1, c2)
            else:
                d2 = d2 + (c2, c1)

    if len(d1) == 0:
        return 2, d2
    else:
        return 1, d1


print(score(combat(deck1, deck2)[1]))
