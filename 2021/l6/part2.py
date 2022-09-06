from ..advent import Advent

advent = Advent(6, 2)

fishes = advent.read.separated(",", int)

counts = [0 for _ in range(9)]

for fish in fishes:
    counts[fish] += 1

for _ in range(256):
    new = counts[0]

    counts[0] = counts[1]
    counts[1] = counts[2]
    counts[2] = counts[3]
    counts[3] = counts[4]
    counts[4] = counts[5]
    counts[5] = counts[6]
    counts[6] = counts[7] + new
    counts[7] = counts[8]
    counts[8] = new

advent.solution(sum(counts))
