from ..advent import Advent, vec2

advent = Advent(14)

SAND_SPAWN = vec2(500, 0)

lines = advent.util.flatten(advent.read.lines(
    lambda ln: advent.util.pairs_overlay([vec2(map(int, pos.split(","))) for pos in ln.split(" -> ")])))

lowest_line = max(max(line[0].y, line[1].y) for line in lines)
lines.append((vec2(-1000000, lowest_line + 2), vec2(1000000, lowest_line + 2)))

sands: set[tuple[int, int]] = set()


def collide_point_line(point: vec2, line: tuple[vec2, vec2]) -> bool:
    return point.x == line[0].x == line[1].x and min(line[0].y, line[1].y) <= point.y <= max(line[0].y, line[1].y) or \
           point.y == line[0].y == line[1].y and min(line[0].x, line[1].x) <= point.x <= max(line[0].x, line[1].x)


def empty(pos: vec2) -> bool:
    return pos.tuple() not in sands and not any(collide_point_line(pos, line) for line in lines)


def simulate_fall(pos: vec2):
    if pos.tuple() in sands:
        return None

    if empty(pos + vec2(0, 1)):
        return simulate_fall(pos + vec2(0, 1))

    elif empty(pos + vec2(-1, 1)):
        return simulate_fall(pos + vec2(-1, 1))

    elif empty(pos + vec2(1, 1)):
        return simulate_fall(pos + vec2(1, 1))

    return pos


while (fall_pos := simulate_fall(SAND_SPAWN)) is not None:
    sands.add(fall_pos.tuple())

advent.solution(len(sands))
