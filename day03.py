with open("./input/day03.txt") as f:
    input = f.read()

p1 = 0
for line in input.split("\n"):
    if not line:
        continue
    a, b = line[0], line[1]
    for n in line[2:]:
        if b > a:
            a = b
            b = n
        if n > b:
            b = n
    x = int(a + b)
    p1 += x
print(f"p1: {p1}")

p2 = 0
for line in input.split("\n"):
    if not line:
        continue
    xs = line[0:12]

    for n in line[12:]:
        prev = xs[0]
        for i, x in enumerate(xs[1:]):
            if x > prev:
                xs = xs[:i] + xs[i + 1 :]
                xs += n
                break
            prev = x
        if n > xs[-1]:
            xs = xs[:-1]
            xs += n
    x = int(xs)
    p2 += x
print(f"p2: {p2}")
