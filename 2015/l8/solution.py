from advent import Advent

advent = Advent()

data = advent.read.lines()()

def difference(ln: str) -> int:
    return len(ln) - len(eval(ln))

def encoded_difference(ln: str) -> int:
    replaced = ln.replace("\\", "\\\\").replace("\"", "\\\"")
    return len(replaced) + 2 - len(ln)

print(sum(map(difference, data)))
print(sum(map(encoded_difference, data)))
