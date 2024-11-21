from advent import Advent


type Cups = tuple[int, ...]


data = tuple(map(int, Advent().read()))
min_value = min(data)
max_value = max(data)


def do_round(cups: Cups, current: int) -> tuple[Cups, int]:
    current_label = cups[current]
    cups = cups[current+1:] + cups[:current+1]
    three = cups[:3]
    cups = cups[3:]

    destination_label = current_label
    while True:
        destination_label -= 1
        if destination_label < min_value:
            destination_label = max_value

        try:
            destination = cups.index(destination_label)
        except ValueError:
            pass
        else:
            break

    cups = three + cups[destination+1:] + cups[:destination+1]
    current = cups.index(current_label) + 1
    if current > max_value:
        current = min_value

    return cups, current


current_index = 0
for _ in range(100):
    data, current_index = do_round(data, current_index)

index = data.index(1)
print("".join(map(str, data[index+1:] + data[:index])))
