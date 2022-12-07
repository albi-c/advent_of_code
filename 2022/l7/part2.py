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


def sum_sizes(selected: list[int], fs: dict, limit: int = 0):
    size = 0
    for name, f in fs.items():
        if isinstance(f, dict):
            s = sum_sizes(selected, f, limit)

            if s >= limit:
                selected.append(s)

            size += s

        else:
            size += f

    if size >= limit:
        selected.append(size)

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

total_size = sum_sizes([], files)
sel = []
sum_sizes(sel, files, 30000000 - (70000000 - total_size))
advent.solution(min(sel))
