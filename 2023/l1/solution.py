from advent import Advent, Stream


DIGITS = [
    ("one", "1"),
    ("two", "2"),
    ("three", "3"),
    ("four", "4"),
    ("five", "5"),
    ("six", "6"),
    ("seven", "7"),
    ("eight", "8"),
    ("nine", "9")
]

advent = Advent()


def solve(lines: list[str]) -> int:
    data = [Stream(ln).filter(lambda ch: ch in "0123456789").to(str) for ln in lines]
    return sum(int(ln[0] + ln[-1]) for ln in data)


print(solve(advent.read.lines()()))


def replace_digits(line: str) -> str:
    output = ""
    buf = ""
    for ch in line:
        if ch in "0123456789":
            output += ch
            buf = ""
        else:
            buf += ch
            for from_, to in DIGITS:
                if buf.endswith(from_):
                    output += to
    return output


print(solve(advent.read.lines().map(replace_digits)()))
