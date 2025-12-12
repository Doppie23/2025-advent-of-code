with open("./input/day12.txt") as f:
    input = f.read()

blocks = input.split("\n\n")

shapes = []

for shape in blocks[:-1]:
    shape_size = sum(int(x == "#") for x in shape)
    shapes.append(shape_size)

p1 = 0

for line in blocks[-1].split("\n"):
    if not line:
        continue

    size, to_add = line.split(": ")
    w, h = map(int, size.split("x"))
    to_add = list(map(int, to_add.split(" ")))

    grid_size = w * h
    to_add_total_size = sum(shapes[i] * n for i, n in enumerate(to_add))

    p1 += int(to_add_total_size <= grid_size)

print(p1)
