import itertools
import math


required = 36000000


def divisors(n: int) -> list[int]:
    small = [d for d in range(1, math.isqrt(n) + 1) if n % d == 0]
    return small + [n // d for d in small if n != d * d]


for i in itertools.count(1):
    divs = divisors(i)
    if sum(divs) * 10 >= required:
        print(i)
        break

for i in itertools.count(1):
    divs = divisors(i)
    if sum(div for div in divs if i // div <= 50) * 11 >= required:
        print(i)
        break
