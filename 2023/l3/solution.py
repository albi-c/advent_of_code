from advent import Advent, ivec2


NEIGHBORS = (
    ivec2(1, 0),
    ivec2(-1, 0),
    ivec2(0, 1),
    ivec2(0, -1),
    ivec2(1, 1),
    ivec2(-1, 1),
    ivec2(1, -1),
    ivec2(-1, -1)
)


advent = Advent()


number_index = 0


def parse_line(y: int, line: str) -> tuple[dict[ivec2, ivec2], dict[ivec2, str]]:
    # returns {pos: (id, value)}, {pos: char}

    global number_index

    numbers_ = {}
    parts_ = {}
    number_buf = ""
    ex = 0
    for x, ch in enumerate(line):
        if ch.isdigit():
            number_buf += ch

        else:
            if number_buf:
                val = int(number_buf)
                for i in range(x - len(number_buf), x):
                    numbers_[ivec2(i, y)] = ivec2(number_index, val)
                number_index += 1
                number_buf = ""

            if ch != ".":
                parts_[ivec2(x, y)] = ch

        ex = x

    if number_buf:
        val = int(number_buf)
        for i in range(ex - len(number_buf), ex):
            numbers_[ivec2(i, y)] = ivec2(number_index, val)
        number_index += 1

    return numbers_, parts_


numbers: dict[ivec2, ivec2]
parts: dict[ivec2, str]
numbers, parts = advent.read.lines().stream().enumerate().unpack_map(parse_line).reduce(
    lambda a, b: (a[0] | b[0], a[1] | b[1]), ({}, {}))

reachable = set()
for part in parts.keys():
    for offset in NEIGHBORS:
        pos = part + offset
        if pos in numbers:
            reachable.add(numbers[pos])

print(sum(n.y for n in reachable))

gear_ratios = 0
for part, char in parts.items():
    if char != "*":
        continue

    neighbor_numbers = set()
    for offset in NEIGHBORS:
        pos = part + offset
        if pos in numbers:
            neighbor_numbers.add(numbers[pos])

    if len(neighbor_numbers) == 2:
        neighbors = tuple(neighbor_numbers)
        gear_ratios += neighbors[0].y * neighbors[1].y

print(gear_ratios)
