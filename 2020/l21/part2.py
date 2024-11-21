from advent import Advent


def parse_line(ln: str) -> tuple[list[str], set[str]]:
    spl = ln[:-1].split(" (contains ")
    return spl[0].split(" "), set(spl[1].split(", "))


data = Advent().read.lines().map(parse_line)()


all_ingredients: set[str] = set()
allergen_options: dict[str, set[str]] = {}

for ingredients, allergens in data:
    ingredient_set = set(ingredients)

    all_ingredients |= ingredient_set

    for allergen in allergens:
        if allergen in allergen_options:
            allergen_options[allergen] &= ingredient_set
        else:
            allergen_options[allergen] = ingredient_set.copy()

found = True
while found:
    found = False
    for allergen, ingredients in allergen_options.items():
        if len(ingredients) == 1:
            ingredient = next(iter(ingredients))
            for allergen_, ingredients_ in allergen_options.items():
                if allergen != allergen_ and ingredient in ingredients_:
                    ingredients_.remove(ingredient)
                    found = True

print(",".join(next(iter(pair[1])) for pair in sorted(allergen_options.items(), key=lambda pair: pair[0])))
