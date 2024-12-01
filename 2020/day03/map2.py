
lines = [i.strip() for i in open("input", "r").readlines()]


slopes = ((1,1), (3, 1), (5, 1), (7, 1), (1, 2))
treecount = [0] * len(slopes)

for index, (slope_x, slope_y) in enumerate(slopes):
    x, y = 0, 0
    while y < len(lines):
        line = lines[y]
        if line[x%len(line)] == "#":
            treecount[index] += 1

        x+=slope_x
        y+=slope_y

print(reduce(lambda x, y: x*y, treecount, 1))
