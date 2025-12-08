from itertools import combinations
from functools import reduce
import operator
from dataclasses import dataclass

with open("./input/day08.txt") as f:
    input = f.read()


n = 1000


@dataclass
class Point:
    x: int
    y: int
    z: int

    def __hash__(self) -> int:
        return (self.x, self.y, self.z).__hash__()

    def dist(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return (
            x * x + y * y + z * z
        )  # dont need sqrt, will only be comparing distances to each other


ps = []

for line in input.split("\n"):
    if not line:
        continue
    ps.append(Point(*[int(x) for x in line.split(",")]))

pairs = combinations(ps, 2)

pairs = sorted(pairs, key=lambda x: -x[0].dist(x[1]))

junctions: list[set[Point]] = []

unseen = set(ps)
last = None

itt = 0
part1 = None
while pairs:
    if itt >= n and part1 is None:
        best = sorted(junctions, key=lambda x: -len(x))[:3]
        part1 = reduce(operator.mul, [len(j) for j in best])
        print(f"p1: {part1}")
    itt += 1
    # for i in range(n):
    if not unseen and len(junctions) == 1:
        print(f"p2: {last[0].x * last[1].x}")
        break

    # print(junctions)
    # i = 0
    # while i < 10:
    (p1, p2) = pairs.pop()
    last = (p1, p2)
    # print(p1, p2)
    if p1 in unseen:
        unseen.remove(p1)
    if p2 in unseen:
        unseen.remove(p2)

    if p1.x == 906:
        pass

    # print(p1, p2)

    j1: set[Point] | None = None
    j1Idx = -1
    j2: set[Point] | None = None
    j2Idx = -1
    for i, j in enumerate(junctions):
        if p1 in j:
            j1 = j
            j1Idx = i
        if p2 in j:
            j2 = j
            j2Idx = i
        if j1 is not None and j2 is not None:
            break

    # print(j1 is None, j1Idx, j2 is None, j2Idx)

    if j1 is None and j2 is None:
        j = set()
        j.add(p1)
        j.add(p2)
        junctions.append(j)
        continue

    if j1 is None:
        j2.add(p1)
        continue
    if j2 is None:
        j1.add(p2)
        continue

    if j1 == j2:
        continue

    j1.update(j2)
    junctions.pop(j2Idx)

    # print(junctions)


# print([len(j) for j in junctions])
