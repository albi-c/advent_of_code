from advent import Advent, Seq

from collections import defaultdict
from typing import Callable
import sys
import math


sys.setrecursionlimit(100000)


Module = tuple[str, Seq[str]]


def parse_line(ln: str) -> tuple[str, Module]:
    a, b = ln.split(" -> ")
    prefix = ""
    if a != "broadcaster":
        prefix = a[0]
        a = a[1:]
    return a, (prefix, Seq(b.split(", ")))


modules: dict[str, Module] = {name: module for name, module in Advent().read.lines().map(parse_line)()}
module_inputs: defaultdict[str, list[str]] = defaultdict(list)
for name, (_, destinations_) in modules.items():
    for dst_ in destinations_:
        module_inputs[dst_].append(name)

high_pulses = 0
low_pulses = 0
ff_states: defaultdict[str, bool] = defaultdict(bool)
co_states: dict[str, dict[str, bool]] = {name: {n: False for n in inputs} for name, inputs in module_inputs.items()}
queue: list[tuple[bool, str, str]] = []
low_received = set()
high_received = set()


def reset():
    global low_pulses, high_pulses, ff_states, co_states, queue, high_received, low_received
    low_pulses = 0
    high_pulses = 0
    ff_states.clear()
    co_states = {name: {n: False for n in inputs} for name, inputs in module_inputs.items()}
    queue = []
    high_received.clear()
    low_received.clear()


def get_pulse_func(pulse: bool) -> Callable[[str, str, bool], None] | Callable[[str, str], None]:
    return high if pulse else low


def low(source: str, name: str, direct: bool = False):
    if not direct:
        queue.append((False, source, name))
        return

    low_received.add(name)

    global low_pulses
    low_pulses += 1

    if name not in modules:
        return

    prefix, destinations = modules[name]

    if prefix == "":
        for dst in destinations:
            low(name, dst)
    elif prefix == "%":
        state = not ff_states[name]
        ff_states[name] = state
        f = get_pulse_func(state)
        for dst in destinations:
            f(name, dst)
    elif prefix == "&":
        co_states[name][source] = False
        for dst in destinations:
            high(name, dst)


def high(source: str, name: str, direct: bool = False):
    if not direct:
        queue.append((True, source, name))
        return

    high_received.add(name)

    global high_pulses
    high_pulses += 1

    if name not in modules:
        return

    prefix, destinations = modules[name]

    if prefix == "&":
        co_states[name][source] = True
        if all(co_states[name].values()):
            for dst in destinations:
                low(name, dst)
        else:
            for dst in destinations:
                high(name, dst)


for _ in range(1000):
    low("button", "broadcaster")

    while len(queue) > 0:
        queue2 = queue
        queue = []
        for pulse_, src_, dst_ in queue2:
            get_pulse_func(pulse_)(src_, dst_, True)

print(low_pulses * high_pulses)


reset()


to_rx = module_inputs[module_inputs["rx"][0]]
counts = []
for to in to_rx:
    reset()

    i = 0
    while to not in low_received:
        low("button", "broadcaster")

        while len(queue) > 0:
            queue2 = queue
            queue = []
            for pulse_, src_, dst_ in queue2:
                get_pulse_func(pulse_)(src_, dst_, True)

        i += 1

    counts.append(i)

print(math.lcm(*counts))
