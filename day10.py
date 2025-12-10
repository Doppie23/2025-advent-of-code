from pulp import *
from collections import deque

with open("./input/day10.txt") as f:
    input = f.read()

lines = input.split("\n")


def to_binary(s):
    s = s[1:-1]
    n = 0
    for c in s.split(","):
        n |= 1 << int(c)
    return n


def printb(n):
    print("{:03b}".format(n))


p1 = 0

for row in lines:
    if not row:
        continue

    row = row.split(" ")
    state = str([i for i, c in enumerate(row[0][1:]) if c == "#"])
    state = to_binary(state)

    buttons = [to_binary(m) for m in row[1:-1]]
    seen = set()

    # state, #moves
    q = deque([(0, 0)])

    while len(q) > 0:
        s, n = q.popleft()

        if s in seen:
            continue
        seen.add(s)

        if s == state:
            p1 += n
            break

        for m in buttons:
            q.append((s ^ m, n + 1))

p2 = 0

# g_j = goal presses at index j
# a_i_j = {0, 1} button i increments index j
#
# x_i = amount of presses on button i
#
# min sum_i x_i
#   minimize amount of button presses
#
# sum_i x_i * a_i_j = g_j foreach j


for row in lines:
    if not row:
        continue

    row = row.split(" ")

    g = [int(l) for l in row[-1][1:-1].split(",")]
    print(g)

    buttons = [[int(l) for l in pattern[1:-1].split(",")] for pattern in row[1:-1]]

    a = []
    for i in range(len(buttons)):
        increments = set(buttons[i])
        idxs = []
        for j in range(len(g)):
            idxs.append(1 if j in increments else 0)
        a.append(idxs)
    print(a)

    x = []
    for i in range(len(buttons)):
        xi = LpVariable(f"x_{i}", lowBound=0, cat="Integer")
        x.append(xi)

    prob = LpProblem("ilp", LpMinimize)

    # objective
    prob += pulp.lpSum(x)

    for j in range(len(g)):
        prob += lpSum(x[i] * a[i][j] for i in range(len(buttons))) == g[j]

    status = prob.solve()
    # print(status)
    print(LpStatus[status])
    res = sum(value(x_i) for x_i in x)
    print(f"res: {res}")
    p2 += res


print(f"p2: {p2}")
