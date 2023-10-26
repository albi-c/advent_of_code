from advent import Advent

advent = Advent()

data = {s[1]: s[0].split() for s in [ln.split(" -> ") for ln in advent.read.lines()()]}
value_cache = {}

OPERATORS = {
    "AND": lambda a, b: a & b,
    "OR": lambda a, b: a | b,
    "LSHIFT": lambda a, b: a << (b & 0xffff),
    "RSHIFT": lambda a, b: a >> (b & 0xffff)
}

def get_value(val: str) -> int:
    global value_cache
    try:
        return int(val)
    except ValueError:
        if val not in value_cache:
            value_cache[val] = evaluate(data[val])
        return value_cache[val]

def evaluate(operation: list[str]) -> int:
    if len(operation) == 1:
        return get_value(operation[0])

    elif len(operation) == 2:
        # must be NOT
        return ~get_value(operation[1])

    elif len(operation) == 3:
        return OPERATORS[operation[1]](get_value(operation[0]), get_value(operation[2]))

a_value = get_value("a") & 0xffff
print(a_value)

value_cache.clear()
data["b"] = [str(a_value)]
print(get_value("a") & 0xffff)
