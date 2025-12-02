with open("./input/day02.txt") as f:
    input = f.read()

ranges = input.split(",")

res = 0
for ran in ranges:
    if not ran:
        continue
    ran = ran.strip()
    l, r = ran.split("-")
    lower = int(l)
    upper = int(r)
    ll = l[: len(l) // 2]
    if not ll:
        ll = "1"
    ill = int(ll + ll)
    while True:
        if lower <= ill <= upper:
            res += ill
        ll = f"{int(ll) + 1}"
        ill = int(ll + ll)
        if ill > upper:
            break

print(res)
