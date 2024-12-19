from advent import Advent
import functools

input_data = Advent().read.blocks()()
elements = input_data[0].split(", ")
words = input_data[1].splitlines()


@functools.cache
def ways_to_create(word: str) -> int:
    if len(word) == 0:
        return 1
    return sum(ways_to_create(word[len(el):]) for el in elements if word.startswith(el))


print(sum(ways_to_create(word) > 0 for word in words))
print(sum(map(ways_to_create, words)))
