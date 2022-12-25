from ..advent import Advent

advent = Advent(25)

FROM_SNAFU = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
TO_SNAFU = {2: "2", 1: "1", 0: "0", 3: "=", 4: "-"}


def decode_snafu(s: str) -> int:
    return sum(FROM_SNAFU[ch] * (5 ** i) for i, ch in enumerate(reversed(s)))


def encode_snafu(n: int) -> str:
    s = ""
    while n:
        s = TO_SNAFU[n % 5] + s
        n //= 5
        if s[0] in "-=":
            n += 1

    return s


num = sum(advent.read.lines(decode_snafu))

advent.solution(encode_snafu(num))
