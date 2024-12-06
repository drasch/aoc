from collections import defaultdict


class GridException(BaseException):
    pass


class Grid:
    grid: list[str] = []
    width: str | None = None

    def __init__(self, data_iter):
        for line in data_iter:
            line = line.strip()
            if not line or not len(line):
                break

            if not self.width:
                self.width = len(line)

            assert self.width == len(line)

            self.grid.append(line)

        row_pos = next(
            (index for index, row in enumerate(self.grid) if "^" in row), None
        )
        if not row_pos:
            raise GridException("guard not found!")

        col_pos = self.grid[row_pos].index("^")
        self.pos = (row_pos, col_pos)

    @property
    def height(self):
        return len(self.grid)


test_data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
""".split()

grid_sample = Grid(test_data)

with open("input") as file:
    grid = Grid(file)


def test_grid_loader():
    assert grid_sample.pos == (6, 4)


__all__ = ["grid", "test_grid"]
