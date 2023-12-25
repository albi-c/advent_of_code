from advent import Advent

import igraph
import math


graph: dict[str, list[str]] = {ln[:3]: ln[5:].split(" ") for ln in Advent().read.lines()()}
print(math.prod(igraph.Graph.ListDict(graph).mincut().sizes()))
