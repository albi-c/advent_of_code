from advent import Advent


type Segment = tuple[int, int]

input_data: list[Segment] = [(i // 2 if i % 2 == 0 else -1, x) for i, x in enumerate(map(int, Advent().read()))]
if input_data[-1][0] == -1:
    input_data.pop(-1)

data = [y for x, n in input_data for y in (x for _ in range(n))]
for i, x in enumerate(data):
    if x == -1:
        while data[-1] == -1:
            data.pop(-1)
        data[i] = data.pop(-1)
print(sum(x * y for x, y in enumerate(data)))

segments = input_data.copy()
max_id = segments[-1][0]

for id_ in range(max_id, -1, -1):
    i = len(segments)
    while i > 0:
        i -= 1
        if segments[i][0] == id_:
            break
    assert i >= 0
    to_fit = segments[i]
    for j, seg in enumerate(segments[:i]):
        if seg[0] == -1 and seg[1] >= to_fit[1]:
            segments[j] = to_fit
            segments[i] = (-1, to_fit[1])
            diff = seg[1] - to_fit[1]
            if diff > 0:
                segments.insert(j + 1, (-1, diff))
            break

print(sum(x * y for x, y in enumerate(y for x, n in segments for y in (x for _ in range(n))) if y != -1))
