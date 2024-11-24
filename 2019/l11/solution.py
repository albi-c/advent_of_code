from advent import Advent, ivec2

from typing import Callable, Iterable, Iterator
import glm

code: list[int] = Advent().read.split(",").map(int)()


type Param = tuple[int, int]


class IntcodeVM:
    data: list[int]
    pc: int
    rb: int
    _running: bool
    _exited: bool
    _ins_table: dict[int, tuple[Callable[[Param, ...], None | int], int]]
    _input_iter: Iterator[int]
    _output_func: Callable[[int], None]

    def __init__(self, data: list[int], inputs: Iterable[int], output_func: Callable[[int], None]):
        self.data = data
        self.pc = 0
        self.rb = 0
        self._running = False
        self._exited = False
        self._ins_table = {
            opcode: (func, func.__code__.co_argcount - 1)
            for opcode, func in (
                (1, self.ins_add),
                (2, self.ins_mul),
                (3, self.ins_inp),
                (4, self.ins_out),
                (5, self.ins_jit),
                (6, self.ins_jif),
                (7, self.ins_lt),
                (8, self.ins_eq),
                (9, self.ins_rel),
                (99, self.ins_exit)
            )
        }
        self._input_iter = iter(inputs)
        self._output_func = output_func

    def run(self) -> bool:
        if self._exited:
            return True
        self._running = True
        self._exited = False
        while self._running:
            ins = self.data[self.pc]
            opcode = ins % 100
            func, num_params = self._ins_table[opcode]
            p_modes_n = ins // 100
            p_modes = []
            for _ in range(num_params):
                p_modes.append(p_modes_n % 10)
                p_modes_n //= 10
            if (new_pc := func(*zip(p_modes, self.data[self.pc+1:self.pc+1+num_params]))) is not None:
                self.pc = new_pc
            else:
                self.pc += 1 + num_params
        return self._exited

    def pause(self):
        self._running = False
        self._exited = False

    def __getitem__(self, index: int) -> int:
        if index > len(self.data):
            self.data += [0 for _ in range(index - len(self.data) + 1024)]
        return self.data[index]

    def __setitem__(self, index: int, value: int):
        if index > len(self.data):
            self.data += [0 for _ in range(index - len(self.data) + 1024)]
        self.data[index] = value

    def load(self, param: Param) -> int:
        mode, x = param
        if mode == 0:
            return self[x]
        elif mode == 1:
            return x
        elif mode == 2:
            return self[x + self.rb]
        else:
            raise ValueError(f"Invalid parameter load mode: {mode}")

    def store(self, param: Param, value: int):
        mode, x = param
        if mode == 0:
            self[x] = value
        elif mode == 2:
            self[x + self.rb] = value
        else:
            raise ValueError(f"Invalid parameter store mode: {mode}")

    def ins_add(self, a: Param, b: Param, out: Param):
        self.store(out, self.load(a) + self.load(b))

    def ins_mul(self, a: Param, b: Param, out: Param):
        self.store(out, self.load(a) * self.load(b))

    def ins_inp(self, out: Param):
        self.store(out, next(self._input_iter))

    def ins_out(self, x: Param):
        self._output_func(self.load(x))

    def ins_jit(self, x: Param, addr: Param) -> int | None:
        if self.load(x) != 0:
            return self.load(addr)

    def ins_jif(self, x: Param, addr: Param) -> int | None:
        if self.load(x) == 0:
            return self.load(addr)

    def ins_lt(self, a: Param, b: Param, out: Param):
        self.store(out, int(self.load(a) < self.load(b)))

    def ins_eq(self, a: Param, b: Param, out: Param):
        self.store(out, int(self.load(a) == self.load(b)))

    def ins_rel(self, x: Param):
        self.rb += self.load(x)

    def ins_exit(self):
        self._running = False
        self._exited = True


class Robot:
    painted: set[ivec2]
    colors: dict[ivec2, int]
    pos: ivec2
    facing: ivec2
    _input_state: int

    def __init__(self):
        self.painted = set()
        self.colors = {}
        self.pos = ivec2(0, 0)
        self.facing = ivec2(0, 1)
        self._input_state = 0

    def __iter__(self):
        return self

    def __next__(self) -> int:
        return self.colors.get(self.pos, 0)

    def __call__(self, x: int):
        if self._input_state == 0:
            pos = ivec2(self.pos)
            self.painted.add(pos)
            self.colors[pos] = x
            self._input_state = 1
        else:
            if x == 0:
                self.facing = ivec2(-self.facing.y, self.facing.x)
            else:
                self.facing = ivec2(self.facing.y, -self.facing.x)
            self.pos += self.facing
            self._input_state = 0


robot = Robot()
vm = IntcodeVM(code.copy(), robot, robot)
vm.run()
print(len(robot.painted))

robot = Robot()
robot.colors[ivec2(0, 0)] = 1
vm = IntcodeVM(code.copy(), robot, robot)
vm.run()

width = glm.max(robot.painted).x
height = -glm.min(robot.painted).y
for y in range(height + 1):
    for x in range(width + 1):
        print("||" if robot.colors.get(ivec2(x, -y), 0) == 1 else "  ", end="")
    print()
