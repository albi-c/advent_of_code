from advent import Advent
import z3

result_1 = []
a = int(Advent().read.lines()()[0].rsplit(" ", 1)[1])
while a != 0:
    b = a & 7
    b ^= 1
    c = a >> b
    b = b ^ c
    a = a >> 3
    b = b ^ 6
    result_1.append(b & 7)
print(",".join(map(str, result_1)))


code = list(map(int, Advent().read.lines()()[-1].split(" ", 1)[1].split(",")))

solver = z3.Optimize()

start_a = z3.BitVec("a", 128)
solver.minimize(start_a)
a = start_a
for x in code:
    b = a & 7
    b ^= 1
    c = a >> b
    b = b ^ c
    a = a >> 3
    b = b ^ 6
    solver.add(b & 7 == x)
solver.add(a == 0)

assert solver.check() == z3.sat
print(solver.model().eval(start_a).as_long())
