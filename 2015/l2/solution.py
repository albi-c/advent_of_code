from advent import Advent, X, Stream

advent = Advent()

def get_surface(dims: tuple[int, int, int]) -> int:
    return Stream.of_combinations(dims, 2).chain_map(X*X, X*2).sum() + (Stream(dims).prod() // max(dims))

def get_ribbon(dims: tuple[int, int, int]) -> int:
    return (sum(dims) - max(dims)) * 2 + Stream(dims).prod()

data = advent.read.stream().split("\n").chain_map("".join, X.split("x"), X.map(int), tuple).to(list)

print(Stream(data).map(get_surface).sum())
print(Stream(data).map(get_ribbon).sum())
