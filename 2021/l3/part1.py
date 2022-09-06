from ..advent import Advent

advent = Advent(3, 1)

data = advent.read.lines(lambda x: [int(val) for val in list(x) if val.strip()][::-1])
dl = len(data[0])

counts = {i: [0, 0] for i in range(dl)}

for num in data:
    for i in range(dl):
        counts[i][num[i]] += 1

gam = 0
eps = 0

for i in range(dl):
    gam |= int(counts[i][0] < counts[i][1]) << i
    eps |= int(counts[i][0] > counts[i][1]) << i

advent.solution(gam * eps)
