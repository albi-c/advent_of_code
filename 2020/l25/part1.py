from advent import Advent

pub1, pub2 = Advent().read.lines().map(int)()


def find_loop_size(num: int) -> int:
    x = 1
    n = 0
    while x != num:
        n += 1
        x *= 7
        x %= 20201227
    return n


def extend_key(key: int, n: int) -> int:
    x = 1
    for _ in range(n):
        x *= key
        x %= 20201227
    return x


print(extend_key(pub1, find_loop_size(pub2)))
