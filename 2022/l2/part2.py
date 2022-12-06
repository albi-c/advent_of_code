from ..advent import Advent

advent = Advent(2)

SHAPES = {
    "A": 0,
    "B": 1,
    "C": 2,

    "X": 0,
    "Y": 1,
    "Z": 2
}

BEATS = [2, 0, 1]
RBEATS = [1, 2, 0]
SCORE = [1, 2, 3]


def calc_score(move: list[int]) -> int:
    if move[1] == 0:
        return SCORE[BEATS[move[0]]]

    elif move[1] == 1:
        return 3 + SCORE[move[0]]

    return 6 + SCORE[RBEATS[move[0]]]


data = advent.read.lines(lambda ln: [SHAPES[shape] for shape in ln.split()])

advent.solution(sum(map(calc_score, data)))
