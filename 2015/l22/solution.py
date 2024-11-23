from advent import Advent

import functools


EFFECTS = (("recharge", 229, 5), ("poison", 173, 6), ("shield", 113, 6))


boss_health, boss_damage = (int(ln.rsplit(" ", 1)[1]) for ln in Advent().read.lines()())


class HashableDict[K, V](dict[K, V]):
    def __hash__(self):
        return hash(tuple(sorted(self.items())))


def process_effects(boss_hp: int, player_mana: int, effects: HashableDict[str, int]) \
        -> tuple[int, int, HashableDict[str, int], int]:
    armor = 0
    new_effects = HashableDict()
    for effect, time in effects.items():
        if effect == "recharge":
            player_mana += 101
        elif effect == "poison":
            boss_hp -= 3
        elif effect == "shield":
            armor += 7
        if time > 1:
            new_effects[effect] = time - 1
    return boss_hp, player_mana, new_effects, armor


@functools.cache
def solve(turn: bool, boss_hp: int, player_hp: int, player_mana: int, effects: HashableDict[str, int], part_2: bool) \
        -> int:
    if boss_hp <= 0:
        return 0

    if turn:
        if part_2:
            player_hp -= 1
            if player_hp <= 0:
                return 1 << 30

        if player_mana < 53:
            return 1 << 30

        boss_hp, player_mana, effects, armor = process_effects(boss_hp, player_mana, effects)

        if boss_hp <= 0:
            return 0

        best = solve(not turn, boss_hp - 4, player_hp, player_mana - 53, effects, part_2) + 53

        if player_mana >= 73:
            best = min(best, solve(not turn, boss_hp - 2, player_hp + 2, player_mana - 73, effects, part_2) + 73)

            for effect, cost, time in EFFECTS:
                if player_mana < cost:
                    break

                if effect not in effects:
                    eff = HashableDict(effects)
                    eff[effect] = time
                    best = min(best, solve(not turn, boss_hp, player_hp, player_mana - cost, eff, part_2) + cost)

        return best

    else:
        boss_hp, player_mana, effects, armor = process_effects(boss_hp, player_mana, effects)

        if boss_hp <= 0:
            return 0
        if player_hp <= boss_damage:
            return 1 << 30

        return solve(not turn, boss_hp, player_hp - max(1, boss_damage - armor), player_mana, effects, part_2)


print(solve(True, boss_health, 50, 500, HashableDict(), False))
print(solve(True, boss_health, 50, 500, HashableDict(), True))
