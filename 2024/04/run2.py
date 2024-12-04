import itertools

with open("input") as file:
    lines = [line.strip() for line in file.readlines()]

splines = [
    line.strip()
    for line in """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".split()
]


kernels = [(-1, -1), (1, 1)]

match = "MAS"


def get_string(lines, pos, kernel, match):
    xend = pos[0] + kernel[0] * (len(match) - 1)
    yend = pos[1] + kernel[1] * (len(match) - 1)
    if (
        min(xend, yend, *pos) < 0
        or max(xend, pos[0]) >= len(lines[0])
        or max(yend, pos[1]) >= len(lines)
    ):
        return False
    return match == "".join(
        [
            lines[pos[1] + (step * kernel[1])][pos[0] + (step * kernel[0])]
            for step in range(len(match))
        ]
    )


print(
    sum(
        [
            get_string(lines, (x, y), kernel, match)
            and (
                get_string(
                    lines, (x, y + (2 * kernel[1])), (kernel[0], -kernel[1]), match
                )
                or get_string(
                    lines, (x + (2 * kernel[0]), y), (-kernel[0], kernel[1]), match
                )
            )
            for x in range(len(lines[0]))
            for y in range(len(lines))
            for kernel in kernels
        ]
    )
)
