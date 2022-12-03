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
SCORE = [1, 2, 3]


def calc_score(move: list[int]) -> int:
    if move[0] == move[1]:
        return 3 + SCORE[move[1]]

    elif BEATS[move[0]] == move[1]:
        return SCORE[move[1]]

    return 6 + SCORE[move[1]]


data = advent.read.lines(lambda ln: [SHAPES[shape] for shape in ln.split()])

score = 0
for m in data:
    score += calc_score(m)

advent.solution(score)
