from advent import Advent


a, b = [], []
for x, y in Advent().read.lines().map(lambda ln: ln.split("   "))():
    a.append(int(x))
    b.append(int(y))
a.sort()
b.sort()


print(sum(abs(x - y) for x, y in zip(a, b)))
print(sum(x * b.count(x) for x in a))
