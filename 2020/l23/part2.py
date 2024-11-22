from __future__ import annotations

from advent import Advent
from typing import Iterable
from dataclasses import dataclass
import itertools


class IndexedLinkedList:
    @dataclass(slots=True)
    class Node:
        next: IndexedLinkedList.Node
        value: int

        def get_next(self, n: int) -> IndexedLinkedList.Node:
            node = self
            for _ in range(n):
                node = node.next
            return node

    head: Node
    _lookup: list[Node]

    def __init__(self, values: Iterable[int], maximum_value: int):
        head = None
        tail = None
        lookup: list[IndexedLinkedList.Node] = [None for _ in range(maximum_value + 1)]
        for val in values:
            assert val >= 0
            if head is None:
                head = tail = self.Node(None, val)
                lookup[val] = head
            else:
                node = self.Node(None, val)
                tail.next = node
                tail = node
                lookup[val] = node
        tail.next = head
        self.head = head
        self._lookup = lookup

    def get(self, value: int) -> Node:
        return self._lookup[value]


type Cups = IndexedLinkedList
type Cup = IndexedLinkedList.Node


data = IndexedLinkedList(itertools.chain(map(int, Advent().read()), range(10, 1000001)), 1000000)

min_value = 1
max_value = 1000000


def do_round(cups: Cups):
    start = cups.head.next
    end = cups.head.get_next(3)
    values = (start.value, start.next.value, end.value)
    cups.head.next = end.next

    dst = cups.head.value
    while True:
        dst -= 1
        if dst < min_value:
            dst = max_value
        if dst in values:
            continue

        destination = cups.get(dst)
        end.next = destination.next
        destination.next = start

        break

    cups.head = cups.head.next


for _ in range(10000000):
    do_round(data)

base = data.get(1)
print(base.next.value * base.next.next.value)
