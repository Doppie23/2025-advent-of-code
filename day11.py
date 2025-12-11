from functools import cache

with open("./input/day11.txt") as f:
    input = f.read()

g = dict()

for l in input.split("\n"):
    if not l:
        continue

    f, t = l.split(": ")
    g[f] = t.split(" ")


@cache
def dfs(n, to_see: frozenset):
    if n == "out":
        return int(len(to_see) == 0)

    if n in to_see:
        to_see = to_see.difference({n})

    return sum(dfs(c, to_see) for c in g[n])


print(dfs("you", frozenset({})))
print(dfs("svr", frozenset({"fft", "dac"})))
