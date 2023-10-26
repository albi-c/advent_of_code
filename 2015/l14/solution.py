from advent import Advent


class Reindeer:
    r: tuple[int, int, int]
    # negative is resting, positive is running
    state: int
    distance: int
    points: int

    def __init__(self, r: tuple[int, int, int]):
        self.r = r
        self.state = r[1]
        self.distance = 0
        self.points = 0

    def step(self) -> int:
        if self.state < 0:
            self.state += 1
            if self.state == 0:
                self.state = self.r[1]

        elif self.state > 0:
            self.state -= 1
            self.distance += self.r[0]
            if self.state == 0:
                self.state = -self.r[2]

        return self.distance


advent = Advent()

data = [(int(ln[3]), int(ln[6]), int(ln[-2])) for ln in advent.read.lines().split(" ")()]

def simulate_reindeer(t: int, r: tuple[int, int, int]) -> int:
    distance = 0
    while t > 0:
        distance += min(t, r[1]) * r[0]
        t -= r[1]
        t -= r[2]
    return distance

print(max(simulate_reindeer(2503, r) for r in data))

reindeer = list(map(Reindeer, data))
for _ in range(2503):
    for r in reindeer:
        r.step()
    d = max(reindeer, key=lambda r: r.distance).distance
    for r in reindeer:
        if r.distance == d:
            r.points += 1
print(max(reindeer, key=lambda r: r.points).points)
