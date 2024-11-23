from advent import Advent


conversions_str, input_str = Advent().read.blocks()()
conversions = {}
for ln in conversions_str.splitlines():
    from_, to = ln.split(" => ")
    if (conv := conversions.get(from_)) is not None:
        conv.append(to)
    else:
        conversions[from_] = [to]
conversions = tuple(conversions.items())


class HashableDict[K, V](dict[K, V]):
    def __hash__(self):
        return id(self)


def replacements(string: str) -> set[str]:
    results = set()
    for i in range(len(string)):
        for from_str, options in conversions:
            from_len = len(from_str)
            if string[i:i+from_len] == from_str:
                a = string[:i]
                b = string[i+from_len:]
                for opt in options:
                    results.add(f"{a}{opt}{b}")
    return results


print(len(replacements(input_str)))


reverse_replacements = [(v, k) for k, vs in conversions for v in vs]
reverse_replacements.sort(key=lambda pair: len(pair[0]), reverse=True)


def replacements_2(string: str) -> str:
    for f, t in reverse_replacements:
        for i in range(len(string)):
            if string[i:i+len(f)] == f:
                yield f"{string[:i]}{t}{string[i+len(f):]}"


visited = {input_str}
molecules = [input_str]

step = 0
while True:
    new_molecules = []
    for mol in molecules:
        if mol == "e":
            break
        for comp in replacements_2(mol):
            if comp in visited:
                continue
            visited.add(comp)
            new_molecules.append(comp)
            break
    molecules = new_molecules
    if len(molecules) == 0:
        break
    step += 1
print(step)
