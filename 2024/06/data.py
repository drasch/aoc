from collections import defaultdict


class GridException(BaseException):
    pass


class Grid:
    grid: list[str]
    width: int
    height: int
    pos: tuple[int, int]
    direction: int
    directions = [(-1, 0), (0, 1), (-1, 0), (0, -1)]

    def __init__(self, data_iter):
        self.grid = []
        for line in data_iter:
            line = line.strip()
            if not line or not len(line):
                break

            if not hasattr(self, "width"):
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

    @property
    def next_move(self):
        return (
            self.pos[0] + self.move_direction[0],
            self.pos[1] + self.move_direction[1],
        )

    @property
    def blocked(self):
        return (
            self.pos[0] + self.move_direction[0],
            self.pos[1] + self.move_direction[1],
        )

    @property
    def in_bounds(self):
        return self.pos[0] in range(0, self.height) and self.pos[1] in range(
            0, self.width
        )

    def __repr__(self):
        return f"<Grid pos={self.pos} height={self.height} width={self.width} direction={self.move_direction}>"


grid_data_test = """....#.....
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


def test_grid_loader():
    grid_sample = Grid(grid_data_test)
    assert grid_sample.pos == (6, 4)
    assert grid_sample.next_move == (5, 4)


def test_turn():
    grid_sample = Grid(grid_data_test)
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


def test_out():
    grid_sample = Grid(grid_data_test)
    assert grid_sample.in_bounds
    grid_sample.pos = (-1, 4)
    assert not grid_sample.in_bounds
    grid_sample.pos = (3, -1)
    assert not grid_sample.in_bounds
    grid_sample.pos = (1, 9)
    assert grid_sample.in_bounds
    grid_sample.pos = (1, 10)
    assert not grid_sample.in_bounds
    grid_sample.pos = (10, 1)
    assert not grid_sample.in_bounds


with open("input") as file:
    grid = Grid(file)

grid_sample = Grid(grid_data_test)

__all__ = ["grid", "test_grid"]
