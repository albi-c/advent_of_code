from advent import Advent


min_value, max_value = Advent().read.split("-").map(int)()

count = 0
for n in range(min_value, max_value + 1):
    s = str(n)
    prev = -1
    good = False
    for i, ch in enumerate(s):
        m = int(ch)
        if m == prev:
            good = True
        if m < prev:
            good = False
            break
        prev = m
    if good:
        count += 1
print(count)

count = 0
for n in range(min_value, max_value + 1):
    s = str(n)
    prev = -1
    good = False
    for i, ch in enumerate(s):
        m = int(ch)
        if m == prev and (i <= 1 or s[i - 2] != ch) and (i >= 5 or s[i + 1] != ch):
            good = True
        if m < prev:
            good = False
            break
        prev = m
    if good:
        count += 1
print(count)
