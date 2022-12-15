from ..advent import Advent, vec2

advent = Advent(15)

Y_SLICE = 2000000

data = advent.read.lines(lambda ln:
                         tuple(vec2(int(part.split("=")[1].split(",")[0]),
                               int(part.split("=")[2])) for part in ln.split(": ")))


def render(y: int, sensor: vec2, beacon: vec2) -> vec2 | None:
    distance = sensor.manhattan(beacon)
    diff = abs(sensor.y - y)

    if distance == diff:
        return vec2(sensor.x, sensor.x)

    if distance < diff:
        return vec2()

    return vec2(sensor.x - (distance - diff), sensor.x + (distance - diff))


def get_deleted(lns: list[vec2]) -> int | None:
    for i, line in enumerate(lns):
        if line.x == line.y:
            return i

        for j, line_ in enumerate(lns):
            if line_.x == line_.y:
                return j

            if i == j:
                continue

            if line.x <= line_.x <= line.y or line.x <= line_.y <= line.y:
                # print(line, line_)
                line.x = min(line.x, line_.x)
                line.y = max(line.y, line_.y)
                # print(line)
                return j

    return None


lines = [render(Y_SLICE, *pair) for pair in data]

# print("R", lines, set(beacon.tuple() for _, beacon in data if beacon.y == Y_SLICE))

while (delete := get_deleted(lines)) is not None:
    lines.pop(delete)

print("R", lines, set(beacon.tuple() for _, beacon in data if beacon.y == Y_SLICE))
advent.solution(sum(line.y - line.x + 1 for line in lines) -
                len(set(beacon.tuple() for _, beacon in data if beacon.y == Y_SLICE)))
