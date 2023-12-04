from advent import Advent, X, Stream

import functools


advent = Advent()

data: list[int]
data = (advent.read.lines().map(X.replace("  ", " ")).split(": ").stream().map(X[1]).map(X.split(" | ")).flatten()
        .map(X.split(" ")).map(X.map(int)).map(set).chunks(2).unpack_map(lambda a, b: a & b).map(len).to(list))

print(Stream(data).map(lambda x: 0 if x == 0 else 1 << (x - 1)).sum())


def merge_winning(a: dict[int, int], b: dict[int, int]) -> dict[int, int]:
    return {k: a.get(k, 0) + b.get(k, 0) for k in a.keys() | b.keys()}


@functools.cache
def get_cards(card_id: int) -> dict[int, int]:
    cards = {card_id: 1}
    winning = data[card_id]
    for card in range(card_id + 1, card_id + winning + 1):
        cards = merge_winning(cards, get_cards(card))

    return cards


cards_sum = {}
for i in range(len(data)):
    cards_sum = merge_winning(cards_sum, get_cards(i))
print(sum(cards_sum.values()))
