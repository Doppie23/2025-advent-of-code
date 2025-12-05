with open("./input/day05.txt") as f:
    input = f.read()

ranges, nums = input.split("\n\n")

ranges = [(int(l), int(u)) for l, u in [s.split("-") for s in ranges.split("\n")]]
nums = [int(x) for x in nums.split("\n") if x]

p1 = 0
for n in nums:
    for l, u in ranges:
        if l <= n <= u:
            p1 += 1
            break

print(p1)

ls = sorted([x[0] for x in ranges])
us = sorted([x[1] for x in ranges])

p2 = us[0] - ls[0] + 1
for i, (l, u) in enumerate(zip(ls[1:], us[1:])):
    prev_u = us[i]
    l = max(l, prev_u + 1)
    p2 += u - l + 1

print(p2)
