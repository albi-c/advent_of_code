from ..advent import Advent

advent = Advent(5)

raw_crates, raw_moves = [block.splitlines() for block in advent.read.blocks()]

cols = int(raw_crates[-1][-1])
raw_crates = raw_crates[-2::-1]

crates = [[] for _ in range(cols)]

for row in raw_crates:
    for crate, i in enumerate(range(1, cols * 4, 4)):
        if i < len(row) and row[i] != " ":
            crates[crate].append(row[i])

moves = [[int(n) for n in move.split()[1::2]] for move in raw_moves]

for n, f, t in moves:
    crates[t - 1] += crates[f - 1][-n:][::-1]
    crates[f - 1] = crates[f - 1][:-n]

advent.solution("".join(col[-1] for col in crates))
