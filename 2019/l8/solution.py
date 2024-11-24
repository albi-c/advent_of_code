from advent import Advent

import numpy as np
import itertools


dimensions = (25, 6)
layer_length = dimensions[0] * dimensions[1]

layers = tuple(np.array(layer, dtype=np.uint8)
               for layer in itertools.batched(map(int, Advent().read()), layer_length))

min_0 = min(layers, key=lambda layer: (layer == 0).sum())
print((min_0 == 1).sum() * (min_0 == 2).sum())


def combine(pixels: tuple[int, ...]) -> int:
    for pix in pixels:
        if pix < 2:
            return pix
    assert False


combined = np.array(list(map(combine, zip(*layers))), dtype=np.uint8).reshape(dimensions[::-1])
print("\n".join("".join("#" if ch == 1 else " " for ch in row) for row in combined))
