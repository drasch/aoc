from collections import defaultdict, Counter, deque


class GridException(BaseException):
    pass


class Grid:
    grid: list[str]
    width: int
    height: int
    pos: tuple[int, int]
    direction: int
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    turns: list[tuple[int, int]]

    def __init__(self, data_iter):
        self.grid = []
        self.turns = []
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
        return self.directions[self.direction]

    def move(self):
        if self.blocked:
            raise GridException("tried to move while blocked!")

        self.pos = self.next_move

    @property
    def next_move(self):
        return (
            self.pos[0] + self.move_direction[0],
            self.pos[1] + self.move_direction[1],
        )

    @property
    def blocked(self):
        return self.pos_in_bounds(self.next_move) and self.grid[self.next_move[0]][
            self.next_move[1]
        ] in ("#", "O")

    def pos_in_bounds(self, pos):
        return pos[0] in range(0, self.height) and pos[1] in range(0, self.width)

    @property
    def in_bounds(self):
        return self.pos_in_bounds(self.pos)

    def run(self, limit=-1):
        self.moves = defaultdict(int)
        last = deque()
        while self.pos_in_bounds(self.pos) and (limit < 0 or limit > 0):
            self.moves[self.pos] += 1

            if len(last) > 2:
                last.popleft()
            last.append(self.moves[self.pos])
            if self.moves[self.pos] > 3 or len(set(last)) == 1 and last[0] > 3:
                print("breaking")
                return -1

            if self.blocked:
                self.turns.append(self.pos)
            while self.blocked:
                self.turn_right()
            self.move()
            limit -= 1

        if limit == 0:
            return -1
        return len(self.moves)

    def block(self, pos):
        self.grid[pos[0]] = (
            self.grid[pos[0]][: pos[1]] + "O" + self.grid[pos[0]][pos[1] + 1 :]
        )

    def __repr__(self):
        return f"<Grid pos={self.pos} height={self.height} width={self.width} direction={self.move_direction}>"

    def print_grid(self):
        for i in range(self.height):
            print(self.grid[i])


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
    grid_sample.pos = (0, 9)
    assert grid_sample.in_bounds
    grid_sample.pos = (1, 10)
    assert not grid_sample.in_bounds
    grid_sample.pos = (10, 1)
    assert not grid_sample.in_bounds


def test_cycle():
    grid_sample = Grid(grid_data_test)
    grid_sample.block((6, 3))
    assert grid_sample.run() == -1


def test_blocked():
    grid_sample = Grid(grid_data_test)
    assert not grid_sample.blocked
    grid_sample.pos = (1, grid_sample.pos[1])
    assert grid_sample.blocked

    # blocked words on edge -- not blocked
    grid_sample.pos = (0, grid_sample.pos[1])
    assert not grid_sample.blocked
    grid_sample.pos = (0, grid_sample.width - 1)
    grid_sample.turn_right()
    assert not grid_sample.blocked


def file_grid():
    with open("input") as file:
        grid = Grid(file)
        return grid


grid_sample = Grid(grid_data_test)


def sliding_window(iterable, window_size):
    """
    Generates a sliding window iterator over the given iterable.
    """
    for i in range(len(iterable) - window_size + 1):
        yield iterable[i : i + window_size]


def cmp(a, b):
    return (a > b) - (a < b)


def not_run_block_scenarios(turns):
    ct = 0
    for steps in sliding_window(turns, 3):
        ys = Counter([pos[0] for pos in steps])
        xs = Counter([pos[1] for pos in steps])
        print(steps)
        print(xs)
        print(ys)

        if len(xs) == 2 and len(ys) == 2:
            # complete the square!
            for key in xs.keys():
                if xs[key] == 1:
                    x = key
                    break
            for key in ys.keys():
                if ys[key] == 1:
                    y = key
                    break
            print(x)
            print(y)
            block = (y + cmp(y, steps[2][0]), x + cmp(x, steps[2][1]))
            grid = file_grid()
            if grid.grid[block[0]][block[1]] != ".":
                continue
            grid.block(block)
            if grid.run_check_loop():
                ct += 1
                break
    return ct


def brute_run_block_scenarios():
    grid = file_grid()
    ct = 0
    for y in range(grid.height):
        for x in range(grid.width):
            grid = file_grid()
            if grid.grid[y][x] != ".":
                continue
            grid.block((y, x))
            if grid.run_check_loop():
                ct += 1
        print(f"ct: {ct}")
    return ct


def run_block_scenarios(moves):
    grid_orig = file_grid()
    moves = set(moves.keys())

    ct = 0
    for spot in list(moves):
        for y, x in [
            (spot[0] + d[0], spot[1] + d[1])
            for d in grid_orig.directions
            if (spot[0] + d[0], spot[1] + d[1]) not in moves
        ]:
            moves.add((y, x))
            grid = file_grid()
            if grid.grid[y][x] != ".":
                continue
            grid.block((y, x))
            if grid.run(10000) == -1:
                print(f"ct: {ct}")
                ct += 1
    print(f"ct: {ct}")
    return ct


__all__ = ["grid", "test_grid"]

if __name__ == "__main__":
    print(grid_sample.run())
    grid = file_grid()
    print(grid.run())
    moves = grid.moves
    print(run_block_scenarios(moves))
