with open("./input/day01.txt") as f:
    input = f.read()

p1 = 0
p2 = 0
dir = 50
lines = input.split()
for l in lines:
    d = l[0]
    n = int(l[1:])
    if d == "L":
        n *= -1

    o_dir = dir
    new_dir = dir + n

    (x, dir) = divmod(new_dir, 100)
    p2 += abs(x) - int(o_dir == 0 and n < 0) + int(dir == 0 and n < 0)

    if dir == 0:
        p1 += 1

print(f"p1 {p1}")
print(f"p2 {p2}")
