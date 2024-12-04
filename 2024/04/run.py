with open("input") as file:
    lines = [line.strip() for line in file.readlines()]

slines = [
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


permutations = (-1, 0, 1)
kernels = [(x, y) for x in permutations for y in permutations if x != 0 or y != 0]

match = "XMAS"


def get_string(lines, pos, kernel, match):
    try:
        xend = pos[0] + kernel[0] * (len(match) - 1)
        yend = pos[1] + kernel[1] * (len(match) - 1)
        if not 0 <= xend <= len(lines[0]) or not 0 <= yend <= len(lines):
            return False

        return match == "".join(
            [
                lines[pos[1] + (step * kernel[1])][pos[0] + (step * kernel[0])]
                for step in range(len(match))
            ]
        )
    except IndexError:
        return False


print(
    sum(
        [
            get_string(lines, (x, y), kernel, "XMAS")
            for x in range(len(lines[0]))
            for y in range(len(lines))
            for kernel in kernels
        ]
    )
)
