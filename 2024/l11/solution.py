from advent import Advent

from collections import defaultdict


input_data: list[int] = Advent().read.split(" ").map(int)()


def solve(n: int):
    stone_counts: defaultdict[int, int] = defaultdict(int)
    for stone in input_data:
        stone_counts[stone] += 1
    for _ in range(n):
        new = defaultdict(int)
        for stone, n in stone_counts.items():
            if stone == 0:
                new[1] += n
            elif len(string := str(stone)) % 2 == 0:
                new[int(string[:len(string)//2])] += n
                new[int(string[len(string)//2:])] += n
            else:
                new[2024 * stone] += n
        stone_counts = new
    print(sum(stone_counts.values()))


solve(25)
solve(75)
