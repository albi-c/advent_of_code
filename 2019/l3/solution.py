from advent import Advent, ivec2


wire_1, wire_2 = Advent().read.lines().map(lambda ln: ln.split(","))()

DIRECTIONS = {
    "R": ivec2(1, 0),
    "L": ivec2(-1, 0),
    "U": ivec2(0, 1),
    "D": ivec2(0, -1)
}


def list_positions(wire: list[str]) -> tuple[list[ivec2], dict[ivec2, int]]:
    positions = []
    distances = {}

    pos = ivec2()
    distance = 0
    for move in wire:
        direction = move[0]
        amount = int(move[1:])
        offset = DIRECTIONS[direction]
        for _ in range(amount):
            pos = pos + offset
            distance += 1
            positions.append(pos)
            if pos not in distances:
                distances[pos] = distance

    return positions, distances


positions_1, distances_1 = list_positions(wire_1)
positions_2, distances_2 = list_positions(wire_2)
intersections = set(positions_1) & set(positions_2)

print(min(abs(pos.x) + abs(pos.y) for pos in intersections))
print(min(distances_1[pos] + distances_2[pos] for pos in intersections))
