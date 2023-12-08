from advent import Advent

import itertools
import math


advent = Advent()

directions, node_data = advent.read.blocks()()
nodes = {ln[0:3]: (ln[7:10], ln[12:15]) for ln in node_data.splitlines()}


def get_moves(pos: str, target: str) -> int:
    moves = 0
    for move in itertools.cycle(directions):
        if pos == target:
            return moves

        moves += 1
        pos = nodes[pos][0 if move == "L" else 1]


def get_moves_to_z(pos: str) -> int:
    moves = 0
    for move in itertools.cycle(directions):
        if pos.endswith("Z"):
            return moves

        moves += 1
        pos = nodes[pos][0 if move == "L" else 1]


def get_multi_moves(positions: list[str]) -> int:
    moves = 0
    for move in itertools.cycle(directions):
        if all(pos.endswith("Z") for pos in positions):
            return moves

        moves += 1
        positions = [nodes[pos][0 if move == "L" else 1] for pos in positions]


print(get_moves("AAA", "ZZZ"))


starts = [pos for pos in nodes.keys() if pos.endswith("A")]

print(math.lcm(*[get_moves_to_z(start) for start in starts]))
