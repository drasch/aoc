from collections import defaultdict


class GridException(BaseException):
    pass


class Grid:
    grid: list[str] = []
    width: str | None = None
    pos: tuple[int, int]
    direction: int
    directions = [(-1, 0), (0, 1), (-1, 0), (0, -1)]

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
        self.direction = 0

    @property
    def height(self):
        return len(self.grid)

    def turn_right(self):
        self.direction = (self.direction + 1) % 4

    @property
    def move_direction(self):
        print(self.directions)
        return self.directions[self.direction]


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


def test_turn():
    assert grid_sample.direction == 0
    assert grid_sample.move_direction == (-1, 0)  # starts moving up
    grid_sample.turn_right()
    assert grid_sample.direction == 1
    assert grid_sample.move_direction == (0, 1)  # moving right
    grid_sample.turn_right()
    assert grid_sample.direction == 2
    grid_sample.turn_right()
    assert grid_sample.direction == 3
    grid_sample.turn_right()  # up again?
    assert grid_sample.direction == 0


__all__ = ["grid", "test_grid"]
