with open("./input/day02.txt") as f:
    input = f.read()

ranges = input.split(",")

seen = set()
for ran in ranges:
    if not ran:
        continue
    ran = ran.strip()
    l, r = ran.split("-")
    lower = int(l)
    upper = int(r)

    ll = "1"
    while True:
        n = 2
        s = ll * n
        if len(ll) != 1 and len(set(s)) == 1:
            ll = str(int(ll) + 1)
            continue
        x = int(s)
        if x > upper:
            break
        while x <= upper:
            if x >= lower:
                seen.add(x)
            n += 1
            x = int(ll * n)
        ll = str(int(ll) + 1)

print(sum(seen))
