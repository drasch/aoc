
lines = [i.strip() for i in open("input", "r").readlines()]


x, y = 0, 0
treecount = 0

while y < len(lines):
    line = lines[y]
    if line[x%len(line)] == "#":
        treecount += 1

    x+=3
    y+=1

print(treecount)
