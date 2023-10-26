from advent import Advent, Util

import string

advent = Advent()

data = advent.read()

def increment(s: str, index: int = -1) -> str:
    if index < -8:
        return "a" * 8

    ch = ord(s[index])+1
    overflow = False
    if ch > ord("z"):
        ch = ord("a")
        overflow = True
    ch = chr(ch)

    ns = list(s)
    ns[index] = ch
    ns = "".join(ns)
    if overflow:
        return increment(ns, index - 1)
    return ns

def check(s: str) -> bool:
    if "i" in s or "o" in s or "l" in s:
        return False

    if not any(ord(a) == ord(b) - 1 and ord(b) + 1 == ord(c) for a, b, c in Util.window(s, 3)):
        return False

    if sum(s.count(c+c) for c in set(s)) < 2:
        return False

    return True

p = data
while not check(p):
    p = increment(p)
print(p)

p = increment(p)
while not check(p):
    p = increment(p)
print(p)
