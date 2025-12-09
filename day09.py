from itertools import combinations

with open("./input/day09.txt") as f:
    input = f.read()

ps = [[int(x) for x in l.split(",")] for l in input.split("\n") if l]


print(
    max(
        [
            (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            for ((x1, y1), (x2, y2)) in combinations(ps, 2)
        ]
    )
)

edges = []

for i in range(len(ps) - 1):
    p1, p2 = ps[i], ps[i + 1]
    edges.append((p1, p2))

edges.append((ps[0], ps[-1]))


def intersects(min_x, min_y, max_x, max_y):
    for (x1, y1), (x2, y2) in edges:
        e_min_x = min(x1, x2)
        e_max_x = max(x1, x2)
        e_min_y = min(y1, y2)
        e_max_y = max(y1, y2)

        if min_x < e_max_x and max_x > e_min_x and min_y < e_max_y and max_y > e_min_y:
            return True
    return False


p2 = 0

for (x1, y1), (x2, y2) in combinations(ps, 2):
    min_x = min(x1, x2)
    max_x = max(x1, x2)
    min_y = min(y1, y2)
    max_y = max(y1, y2)

    if not intersects(min_x, min_y, max_x, max_y):
        area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
        if area > p2:
            p2 = area


print(p2)
