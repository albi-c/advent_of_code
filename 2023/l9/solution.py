from advent import Advent, Util


advent = Advent()

data: list[list[int]] = advent.read.lines().split().map(int)()


def get_next_value(seq: list[int]) -> int:
    if all(x == 0 for x in seq):
        return 0

    new_seq = [b - a for a, b in Util.window(seq, 2)]
    return seq[-1] + get_next_value(new_seq)


print(sum(map(get_next_value, data)))


print(sum(get_next_value(seq[::-1]) for seq in data))
