from ..advent import Advent

advent = Advent(3, 2)

data = advent.read.lines(lambda x: [int(val) for val in list(x) if val.strip()][::-1])
dl = len(data[0])

def count(data, dl):
    counts = {i: [0, 0] for i in range(dl)}

    for num in data:
        for i in range(dl):
            counts[i][num[i]] += 1
    
    return counts

def rf(lst, v0, v1):
    l = lst.copy()

    for pos in range(dl - 1, -1, -1):
        if len(l) <= 1:
            break

        c = count(l, len(l[0]))

        if c[pos][0] <= c[pos][1]:
            l = list(filter(lambda x: x[pos] == v1, l))
        else:
            l = list(filter(lambda x: x[pos] == v0, l))
    
    return int("".join([str(x) for x in l[0][::-1]]), base=2)

og = rf(data, 0, 1)
cs = rf(data, 1, 0)

advent.solution(og * cs)
