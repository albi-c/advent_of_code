from advent import Advent, Util

import json

advent = Advent()

data = json.loads(advent.read())


def sum_numbers(d: int | str | list | dict) -> int:
    if isinstance(d, int):
        return d

    elif isinstance(d, list):
        return sum(map(sum_numbers, d))

    elif isinstance(d, dict):
        return sum(map(sum_numbers, d.values()))

    elif isinstance(d, str):
        return 0

    raise TypeError


def sum_numbers_check_red(d: int | str | list | dict) -> int:
    if isinstance(d, int):
        return d

    elif isinstance(d, list):
        return sum(map(sum_numbers_check_red, d))

    elif isinstance(d, dict):
        if "red" in d.values():
            return 0
        return sum(map(sum_numbers_check_red, d.values()))

    elif isinstance(d, str):
        return 0

    raise TypeError


print(sum_numbers(data))
print(sum_numbers_check_red(data))
