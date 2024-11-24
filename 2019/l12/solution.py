from __future__ import annotations

from advent import Advent, ivec3
import math


class Moon:
    pos: ivec3
    vel: ivec3

    def __init__(self, pos: ivec3, vel: ivec3 = None):
        self.pos = pos
        self.vel = ivec3(0) if vel is None else vel

    @staticmethod
    def parse(ln: str) -> Moon:
        return Moon(ivec3(*(int(coord[2:]) for coord in ln[1:-1].split(", "))))

    def apply_gravity(self, other: Moon):
        d = other.pos - self.pos
        self.vel.x += 0 if d.x == 0 else 1 if d.x > 0 else -1
        self.vel.y += 0 if d.y == 0 else 1 if d.y > 0 else -1
        self.vel.z += 0 if d.z == 0 else 1 if d.z > 0 else -1

    def apply_velocity(self):
        self.pos += self.vel

    def get_energy(self) -> int:
        return sum(abs(self.pos)) * sum(abs(self.vel))

    def copy(self) -> Moon:
        return Moon(ivec3(self.pos), ivec3(self.vel))


data: list[Moon] = Advent().read.lines().map(Moon.parse)()


def step(moons: list[Moon]):
    for a in moons:
        for b in moons:
            if a is not b:
                a.apply_gravity(b)

    for m in moons:
        m.apply_velocity()


def part_1() -> int:
    moons = [moon.copy() for moon in data]
    for _ in range(1000):
        step(moons)
    return sum(m.get_energy() for m in moons)


print(part_1())


def simulate_axis(axis: int, moons: list[Moon]) -> int:
    count = len(moons)
    positions = [moon.pos[axis] for moon in moons]
    target_pos = list(positions)
    velocities = [0 for _ in range(count)]
    target_vel = list(velocities)
    steps = 0
    while True:
        for i in range(count):
            for j in range(count):
                if i != j:
                    d = positions[j] - positions[i]
                    velocities[i] += 0 if d == 0 else 1 if d > 0 else -1

        for i in range(count):
            positions[i] += velocities[i]

        steps += 1

        if velocities == target_vel and positions == target_pos:
            return steps


def part_2() -> int:
    moons = [moon.copy() for moon in data]
    return math.lcm(simulate_axis(0, moons), simulate_axis(1, moons), simulate_axis(2, moons))


print(part_2())
