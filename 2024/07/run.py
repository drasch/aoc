from operator import add, mul
from itertools import product
from functools import reduce
from collections import deque


class Calibrator:
    calibrations: list[tuple[int, list[int]]]

    def __init__(self, fn):
        self.calibrations = []
        with open(fn, "r") as file:
            for line in file:
                if len(line) < 2:
                    break

                first, rest = line.strip().split(": ")
                nums = list(map(int, rest.split()))
                self.calibrations.append((int(first), nums))

    def try_sum(self, target, operands):
        concat = lambda x, y: int(str(x) + str(y))
        operations_set = [(add, mul, concat)] * (len(operands) - 1)
        operations_set = map(deque, product(*operations_set))

        return target in [
            reduce(lambda x, y: operations.popleft()(x, y), operands)
            for operations in operations_set
        ]

    def try_all(self):
        return sum(
            [
                calibration[0]
                for calibration in self.calibrations
                if self.try_sum(*calibration)
            ]
        )


if __name__ == "__main__":
    c = Calibrator("input")
    print(c.try_all())
