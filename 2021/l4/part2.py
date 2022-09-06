from ..advent import Advent

def check_col(b, i):
    for j in range(0, 21, 5):
        if b[i + j] != -1:
            return False
    
    return True

def check_row(b, i):
    for j in range(5):
        if b[i * 5 + j] != -1:
            return False
    
    return True


def check_win(b):
    for i in range(5):
        if check_col(b, i):
            return True
        
        if check_row(b, i):
            return True
    
    return False

advent = Advent(4, 2)

data = advent.read.blocks()

draws = [int(val) for val in data[0].split(",")]

boards = [
    [
        int(val) for val in
        advent.util.flatten([
            row.split(" ") for row in board.splitlines()
        ]) if val
    ] for board in data[1:]
]

won = set()

for n in draws:
    for i, b in enumerate(boards):
        boards[i] = [val if val != n else -1 for val in b]
    
    for i, b in enumerate(boards):
        if check_win(b):
            if i not in won:
                advent.solution((sum(b) + b.count(-1)) * n)

            won.add(i)
