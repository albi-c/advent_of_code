from ..advent import Advent

advent = Advent(20)

values: list[tuple[int, int]] = [(i, int(ln)) for i, ln in enumerate(advent.read.lines())]
