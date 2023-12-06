from advent import Advent, Stream, Seq


advent = Advent()


def repeat_replace(string: str) -> str:
    while "  " in (string := string.replace("  ", " ")):
        pass

    return string


def parse_line(ln: str) -> list[int]:
    return list(map(int, ln.split(": ")[1].split(" ")))


times, distances = advent.read.lines().map(repeat_replace).map(parse_line)()

print(times, distances)


def get_options(t: int, d: int) -> int:
    return sum(x * (t - x) > d for x in range(1, t))


print(Stream.of_zip(times, distances).unpack_map(get_options).prod())


def join_numbers(numbers: list[int]) -> int:
    return int("".join(map(str, numbers)))


print(get_options(join_numbers(times), join_numbers(distances)))
