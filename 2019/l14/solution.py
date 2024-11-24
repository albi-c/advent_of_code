from advent import Advent, NumberObject

from collections import defaultdict
import math


reactions = {}
for left, right in Advent().read.lines().split(" => ")():
    spl = right.split(" ")
    reactions[spl[1]] = (int(spl[0]), tuple((inp.split(" ")[1], int(inp.split(" ")[0])) for inp in left.split(", ")))


def ensure_amount(comp: str, amount: int, avail: defaultdict[str, int], used_ore: NumberObject[int]):
    if avail[comp] >= amount:
        return

    needed = amount - avail[comp]

    if comp == "ORE":
        used_ore.add(needed)
        avail[comp] += needed
        return

    reaction = reactions[comp]
    batches = math.ceil(needed / reaction[0])
    for i, a in reaction[1]:
        ensure_amount(i, a * batches, avail, used_ore)
        avail[i] -= a * batches
        assert avail[i] >= 0
    avail[comp] += batches * reaction[0]


used_ore_counter = NumberObject(0)
ensure_amount("FUEL", 1, defaultdict(int), used_ore_counter)
print(used_ore_counter.v)


used_ore_counter = NumberObject(0)
# binary search by hand
ensure_amount("FUEL", 6216589, defaultdict(int), used_ore_counter)
print(used_ore_counter.v)
