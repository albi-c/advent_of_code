from advent import Advent, Stream, X, Util


advent = Advent()


# [(destination_start, source_start, length)]
Map = list[tuple[int, ...]]


# (start, length)
Range = tuple[int, int]


data: list[list[str]] = advent.read.blocks().lines()()

seeds = list(map(int, data[0][0].split(": ")[1].split(" ")))


def parse_map(map_data: list[str]) -> Map:
    return sorted([tuple(map(int, row.split())) for row in map_data], key=lambda m: m[0])


maps = Stream(data).skip(1).map(X[1:]).map(parse_map).to(list)


def map_lookup(map_: Map, value: int) -> int:
    for row in map_:
        if row[1] <= value < row[1] + row[2]:
            return value - row[1] + row[0]

    return value


def chain_map_lookup(value: int) -> int:
    for map_ in maps:
        value = map_lookup(map_, value)
    return value


print(min(map(chain_map_lookup, seeds)))


def map_lookup_range(map_: Map, values: list[Range]) -> list[Range]:
    output = []

    for start, length in values:
        end = start + length
        mapped = False

        for r_d_start, r_s_start, r_length in map_:
            r_s_end = r_s_start + r_length

            if start < r_s_end and end > r_s_start:
                mapped = True

                if start < r_s_start:
                    output.append((start, r_s_start - start))

                overlap_start = max(start, r_s_start)
                output.append((
                    r_d_start + (overlap_start - r_s_start),
                    min(end, r_s_end) - overlap_start
                ))

                if end > r_s_end:
                    start = r_s_end
                    length = end - r_s_end
                    continue

        if not mapped:
            output.append((start, length))

    return output


def chain_map_lookup_range(values: list[Range]) -> list[Range]:
    for map_ in maps:
        values = map_lookup_range(map_, values)
    return values


ranges = [(a, b) for a, b in Util.chunks(seeds, 2)]


print(min(ran[0] for ran in chain_map_lookup_range(ranges)))
