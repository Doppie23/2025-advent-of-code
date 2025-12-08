from collections import defaultdict

with open("./input/day07.txt") as f:
    input = f.read()

lines = input.split("\n")

s = lines[0].find("S")
beams = set([s])
beams_p2 = defaultdict(int)
beams_p2[s] = 1

p1 = 0

for l in lines[1:]:
    for i, c in enumerate(l):
        if c == "^" and i in beams:
            p1 += 1
            beams.remove(i)
            beams.add(i + 1)
            beams.add(i - 1)

            beams_p2[i + 1] += beams_p2[i]
            beams_p2[i - 1] += beams_p2[i]
            beams_p2[i] = 0

print(p1)
print(sum(beams_p2.values()))
