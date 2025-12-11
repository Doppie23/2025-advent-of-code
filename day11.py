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
def dfs(n, seen_fft: bool, seen_dac: bool):
    if n == "out":
        return int(seen_dac and seen_fft)

    re_fft = False
    re_dac = False
    if n == "fft":
        seen_fft = True
        re_fft = True
    if n == "dac":
        seen_dac = True
        re_dac = True

    res = sum(dfs(c, seen_fft, seen_dac) for c in g[n])

    if re_fft:
        seen_fft = False
    if re_dac:
        seen_dac = False

    return res


print(dfs("you", True, True))
print(dfs("svr", False, False))
