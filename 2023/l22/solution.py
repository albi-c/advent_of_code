from __future__ import annotations

from advent import Advent

from dataclasses import dataclass
import itertools
import tqdm


@dataclass
class ivec3:
    x: int
    y: int
    z: int

    __slots__ = ("x", "y", "z")

    def copy(self) -> ivec3:
        return ivec3(self.x, self.y, self.z)

    def up(self, n: int = 1) -> ivec3:
        return ivec3(self.x, self.y + n, self.z)

    def down(self, n: int = 1) -> ivec3:
        return self.up(-n)


@dataclass
class Block:
    a: ivec3
    b: ivec3

    @classmethod
    def make_swizzled(cls, a: ivec3, b: ivec3):
        return Block(ivec3(a.x, a.z, a.y), ivec3(b.x, b.z, b.y))

    def copy(self) -> Block:
        return Block(self.a.copy(), self.b.copy())

    def up(self, n: int = 1) -> Block:
        return Block(self.a.up(n), self.b.up(n))

    def down(self, n: int = 1) -> Block:
        return self.up(-n)

    def collides(self, other: Block) -> bool:
        return (self.a.x <= other.b.x and self.b.x >= other.a.x and self.a.y <= other.b.y and self.b.y >= other.a.y
                and self.a.z <= other.b.z and self.b.z >= other.a.z)


def parse_line(ln: str) -> Block:
    spl = ln.split("~")
    return Block.make_swizzled(ivec3(*map(int, spl[0].split(","))), ivec3(*map(int, spl[1].split(","))))


data: list[Block] = Advent().read.lines().map(parse_line)()

floor = Block(ivec3(0, 0, 0), ivec3(max(b.b.x for b in data), 0, max(b.b.z for b in data)))


def collides(block: Block, blocks: list[Block], skipped_block: Block) -> bool:
    return block.collides(floor) or any(block.collides(b) and b is not skipped_block for b in blocks)


def make_fall(blocks: list[Block], progress: bool = True, exit_on_fall: bool = False) -> bool:
    moved = True
    for _ in (tqdm.tqdm(itertools.count(), leave=False) if progress else itertools.count()):
        if not moved:
            break
        moved = False

        for i, block in enumerate(blocks):
            down = block.down()
            if not collides(down, blocks, block):
                blocks[i] = down
                moved = True
                if exit_on_fall:
                    return moved

    return moved


def count_unique_falls(blocks: list[Block]) -> int:
    moved = True
    unique: set[int] = set()
    while moved:
        moved = False

        for i, block in enumerate(blocks):
            down = block.down()
            if not collides(down, blocks, block):
                unique.add(i)
                blocks[i] = down
                moved = True

    return len(unique)


def can_be_removed(blocks: list[Block], i: int) -> bool:
    blocks = blocks.copy()
    blocks.pop(i)

    return not make_fall(blocks, False, True)


def unique_falls(blocks: list[Block], i: int) -> int:
    blocks = blocks.copy()
    blocks.pop(i)

    return count_unique_falls(blocks)


blocks_ = data.copy()
make_fall(blocks_)

print("\n\n", sum(can_be_removed(blocks_, i) for i in tqdm.trange(len(data))))

print("\n\n", sum(unique_falls(blocks_, i) for i in tqdm.trange(len(data))))
