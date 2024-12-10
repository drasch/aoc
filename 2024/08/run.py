from collections import defaultdict
from itertools import combinations
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

        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] in ANT_CHARS:
                    self.antennae[self.grid[y][x]].append((y,x))
        #print(self.antennae)

    def find_antinode(self, pos1, pos2):
        y = pos2[0]-pos1[0]
        x = pos2[1]-pos1[1]

        #print(pos1, pos2)
        pos3 = (pos2[0]+y, pos2[1]+x)
        pos4 = (pos1[0]-y, pos1[1]-x)
        return [pos for pos in [pos3, pos4] if self.pos_in_bounds(pos)]


    def find_antinodes(self):
        for key, antennae in self.antennae.items():
            for pos1, pos2 in combinations(antennae, 2):
                print(pos1, pos2)

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


def test_find_antinodes():
    grid_sample = Grid("input.test")
    pos1 = (4, 4)
    pos2 = (5, 5)
    pos3, pos4 = grid_sample.find_antinode(pos1, pos2)
    assert pos3 == (6, 6)
    assert pos4 == (3, 3)

    pos1 = (5, 5)
    pos2 = (4, 4)
    pos3, pos4 = grid_sample.find_antinode(pos1, pos2)
    assert pos4 == (6, 6)
    assert pos3 == (3, 3)

    pos1 = (5, 5)
    pos2 = (7, 4)
    pos3, pos4 = grid_sample.find_antinode(pos1, pos2)
    assert pos3 == (9, 3)
    assert pos4 == (3, 6)

    pos1 = (3, 3)
    pos2 = (5, 1)
    (pos3,) = grid_sample.find_antinode(pos1, pos2)
    assert pos3 == (1, 5)


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
    print(grid_sample().find_antinodes())
    #grid = grid_final()
    #print(grid.find_antinodes())
