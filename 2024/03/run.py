import re


lines = []

with open("input") as file:
    for line in file:
        line = line.strip()
        lines.append(line)

filtered = sum(
    [
        sum([int(n1) * int(n2) for n1, n2 in re.findall(r"mul\((\d+),(\d+)\)", line)])
        for line in lines
    ]
)
print(filtered)
