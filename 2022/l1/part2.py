from ..advent import Advent

advent = Advent(1)

data = [list(map(int, block.splitlines())) for block in advent.read.blocks()]

advent.solution(sum(sorted(map(sum, data))[-3:]))
