with open("./input/day04.txt") as f:
    input = f.read()

lines = input.split("\n")[:-1]
w = len(lines[0])
h = len(lines)

nl = []
for l in lines:
    chars = list(map(lambda x: x, l))
    nl.append(chars)
lines = nl

p1 = 0
for r in range(h):
    for c in range(w):
        if lines[r][c] != "@":
            continue
        n = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                nr = r + i
                nc = c + j
                if 0 <= nr < h and 0 <= nc < w:
                    if lines[nr][nc] == "@":
                        n += 1
        if n < 4:
            p1 += 1

p2 = 0
while True:
    removed = 0
    for r in range(h):
        for c in range(w):
            if lines[r][c] != "@":
                continue
            n = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    nr = r + i
                    nc = c + j
                    if 0 <= nr < h and 0 <= nc < w:
                        if lines[nr][nc] == "@":
                            n += 1
            if n < 4:
                lines[r][c] = "."
                removed += 1
    if removed == 0:
        break
    p2 += removed

print(p1)
print(p2)
