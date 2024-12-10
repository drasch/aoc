from collections import defaultdict
from typing import DefaultDict
import string

ANT_CHARS = string.ascii_letters + string.digits

type Position = tuple[int, int]


class GridException(BaseException):
    pass


class Grid:
    grid: list[str]
    width: int
    height: int
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    antennae: DefaultDict[str, list[Position]]

    def __init__(self, filename: str):
        with open(filename, "r") as file:
            self.antennae = defaultdict(list)
            self.grid = []
            for line in file:
                line = line.strip()
                if not line or not len(line):
                    break

                if not hasattr(self, "width"):
                    self.width = len(line)

                assert self.width == len(line)

                self.grid.append(line)
            self.height = len(self.grid)

    def pos_in_bounds(self, pos: Position):
        return pos[0] in range(0, self.height) and pos[1] in range(0, self.width)

    def place_antinode(self, pos: Position):
        if not self.pos_in_bounds(pos):
            raise GridException(f"antinode placed at invalid location {pos}")
        self.grid[pos[0]] = (
            self.grid[pos[0]][: pos[1]] + "O" + self.grid[pos[0]][pos[1] + 1 :]
        )

    def __repr__(self):
        return f"<Grid height={self.height} width={self.width}>"

    def print_grid(self):
        for i in range(self.height):
            print(self.grid[i])


def test_grid_loader():
    grid_sample = Grid("input.test")
    assert grid_sample.width == 12
    assert grid_sample.height == 12


def test_out():
    grid_sample = Grid("input.test")
    assert not grid_sample.pos_in_bounds((-1, 4))
    assert not grid_sample.pos_in_bounds((3, -1))
    assert grid_sample.pos_in_bounds((1, 9))
    assert grid_sample.pos_in_bounds((0, 9))
    assert not grid_sample.pos_in_bounds((1, 12))
    assert not grid_sample.pos_in_bounds((12, 1))


def cmp(a: int, b: int):
    return (a > b) - (a < b)


def grid_sample() -> Grid:
    return Grid("input.test")


def grid_final() -> Grid:
    return Grid("input")


if __name__ == "__main__":
    print(grid_sample().run())
    grid = grid_final()
    print(grid.run())
