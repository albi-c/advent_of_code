from advent import Advent, Stream


CARDS = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"][::-1]
CARDS_2 = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"][::-1]


advent = Advent()

games: list[tuple[str, str]] = advent.read.lines().split(" ").stream().unpack_map(lambda hand, bid: (hand, int(bid))).to(list)


def get_hand_type(hand: str) -> int:
    hand_set = set(hand)
    hand_counts = {card: hand.count(card) for card in hand_set}

    if 5 in hand_counts.values():
        return 6
    elif 4 in hand_counts.values():
        return 5
    elif 3 in hand_counts.values():
        if 2 in hand_counts.values():
            return 4
        return 3
    elif Stream(hand_counts.values()).filter(lambda x: x == 2).len() == 2:
        return 2
    elif 2 in hand_counts.values():
        return 1
    return 0


def get_hand_type_2(hand: str) -> int:
    hand_set = set(hand)
    hand_counts = {card: hand.count(card) for card in hand_set}

    occurence_ordered = sorted(hand_counts.keys(), key=lambda k: hand_counts[k], reverse=True)
    most_occured = occurence_ordered[0]
    if most_occured == "J":
        if len(occurence_ordered) == 1:
            return 6
        most_occured = occurence_ordered[1]
    hand_counts[most_occured] += hand_counts.get("J", 0)
    hand_counts["J"] = 0

    if 5 in hand_counts.values():
        return 6
    elif 4 in hand_counts.values():
        return 5
    elif 3 in hand_counts.values():
        if 2 in hand_counts.values():
            return 4
        return 3
    elif Stream(hand_counts.values()).filter(lambda x: x == 2).len() == 2:
        return 2
    elif 2 in hand_counts.values():
        return 1
    return 0


def hand_comparator(hand: str) -> int:
    return (get_hand_type(hand) << 32) + sum(CARDS.index(card) << (i * 4) for i, card in enumerate(reversed(hand)))


def hand_comparator_2(hand: str) -> int:
    return (get_hand_type_2(hand) << 32) + sum(CARDS_2.index(card) << (i * 4) for i, card in enumerate(reversed(hand)))


sorted_games = sorted(games, key=lambda game: hand_comparator(game[0]))

print(sum(bid * i for i, (_, bid) in enumerate(sorted_games, start=1)))


sorted_games_2 = sorted(games, key=lambda game: hand_comparator_2(game[0]))

print(sum(bid * i for i, (_, bid) in enumerate(sorted_games_2, start=1)))
