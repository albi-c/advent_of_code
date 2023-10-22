from advent import Advent, X, Stream

advent = Advent()

data = advent.read.lines()()

print(sum(sum(s.count(v) for v in "aeiou") >= 3 and Stream(s).window(2).map(X==X).any() and not any(
    n in s for n in ("ab", "cd", "pq", "xy")) for s in data))

print(sum(Stream(s).window(3).chain_map(tuple, lambda t: t[0] == t[2]).any() and any(
    s.count(p) >= 2 for p in Stream(s).window(2).map("".join)) for s in data))
