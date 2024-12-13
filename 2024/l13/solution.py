from advent import Advent, ivec2
import z3


input_data: list[list[ivec2]] = [[ivec2(*(int(x[2:]) for x in ln.split(": ")[1].split(", "))) for ln in block]
                                 for block in Advent().read.blocks().lines()()]


def solve(machine: list[ivec2], add: int) -> int:
    a, b, target = machine
    solver = z3.Optimize()

    na = z3.Int("na")
    solver.add(na >= 0)
    nb = z3.Int("nb")
    solver.add(nb >= 0)

    solver.add(na * a.x + nb * b.x == target.x + add)
    solver.add(na * a.y + nb * b.y == target.y + add)

    cost = z3.Int("cost")
    solver.add(cost == 3 * na + nb)
    solver.minimize(cost)

    if solver.check() == z3.sat:
        return solver.model().eval(cost).as_long()
    return 0


print(sum(solve(machine, 0) for machine in input_data))
print(sum(solve(machine, 10000000000000) for machine in input_data))
