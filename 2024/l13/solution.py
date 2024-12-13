from advent import Advent, ivec2


input_data: list[list[ivec2]] = [[ivec2(*(int(x[2:]) for x in ln.split(": ")[1].split(", "))) for ln in block]
                                 for block in Advent().read.blocks().lines()()]


def find_best(machine: list[ivec2]) -> int:
    best = 1 << 30
    a, b, target = machine
    for i in range(101):
        pa = a * i
        if pa.x > target.x or pa.y > target.y:
            continue
        rem = target - pa
        if rem.x % b.x != 0 or rem.y % b.y != 0:
            continue
        rem //= b
        if rem.x != rem.y:
            continue
        best = min(best, 3 * i + rem.x)
    return best if best != 1 << 30 else 0


print(sum(map(find_best, input_data)))
