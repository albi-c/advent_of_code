from advent import Advent, X, Stream


LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14
}


advent = Advent()


def parse(line: str) -> list[dict[str, int]]:
    rounds = []
    for r in line.split("; "):
        rounds.append({name: int(value) for value, name in map(X.split(" "), r.split(", "))})
    return rounds


data = [(int(id_.split()[1]), parse(ln)) for id_, ln in advent.read.lines().split(": ")()]

print(Stream(data).filter(lambda t: all(all(v <= LIMITS[k] for k, v in r.items()) for r in t[1])).map(X[0]).sum())


def merge_rounds(a: dict[str, int], b: dict[str, int]) -> dict[str, int]:
    return {k: max(a.get(k, 0), b.get(k, 0)) for k in a.keys() | b.keys()}


def get_power(cubes: dict[str, int]) -> int:
    return Stream(cubes.values()).prod()


print(sum(get_power(Stream(g).reduce(merge_rounds, {})) for _, g in data))
