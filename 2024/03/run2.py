import re


lines = []

with open("input") as file:
    for line in file:
        line = line.strip()
        lines.append(line)


# lines = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))i"]

# line = lines[0]


def is_enabled(match, line):
    command_re = r"|".join(map(re.escape, ["do()"[::-1], "don't()"[::-1]]))
    disabler = re.search(command_re, line[match.start() :: -1])
    return (not disabler) or (disabler and disabler.group(0)[::-1] not in "don't()")


line = "".join(lines)

filtered = sum(
    [
        int(match[1]) * int(match[2])
        for match in re.finditer(r"mul\((\d+),(\d+)\)", line)
        if is_enabled(match, line)
    ]
)
print(filtered)