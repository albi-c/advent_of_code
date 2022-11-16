from ..advent import Advent

advent = Advent(1)

modules = advent.read.lines(int)


def calculate_fuel(mass: int) -> int:
    fuel = mass // 3 - 2

    if fuel <= 0:
        return 0

    return fuel + calculate_fuel(fuel)


advent.solution(sum(map(calculate_fuel, modules)))
