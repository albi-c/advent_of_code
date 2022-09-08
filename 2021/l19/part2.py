from ..advent import Advent, vec3

advent = Advent(19, 2)

def resolve(i: int, j: int, scanners: list) -> tuple:
    for rotation in vec3.rotation_functions():
        scanner = set(map(rotation, scanners[j]))
        for s1 in scanners[i]:
            for s2 in scanner:
                diff = s1 - s2
                moved = set(s + diff for s in scanner)
                
                if len(scanners[i].intersection(moved)) >= 12:
                    scanners[j] = moved
                    return (True, diff)
    
    return (False, None)

scanners = [set(vec3(list(map(int, line.split(",")))) for line in block.splitlines()[1:]) for block in advent.read.blocks()]

scanner_positions = [vec3() for _ in range(len(scanners))]
unmatched = set(range(1, len(scanners)))
visit_queue = [0]
while visit_queue:
    i = visit_queue.pop()
    for j in list(unmatched):
        success, diff = resolve(i, j, scanners)
        if success:
            visit_queue.append(j)
            unmatched.remove(j)
            scanner_positions[j] = diff

max_distance = 0
for p1 in scanner_positions:
    for p2 in scanner_positions:
        max_distance = max(max_distance, p1.manhattan(p2))

advent.solution(max_distance)
