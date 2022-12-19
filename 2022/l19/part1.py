from ..advent import Advent, vec4

advent = Advent(19)

Blueprint = tuple[vec4, vec4, vec4, vec4]
Branch = tuple[vec4, vec4]


def parse_blueprint(text: str) -> Blueprint:
    spl = text.split(": ")[1].replace(".", "").split(" ")

    return vec4(int(spl[4]), 0, 0, 0), vec4(int(spl[10]), 0, 0, 0), \
           vec4(int(spl[16]), int(spl[19]), 0, 0), vec4(int(spl[25]), 0, int(spl[28]), 0)


blueprints = advent.read.lines(parse_blueprint)


def craftable(robot: vec4, materials: vec4) -> bool:
    return robot.x <= materials.x and robot.y <= materials.y and robot.z <= materials.z and robot.w <= materials.w


def find_best(blueprint: Blueprint, time: int = 24) -> int:
    queue: list[Branch] = [(vec4(1, 0, 0, 0), vec4())]

    required_to_build = [max(r_ * vec4.unit(i) for r_ in blueprint) for i in range(4)]

    while time > 0:
        print(time, len(queue))

        new_queue: list[Branch] = []

        for robots, materials in queue:
            if craftable(blueprint[3], materials):
                materials += robots
                robots.w += 1
                materials -= blueprint[3]
                continue

            if all(craftable(r, robots) for r in blueprint[:3]):
                materials += robots
                continue

            for i, r in enumerate(blueprint[:3]):
                if craftable(r, materials) and robots * vec4.unit(i) >= required_to_build[i]:
                    new_queue.append((robots + vec4.unit(i), materials + robots - r))

            materials += robots

        queue += new_queue

        best = max(materials.w for _, materials in queue)
        queue = [branch for branch in queue if branch[1].w + 1 > best]

        time -= 1

    return max(materials.w for _, materials in queue)


print(find_best(blueprints[1]))

# advent.solution(sum((i + 1) * find_best(b) for i, b in enumerate(blueprints)))
