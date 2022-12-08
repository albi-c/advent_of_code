import itertools
import math
import os
import sys


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
    
    def __repr__(self) -> str:
        return f"vec2({self.x}, {self.y})"
    
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
        diff = abs(self - o)
        return diff.x + diff.y
    
    def in_bounds(self, a: 'vec2', b: 'vec2'):
        lx = min(a.x, b.x)
        ux = max(a.x, b.x)

        ly = min(a.y, b.y)
        uy = max(a.y, b.y)

        return lx <= self.x <= ux and self.y >= ly and self.y <= uy
    
    def tuple(self) -> tuple:
        return self.x, self.y


class vec3:
    def __init__(self, x=None, y=None, z=None):
        if x is None and y is None and z is None:
            self.x = 0
            self.y = 0
            self.z = 0
        elif x is not None and y is None and z is None:
            if type(x) in [int, float]:
                self.x = self.y = self.z = x
            else:
                self.x = x[0]
                self.y = x[1]
                self.z = x[2]
        elif x is not None and y is not None and z is not None:
            self.x = x
            self.y = y
            self.z = z
    
    def __repr__(self) -> str:
        return f"vec3({self.x}, {self.y}, {self.z})"
    
    def __add__(self, o: 'vec3') -> 'vec3':
        return vec3(self.x + o.x, self.y + o.y, self.z + o.z)

    def __sub__(self, o: 'vec3') -> 'vec3':
        return vec3(self.x - o.x, self.y - o.y, self.z - o.z)

    def __mul__(self, o) -> 'vec3':
        if isinstance(o, mat3):
            return o * self
        else:
            return vec3(self.x * o.x, self.y * o.y, self.z * o.z)

    def __truediv__(self, o: 'vec3') -> 'vec3':
        return vec3(self.x / o.x, self.y / o.y, self.z / o.z)

    def __floordiv__(self, o: 'vec3') -> 'vec3':
        return vec3(self.x // o.x, self.y // o.y, self.z // o.z)

    def __pow__(self, o: 'vec3') -> 'vec3':
        return vec3(self.x ** o.x, self.y ** o.y, self.z ** o.z)
    
    def __iadd__(self, o: 'vec3') -> 'vec3':
        self.x += o.x
        self.y += o.y
        self.z += o.z
        return self

    def __isub__(self, o: 'vec3') -> 'vec3':
        self.x -= o.x
        self.y -= o.y
        self.z -= o.z
        return self

    def __imul__(self, o: 'vec3') -> 'vec3':
        if isinstance(o, mat3):
            self = self * o
        else:
            self.x *= o.x
            self.y *= o.y
            self.z *= o.z
        return self

    def __itruediv__(self, o: 'vec3') -> 'vec3':
        self.x /= o.x
        self.y /= o.y
        self.z /= o.z
        return self

    def __ifloordiv__(self, o: 'vec3') -> 'vec3':
        self.x //= o.x
        self.y //= o.y
        self.z //= o.z
        return self

    def __ipow__(self, o: 'vec3') -> 'vec3':
        self.x **= o.x
        self.y **= o.y
        self.z **= o.z
        return self
    
    def __neg__(self) -> 'vec3':
        return vec3(-self.x, -self.y, -self.z)

    def __abs__(self) -> 'vec3':
        return vec3(abs(self.x), abs(self.y), abs(self.z))
    
    def __eq__(self, o: 'vec3') -> bool:
        return self.x == o.x and self.y == o.y and self.z == o.z
    
    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))
    
    def __len__(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def distance(self, o: 'vec3'):
        return len(self - o)

    def manhattan(self, o: 'vec3'):
        diff = abs(self - o)
        return diff.x + diff.y + diff.z
    
    def in_bounds(self, a: 'vec3', b: 'vec3'):
        lx = min(a.x, b.x)
        ux = max(a.x, b.x)

        ly = min(a.y, b.y)
        uy = max(a.y, b.y)

        lz = min(a.z, b.z)
        uz = max(a.z, b.z)

        return lx <= self.x <= ux and ly <= self.y <= uy and lz <= self.z <= uz
    
    def tuple(self) -> tuple:
        return self.x, self.y, self.z
    
    def rotations(self) -> 'vec3':
        for mat in vec3.rotation_matrices():
            yield mat * self
    
    @staticmethod
    def rotation_matrices():
        for xm, ym, zm in itertools.product((1, -1), (1, -1), (1, -1)):
            for x, y, z in itertools.permutations((0, 1, 2), 3):
                mat = mat3.empty_list()
                mat[0][x] = xm
                mat[1][y] = ym
                mat[2][z] = zm
                yield mat3(mat)
    
    @staticmethod
    def rotation_functions():
        for mat in vec3.rotation_matrices():
            yield lambda vec: mat * vec


class mat3:
    def __init__(self, data: list = None):
        self.data = data if data is not None else mat3.identity_list()
    
    def __repr__(self) -> str:
        return f"mat3({self.data})"
    
    @staticmethod
    def identity() -> 'mat3':
        return mat3(mat3.identity_list())
    
    @staticmethod
    def identity_list() -> list:
        return [[1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]]
    
    @staticmethod
    def empty() -> 'mat3':
        return mat3(mat3.empty_list())

    @staticmethod
    def empty_list() -> list:
        return [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
    
    @staticmethod
    def scale(scale: vec3) -> 'mat3':
        return mat3([[scale.x, 0, 0],
                     [0, scale.y, 0],
                     [0, 0, scale.z]])

    def __mul__(self, o: vec3) -> vec3:
        return vec3([sum(map(lambda p: p[0] * p[1], zip(self.data[i], (o.x, o.y, o.z)))) for i in range(3)])

    def __eq__(self, o) -> bool:
        return self.data == o.data

    def __hash__(self):
        return hash(tuple([tuple(row) for row in self.data]))


class BitListReader:
    def __init__(self, bl: 'BitList'):
        self.bl = bl
    
    def bit(self) -> bool:
        self.bl.index += 1
        return self.bl[self.bl.index]
    
    def bits(self, n: int) -> bool | list:
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
    
    def append(self, val: bool | int):
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

    def col(self, i: int):
        return [row[i] for row in self.data]
    
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
        bitlist = BitList()

        for ch in open(self.ipath).read().strip():
            n = int(ch, 16)
            bitlist.append((n & 0b1000) >> 3)
            bitlist.append((n & 0b100) >> 2)
            bitlist.append((n & 0b10) >> 1)
            bitlist.append((n & 0b1))

        return bitlist
    
    def __call__(self):
        return open(self.ipath).read().strip()


class AdventUtil:
    @staticmethod
    def flatten(lst: list):
        return [val for group in lst for val in group]

    @staticmethod
    def remove_duplicates(lst: list):
        tmp = []
        
        for e in lst:
            if e not in tmp:
                tmp.append(e)
        
        return tmp

    @staticmethod
    def pairs_overlay(lst: list):
        prev = lst[0]
        for el in lst[1:]:
            yield prev, el
            prev = el

    @staticmethod
    def product(lst: list[int]) -> int:
        n = 1
        for x in lst:
            n *= x
        return n

    @staticmethod
    def chunks(lst: list, size: int) -> list:
        for i in range(0, len(lst), size):
            yield lst[i:i + size]


class Advent:
    def __init__(self, level: int):
        self.level = level
        self.read = AdventReader(self)
        self.util = AdventUtil()

    @staticmethod
    def solution(message) -> None:
        print(f"Solution: {message}")
        Advent.exit()

    @staticmethod
    def exit() -> None:
        sys.exit(0)


class IntcodeVM:
    data: list[int]
    step: int
    running: bool
    
    instruction_table: dict[int, tuple[callable, int]]

    def __init__(self, data: list[int]):
        self.data = data.copy()
        self.step = 0
        self.running = False

        self.instruction_table = {}
        for opcode, func in {
            1: self.ins_add,
            2: self.ins_mul,

            99: self.ins_exit
        }.items():
            self.instruction_table[opcode] = (func, func.__code__.co_argcount - 1)

    def run(self):
        self.running = True
        while self.running:
            opcode = self.data[self.step]
            func, n_params = self.instruction_table[opcode]
            func(*self.data[self.step+1:self.step+1+n_params])
            self.step += 1 + n_params

    def __getitem__(self, item: int) -> int:
        return self.data[item]

    def __setitem__(self, key: int, value: int):
        self.data[key] = value

    def ins_add(self, a: int, b: int, out: int):
        self[out] = self[a] + self[b]

    def ins_mul(self, a: int, b: int, out: int):
        self[out] = self[a] * self[b]

    def ins_exit(self):
        self.running = False
