from collections import defaultdict

from ..advent import Advent

advent = Advent(14, 2)

template, rules = advent.read.blocks()
template = ["".join(pair) for pair in advent.util.pairs_overlay(template)]
rules = {k: v for k, v in [rule.split(" -> ") for rule in rules.splitlines()]}

polymer = defaultdict(int)
for pair in template:
    polymer[pair] += 1

print(polymer)

for _ in range(40):
    npolymer = defaultdict(int)

    for pair, n in polymer.items():
        npolymer[pair[0] + rules[pair]] += n
        npolymer[rules[pair] + pair[1]] += n
    
    polymer = npolymer

ecounts = defaultdict(int)
for pair, n in polymer.items():
    ecounts[pair[0]] += n
ecounts[template[-1][1]] += 1

advent.solution(max(ecounts.values()) - min(ecounts.values()))
