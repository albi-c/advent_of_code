from advent import Advent, Stream, X

import hashlib

advent = Advent()

data = advent.read()

for n in Stream.of_old_value_producer(X+1, 5, True):
    if hashlib.md5(f"{data}{n}".encode("utf-8")).hexdigest().startswith("00000"):
        print(n)
        break

for n in Stream.of_old_value_producer(X+1, 5, True):
    if hashlib.md5(f"{data}{n}".encode("utf-8")).hexdigest().startswith("000000"):
        print(n)
        break
