from ..advent import Advent, vec4

advent = Advent(19)

Blueprint = tuple[vec4, vec4, vec4, vec4]


def parse_blueprint(text: str) -> Blueprint:
    spl = text.split(": ")[1].replace(".", "").split(" ")

    return vec4(int(spl[4]), 0, 0, 0), vec4(int(spl[10]), 0, 0, 0), \
           vec4(int(spl[16]), int(spl[19]), 0, 0), vec4(int(spl[25]), 0, int(spl[28]), 0)


blueprints = advent.read.lines(parse_blueprint)


def craftable(robot: vec4, materials: vec4) -> bool:
    return robot.x <= materials.x and robot.y <= materials.y and robot.z <= materials.z and robot.w <= materials.w


def find_best(blueprint: Blueprint, time: int, robots: vec4, materials: vec4) -> int:
    if time <= 0:
        return materials.w

    if craftable(blueprint[3], materials):
        return find_best(blueprint, time - 1, robots + vec4.unit(3), materials + robots - blueprint[3])

    best = find_best(blueprint, time - 1, robots, materials + robots)
    # print(time, best, materials)

    for i, r in enumerate(blueprint[:3]):
        if craftable(r, materials):
            best = max(
                best,
                find_best(blueprint, time - 1, robots + vec4.unit(i), materials + robots - r)
            )

    return best


print(find_best(blueprints[0], 20, vec4(1, 0, 0, 0), vec4(0, 0, 0, 0)))
# print(find_best(blueprints[1], 24, vec4(1, 0, 0, 0), vec4(0, 0, 0, 0)))
