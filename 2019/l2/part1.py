from ..advent import Advent, IntcodeVM

advent = Advent(2)

vm = IntcodeVM(advent.read.separated(",", int))

vm[1] = 12
vm[2] = 2

vm.run()

advent.solution(vm[0])
