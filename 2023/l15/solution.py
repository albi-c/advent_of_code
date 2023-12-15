from advent import Advent


advent = Advent()

data = advent.read.split(",")()


def get_hash(string: str) -> int:
    val = 0
    for ch in string:
        val += ord(ch)
        val *= 17
        val &= 0xff   # modulo 256

    return val


print(sum(map(get_hash, data)))


boxes: list[list[tuple[str, int]]] = [[] for _ in range(256)]

for lens in data:
    if "-" in lens:
        label = lens[:-1]
        box = boxes[get_hash(label)]
        for i, (lab, _) in enumerate(box):
            if lab == label:
                box.pop(i)
                break

    elif "=" in lens:
        label, focal_length = lens.split("=")
        focal_length = int(focal_length)
        box = boxes[get_hash(label)]
        added = False
        for i, (lab, _) in enumerate(box):
            if lab == label:
                box[i] = (label, focal_length)
                added = True
                break
        if not added:
            box.append((label, focal_length))

    else:
        assert False

print(sum(i * sum(j * v for j, (_, v) in enumerate(box, start=1)) for i, box in enumerate(boxes, start=1)))
