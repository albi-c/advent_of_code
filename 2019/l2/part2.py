from ..advent import Advent, IntcodeVM

advent = Advent(2)

data = advent.read.separated(",", int)

for a in range(100):
    for b in range(100):
        vm = IntcodeVM(data)
        vm[1] = a
        vm[2] = b
        vm.run()
        if vm[0] == 19690720:
            advent.solution(100 * a + b)
