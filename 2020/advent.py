import os, sys, math

class vec2:
    def __init__(self, x = None, y = None):
        if x is None and y is None:
            self.x = 0
            self.y = 0
        elif x is not None and y is None:
            self.x = x[0]
            self.y = x[1]
        elif x is not None and y is not None:
            self.x = x
            self.y = y
    
    def __add__(self, o: 'vec2') -> 'vec2':
        return vec2(self.x + o.x, self.y + o.y)
    def __sub__(self, o: 'vec2') -> 'vec2':
        return vec2(self.x - o.x, self.y - o.y)
    def __mul__(self, o: 'vec2') -> 'vec2':
        return vec2(self.x * o.x, self.y * o.y)
    def __truediv__(self, o: 'vec2') -> 'vec2':
        return vec2(self.x / o.x, self.y / o.y)
    def __floordiv__(self, o: 'vec2') -> 'vec2':
        return vec2(self.x // o.x, self.y // o.y)
    def __pow__(self, o: 'vec2') -> 'vec2':
        return vec2(self.x ** o.x, self.y ** o.y)
    
    def __iadd__(self, o: 'vec2') -> 'vec2':
        self.x += o.x
        self.y += o.y
        return self
    def __isub__(self, o: 'vec2') -> 'vec2':
        self.x -= o.x
        self.y -= o.y
        return self
    def __imul__(self, o: 'vec2') -> 'vec2':
        self.x *= o.x
        self.y *= o.y
        return self
    def __itruediv__(self, o: 'vec2') -> 'vec2':
        self.x /= o.x
        self.y /= o.y
        return self
    def __ifloordiv__(self, o: 'vec2') -> 'vec2':
        self.x //= o.x
        self.y //= o.y
        return self
    def __ipow__(self, o: 'vec2') -> 'vec2':
        self.x **= o.x
        self.y **= o.y
        return self
    
    def __neg__(self) -> 'vec2':
        return vec2(-self.x, -self.y)
    def __abs__(self) -> 'vec2':
        return vec2(abs(self.x), abs(self.y))
    
    def __len__(self):
        return math.sqrt(self.x * self.x + self.y * self.y)
    def distance(self, o: 'vec2'):
        return len(self - o)
    def manhattan(self, o: 'vec2'):
        return abs(abs(self) - abs(o))
    
    def in_bounds(self, a: 'vec2', b: 'vec2'):
        lx = min(a.x, b.x)
        ux = max(a.x, b.x)

        ly = min(a.y, b.y)
        uy = max(a.y, b.y)

        return self.x >= lx and self.x <= ux and self.y >= ly and self.y <= uy
    
    def tuple(self) -> tuple:
        return (self.x, self.y)

class BitListReader:
    def __init__(self, bl: 'BitList'):
        self.bl = bl
    
    def bit(self) -> bool:
        self.bl.index += 1
        return self.bl[self.bl.index]
    
    def bits(self, n: int) -> list:
        self.bl.index += n
        return self.bl[self.bl.index-n+1:self.bl.index+1]
    
    def int(self, n: int) -> int:
        bits = self.bits(n)
        r = 0
        for b in bits:
            r |= b
            r <<= 1
        return r >> 1

class BitList:
    def __init__(self, data: list = None):
        self.data = data.copy() if data is not None else []
        self.index = -1

        self.read = BitListReader(self)
    
    def __len__(self) -> int:
        return len(self.data)
    
    def __getitem__(self, pos: int) -> bool:
        return self.data[pos]
    
    def __setitem__(self, pos: int, val: bool):
        self.data[pos] = val
    
    def append(self, val: bool):
        self.data.append(bool(val))

class Grid:
    def __init__(self, data: list):
        self.data = data

        self.width = len(data[0])
        self.height = len(data)
    
    def get(self, key: tuple):
        return self.data[key[1]][key[0]]
    
    def set(self, key: tuple, value):
        self.data[key[1]][key[0]] = value
    
    def __getitem__(self, key: tuple):
        return self.get(key)
    
    def __setitem__(self, key: tuple, value):
        self.set(key, value)
    
    def neighbors(self, pos: tuple):
        if pos[0] > 0:
            yield (pos[0] - 1, pos[1]), self.get((pos[0] - 1, pos[1]))
        if pos[0] < self.width - 1:
            yield (pos[0] + 1, pos[1]), self.get((pos[0] + 1, pos[1]))
        if pos[1] > 0:
            yield (pos[0], pos[1] - 1), self.get((pos[0], pos[1] - 1))
        if pos[1] < self.height - 1:
            yield (pos[0], pos[1] + 1), self.get((pos[0], pos[1] + 1))
    
    def items(self):
        for y, row in enumerate(self.data):
            for x, val in enumerate(row):
                yield (x, y), val
    
    @staticmethod
    def print(points):
        mx = max(map(lambda x: x[0], points)) + 1
        my = max(map(lambda x: x[1], points)) + 1

        for y in range(my):
            for x in range(mx):
                print("##" if [x, y] in points else "..", end="")
            
            print()

class AdventReader:
    def __init__(self, advent: 'Advent'):
        self.advent = advent
        self.level = self.advent.level

        self.ipath = os.path.join(os.path.dirname(__file__), f"l{str(self.level)}", "input.txt")
    
    def lines(self, convert = lambda x: x):
        return [convert(val.strip()) for val in open(self.ipath).readlines()]
    
    def blocks(self):
        return [block for block in open(self.ipath).read().split("\n\n") if block.strip()]
    
    def separated(self, sep: str = ",", convert = lambda x: x):
        return [convert(val) for val in open(self.ipath).read().split(sep)]
    
    def grid(self, convert = lambda x: x) -> Grid:
        return Grid([[convert(val) for val in row.strip()] for row in open(self.ipath).readlines()])
    
    def bitlist_hex(self) -> BitList:
        l = BitList()

        for ch in open(self.ipath).read().strip():
            n = int(ch, 16)
            l.append((n & 0b1000) >> 3)
            l.append((n & 0b100) >> 2)
            l.append((n & 0b10) >> 1)
            l.append((n & 0b1))

        return l
    
    def __call__(self):
        return open(self.ipath).read().strip()

class AdventUtil:
    def flatten(self, lst):
        return [val for group in lst for val in group]
    
    def remove_duplicates(self, lst):
        tmp = []
        
        for e in lst:
            if e not in tmp:
                tmp.append(e)
        
        return tmp
    
    def pairs_overlay(self, lst):
        prev = lst[0]
        for el in lst[1:]:
            yield prev, el
            prev = el
    
    def product(self, lst):
        n = 1
        for x in lst:
            n *= x
        return n

class Advent:
    def __init__(self, level: int, part: int):
        self.level = level
        self.part = part

        self.read = AdventReader(self)
        self.util = AdventUtil()
    
    def solution(self, message) -> None:
        print(f"Solution: {message}")
    
    def exit(self) -> None:
        sys.exit(0)
