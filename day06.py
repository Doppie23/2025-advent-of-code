from functools import reduce
import operator

with open("./input/day06.txt") as f:
    input = f.read()

lines = input.split("\n")

nums = [x for x in [l.split(" ") for l in lines[:-2]]]
nums = [[int(x) for x in l if x] for l in nums]

ops = [x for l in lines[-2] for x in l.split(" ") if x]

p1 = 0
rows = len(nums)
for i, op in enumerate(ops):
    num = [nums[r][i] for r in range(rows)]
    if op == "+":
        p1 += sum(num)
    elif op == "*":
        p1 += reduce(operator.mul, num, 1)

print(p1)

lines = lines[:-2]
cols = []
i = 0
while i < len(lines[0]):
    start = i
    d = [l[i] for l in lines]
    while not all([l[i] == " " for l in lines]):
        i += 1
        if i >= len(lines[0]):
            break
    cols.append([l[start:i] for l in lines])
    i += 1

p2 = 0
for i, col in enumerate(cols):
    acc = 0 if ops[i] == "+" else 1
    for j in range(len(col[0])):
        s = "".join([c[j] for c in col])
        if ops[i] == "+":
            acc += int(s)
        else:
            acc *= int(s)
    p2 += acc

print(p2)
