from advent import Advent

from typing import Callable, Iterable, Iterator, Sequence
import itertools

code: list[int] = Advent().read.split(",").map(int)()


type Param = tuple[int, int]


class IntcodeVM:
    data: list[int]
    pc: int
    _running: bool
    _exited: bool
    _ins_table: dict[int, tuple[Callable[[Param, ...], None | int], int]]
    _input_iter: Iterator[int]
    _output_func: Callable[[int], None]

    def __init__(self, data: list[int], inputs: Iterable[int], output_func: Callable[[int], None]):
        self.data = data
        self.pc = 0
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
        return self.data[index]

    def __setitem__(self, index: int, value: int):
        self.data[index] = value

    def load(self, param: Param) -> int:
        mode, x = param
        if mode == 0:
            return self[x]
        elif mode == 1:
            return x
        else:
            raise ValueError(f"Invalid parameter load mode: {mode}")

    def store(self, param: Param, value: int):
        mode, x = param
        if mode == 0:
            self[x] = value
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

    def ins_exit(self):
        self._running = False
        self._exited = True


class OutputBuffer:
    data: list[int]

    def __init__(self):
        self.data = []

    def __call__(self, x: int):
        self.data.append(x)

    def __getitem__(self, item: int) -> int:
        return self.data[item]


class Pipe:
    data: list[int]
    src: IntcodeVM = None
    dst: IntcodeVM = None

    def __init__(self, start_data: list[int] = None):
        self.data = [] if start_data is None else start_data

    def __call__(self, x: int):
        self.data.append(x)
        self.src.pause()

    def __iter__(self):
        return self

    def __next__(self):
        while len(self.data) == 0:
            self.src.run()
        return self.data.pop(0)


def get_signal(phases: Iterable[int]) -> int:
    signal = 0
    buf = OutputBuffer()
    for phase in phases:
        vm = IntcodeVM(code.copy(), (phase, signal), buf)
        vm.run()
        signal = buf[-1]
    return signal


print(max(get_signal(option) for option in itertools.permutations(range(5))))


def get_feedback_loop_signal(phases: Sequence[int]) -> int:
    pipes = [Pipe([phase]) for i, phase in enumerate(phases)]
    pipes[0].data.append(0)
    vms = [IntcodeVM(code.copy(), pipes[i - 1], pipes[i]) for i in range(len(phases))]
    for i, vm in enumerate(vms):
        pipes[i].src = vm
        pipes[i].dst = vms[(i + 1) % len(pipes)]
    while not vms[-1].run():
        pass
    return next(pipes[-1])


print(max(get_feedback_loop_signal(option) for option in itertools.permutations(range(5, 10))))
