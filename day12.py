with open("./input/day12.txt") as f:
    input = f.read()


def list_grid_print(xs):
    for x in xs:
        print(grid_to_string(x))
        print()


def grid_to_string(s: list[list[bool]]):
    return "\n".join("".join("#" if c else "." for c in r) for r in s)


def all_variations(s: list[list[bool]]):
    seen = set([grid_to_string(s)])
    res = [s]

    # rotate
    for _ in range(3):
        last = res[-1]
        rotated = [list(row) for row in zip(*last[::-1])]

        str = grid_to_string(rotated)
        if str not in seen:
            seen.add(str)
            res.append(rotated)

    # flip
    for m in res.copy():
        h = len(m)
        w = len(m[0])
        nm = []
        for r in range(h):
            nr = []
            for c in range(w):
                c = w - c - 1
                nr.append(m[r][c])
            nm.append(nr)
        str = grid_to_string(nm)
        if str not in seen:
            seen.add(str)
            res.append(nm)

    return res


# to_add is list with at each index i how much to still fit in the grid of shapes[i]
def fits(grid: list[list[bool]], to_add: list[int], shapes) -> bool:
    # if all(x == 0 for x in to_add):
    #     return True

    h = len(grid)
    w = len(grid[0])

    remaining_to_add_size = sum(shapes[i][1] * n for i, n in enumerate(to_add))
    empty_space = sum(int(not x) for row in grid for x in row)

    return remaining_to_add_size <= empty_space  # ._.

    if remaining_to_add_size > empty_space:
        return False

    # first non-zero index
    si = [i for i, x in enumerate(to_add) if x > 0][0]
    to_add[si] -= 1
    shape_variations, size = shapes[si]

    # try each place, check if all trues at s are false in grid.
    # if not, move one over, tried all places, move to next variation
    # if we found a fit, decrease to_add, recuse in fits
    # if fits return true, we are done, return true,
    # if fits is false, undo modificatoins, and continue trying

    for s in shape_variations:
        sh = len(s)
        sw = len(s[0])

        for dr in range(h - sh + 1):
            for dc in range(w - sw + 1):
                space = all(
                    not grid[dr + sr][dc + sc] if s[sr][sc] else True
                    for sr in range(sh)
                    for sc in range(sw)
                )
                if not space:
                    continue

                for sr in range(sh):
                    for sc in range(sw):
                        if s[sr][sc]:
                            grid[dr + sr][dc + sc] = s[sr][sc]

                success = fits(grid, to_add, shapes)
                if success:
                    return True

                # backtrack
                for sr in range(sh):
                    for sc in range(sw):
                        if s[sr][sc]:
                            grid[dr + sr][dc + sc] = False
    to_add[si] += 1
    return False


blocks = input.split("\n\n")

shapes = []

for shape in blocks[:-1]:
    shape = shape.split("\n")
    shape = shape[1:]
    shape = [[x == "#" for x in line] for line in shape]
    size = sum(int(x) for row in shape for x in row)
    shapes.append((all_variations(shape), size))
    # print(shape)

p1 = 0

for line in blocks[-1].split("\n"):
    if not line:
        continue
    size, to_add = line.split(": ")
    to_add = list(map(int, to_add.split(" ")))
    w, h = size.split("x")
    w, h = int(w), int(h)
    grid = [[False for _ in range(w)] for _ in range(h)]

    if fits(grid, to_add, shapes):
        print(w, h)
        print(grid_to_string(grid))
        print()
        p1 += 1

    # print(grid_to_string(grid))
    # print()
print(p1)


# size = 3
# grid = [
#     [False, False, False, True],
#     [False, True, False, True],
#     [True, True, False, True],
#     [True, True, True, True],
# ]
#
#
# shapes = [
#     all_variations(
#         [
#             [True, True, True],
#             [True, False, False],
#             [True, True, True],
#         ]
#     ),
# ]
#
#
# print(fits(grid, [1], shapes))
#
# s = shapes[0][0]
# print(len(all_variations(s)))
# list_grid_print(all_variations(s))
