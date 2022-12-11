from ..advent import Advent

advent = Advent(11)


def parse_monkey(data: str) -> dict:
    lns = data.splitlines()

    return {
        "items": list(map(int, lns[1].split(": ")[1].split(", "))),
        "operation": (lambda x: x * x) if "old * old" in lns[2] else
                     (lambda x: x * int(lns[2].split(" * ")[1])) if "*" in lns[2] else
                     (lambda x: x + int(lns[2].split(" + ")[1])),
        "test": int(lns[3].split("by ")[1]),
        "true": int(lns[4].split("monkey ")[1]),
        "false": int(lns[5].split("monkey ")[1]),
        "inspected": 0
    }


monkeys = list(map(parse_monkey, advent.read.blocks()))

for _ in range(20):
    for m in monkeys:
        for i in range(len(m["items"])):
            m["inspected"] += 1
            m["items"][i] = m["operation"](m["items"][i]) // 3
            monkeys[m["true"] if m["items"][i] % m["test"] == 0 else m["false"]]["items"].append(m["items"][i])
        m["items"] = []

monkeys.sort(key=lambda monkey: monkey["inspected"])
advent.solution(monkeys[-1]["inspected"] * monkeys[-2]["inspected"])
