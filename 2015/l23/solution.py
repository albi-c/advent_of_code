from advent import Advent


type Ins = tuple[str, int | tuple[int, int]]


def parse_line(ln: str) -> Ins:
    name, params = ln.split(" ", 1)
    if name == "jie" or name == "jio":
        reg, offset = params.split(", ", 1)
        return name, (1 if reg == "b" else 0, int(offset))
    if name == "jmp":
        return name, int(params)
    return name, 1 if params == "b" else 0


code: list[Ins] = Advent().read.lines().map(parse_line)()


def run(regs: list[int]) -> list[int]:
    pc = 0
    while pc < len(code):
        name, param = code[pc]
        if name == "jmp":
            pc += param
            continue
        elif name == "jie" and regs[param[0]] % 2 == 0:
            pc += param[1]
            continue
        elif name == "jio" and regs[param[0]] == 1:
            pc += param[1]
            continue

        if name == "hlf":
            regs[param] //= 2
        elif name == "tpl":
            regs[param] *= 3
        elif name == "inc":
            regs[param] += 1
        pc += 1
    return regs


print(run([0, 0])[1])
print(run([1, 0])[1])
