from __future__ import annotations

from advent import Advent

from dataclasses import dataclass
import itertools


@dataclass(frozen=True, slots=True)
class Item:
    cost: int
    damage: int
    armor: int


@dataclass(slots=True)
class Fighter:
    health: int
    damage: int = 0
    armor: int = 0

    def add_stats(self, item: Item | None):
        if item is not None:
            self.damage += item.damage
            self.armor += item.armor

    def copy(self) -> Fighter:
        return Fighter(self.health, self.damage, self.armor)


WEAPONS = (
    Item(8, 4, 0),
    Item(10, 5, 0),
    Item(25, 6, 0),
    Item(40, 7, 0),
    Item(74, 8, 0)
)

ARMOR = (
    Item(13, 0, 1),
    Item(31, 0, 2),
    Item(53, 0, 3),
    Item(75, 0, 4),
    Item(102, 0, 5),
    None
)

RINGS = (
    Item(25, 1, 0),
    Item(50, 2, 0),
    Item(100, 3, 0),
    Item(20, 0, 1),
    Item(40, 0, 2),
    Item(80, 0, 3)
)

player = Fighter(100)
boss = Fighter(*(int(ln.rsplit(" ", 1)[1]) for ln in Advent().read.lines()()))


def simulate(a: Fighter, b: Fighter) -> bool:
    ah = a.health
    bh = b.health
    while True:
        ah -= max(1, b.damage - a.armor)
        if ah <= 0:
            return False
        bh -= max(1, a.damage - b.armor)
        if bh <= 0:
            return True


best = 1 << 30
worst = 0
for weapon in WEAPONS:
    for armor in ARMOR:
        for n_rings in range(3):
            for rings in itertools.combinations(RINGS, n_rings):
                p = player.copy()
                p.add_stats(weapon)
                p.add_stats(armor)
                for ring in rings:
                    p.add_stats(ring)
                cost = weapon.cost + sum(ring.cost for ring in rings)
                if armor is not None:
                    cost += armor.cost
                if simulate(p, boss):
                    best = min(best, cost)
                else:
                    worst = max(worst, cost)
print(best)
print(worst)
