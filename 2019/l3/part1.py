from ..advent import Advent, vec2

advent = Advent(3)

wire1, wire2 = advent.read.lines(lambda line: line.split(","))

DIRECTIONS = {
    "R": vec2(1, 0),
    "L": vec2(-1, 0),
    "U": vec2(0, 1),
    "D": vec2(0, -1)
}


def list_positions(wire: list[str]) -> list[vec2]:
    positions = []

    pos = vec2()
    for move in wire:
        direction = move[0]
        amount = int(move[1:])
        pos += DIRECTIONS[direction] * amount

    return positions
