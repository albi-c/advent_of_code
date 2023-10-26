from advent import Advent, Util

advent = Advent()

MATCH = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

MATCH_2 = {
    "children": lambda x: x == 3,
    "cats": lambda x: x > 7,
    "samoyeds": lambda x: x == 2,
    "pomeranians": lambda x: x < 3,
    "akitas": lambda x: x == 0,
    "vizslas": lambda x: x == 0,
    "goldfish": lambda x: x < 5,
    "trees": lambda x: x > 3,
    "cars": lambda x: x == 2,
    "perfumes": lambda x: x == 1,
}

data = [(int(ln[1][:-1]), [(k[:-1], int(v.replace(",", ""))) for k, v in Util.chunks(ln[2:], 2)]) for ln in advent.read.lines().split()()]

for i, d in data:
    ok = True
    for k, v in d:
        if MATCH[k] != v:
            ok = False
            break
    if ok:
        print(i)
        break

for i, d in data:
    ok = True
    for k, v in d:
        if not MATCH_2[k](v):
            ok = False
            break
    if ok:
        print(i)
        break
