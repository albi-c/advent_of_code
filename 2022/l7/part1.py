from ..advent import Advent

advent = Advent(7)

data = advent.read.lines()

files = {}


def add_file(fs: dict, directory: list[str], name: str, size: int):
    if len(directory) == 0:
        fs[name] = size

    else:
        if directory[0] not in fs:
            fs[directory[0]] = {}

        add_file(fs[directory[0]], directory[1:], name, size)


def sum_sizes(selected: list[int], fs: dict):
    size = 0
    for f in fs.values():
        if isinstance(f, dict):
            s = sum_sizes(selected, f)

            if s <= 100000:
                selected.append(s)

            size += s

        else:
            size += f

    return size


cwd = []
for i, ln in enumerate(data):
    ln = ln[2:]
    if ln.startswith("cd"):
        d = ln[3:]
        if d == "/":
            cwd = []
        elif d == "..":
            cwd.pop(-1)
        else:
            cwd.append(d)
    else:
        for line in data[i:]:
            if line.startswith("$") or line.startswith("dir"):
                break

            spl = line.split()
            add_file(files, cwd, spl[1], int(spl[0]))

sel = []
sum_sizes(sel, files)
advent.solution(sum(sel))
