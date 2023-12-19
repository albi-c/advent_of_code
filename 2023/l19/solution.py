from advent import Advent, Stream

from typing import Callable
import math


Part = dict[str, int]
Filter = Callable[[Part], bool | str | None]
Filter2 = tuple[str | None, bool, int, str]
Workflow = tuple[tuple[Filter, Filter2], ...]


def parse_filter(string: str) -> Filter:
    if ":" in string:
        spl = string.split(":")
        param = string[0]
        n = int(spl[0][2:])
        dst = spl[1]
        dst = True if dst == "A" else False if dst == "R" else dst
        if string[1] == ">":
            return lambda p: dst if p[param] > n else None
        elif string[1] == "<":
            return lambda p: dst if p[param] < n else None
        else:
            raise ValueError()

    dst = string
    dst = True if dst == "A" else False if dst == "R" else dst
    return lambda _: dst


def parse_filter_2(string: str) -> Filter2:
    if ":" in string:
        spl = string.split(":")
        return string[0], string[1] == ">", int(spl[0][2:]), spl[1]

    return None, False, 0, string

def parse_workflows(data: list[str]) -> dict[str, Workflow]:
    return {ln.split("{")[0]: tuple((parse_filter(f), parse_filter_2(f))
                                    for f in ln[:-1].split("{")[1].split(",")) for ln in data}


def parse_parts(data: list[str]) -> list[Part]:
    return [{p[0]: int(p[2:]) for p in ln[1:-1].split(",")} for ln in data]


workflow_block, part_block = Advent().read.blocks()()
workflows = parse_workflows(workflow_block.splitlines())
parts_ = parse_parts(part_block.splitlines())


def part1():
    ratings = 0
    for part in parts_:
        finished = False
        wf = workflows["in"]
        while not finished:
            for f, _ in wf:
                val = f(part)
                if isinstance(val, str):
                    wf = workflows[val]
                    break
                elif val is None:
                    continue
                elif val is True:
                    ratings += sum(part.values())
                    finished = True
                    break
                elif val is False:
                    finished = True
                    break
                else:
                    pass

    return ratings


def part2(parts: dict[str, tuple[int, int]], workflow_name: str, i: int) -> int:
    if workflow_name == "R":
        return 0
    elif workflow_name == "A":
        return math.prod(b - a + 1 for a, b in parts.values())

    workflow = workflows[workflow_name]
    _, (param, gt, val, dst) = workflow[i]

    if param is None:
        return part2(parts, dst, 0)

    a, b = parts[param]

    if gt:
        x = (val + 1, b)
        y = (a, val)
    else:
        x = (a, val - 1)
        y = (val, b)

    count = 0
    if x[1] - x[0] > 0:
        count += part2(parts | {param: x}, dst, 0)
    if y[1] - y[0] > 0:
        count += part2(parts | {param: y}, workflow_name, i + 1)

    return count


print(part1())
print(part2({p: (1, 4000) for p in "xmas"}, "in", 0))
