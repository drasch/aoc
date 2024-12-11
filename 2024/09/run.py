class Disk:
    disk_blocks: list[int | None]

    def __init__(self, fn) -> None:
        self.disk_blocks = []
        with open(fn, "r") as file:
            line = file.read().strip()

        block_id = 0
        for i in range(len(line)):
            val = int(line[i])
            if i % 2 == 0:
                self.disk_blocks += [block_id] * val
                block_id += 1
            else:
                self.disk_blocks += [None] * val

    def move_blocks(self) -> None:
        def block_to_move():
            pos = len(self.disk_blocks) - 1
            while pos >= 0:
                while self.disk_blocks[pos] is None and pos >= 0:
                    pos -= 1
                yield pos

        next_block = block_to_move()
        try:
            for index in range(len(self.disk_blocks)):
                block = self.disk_blocks[index]
                if block is None:
                    pos_to_take = next(next_block)

                    if pos_to_take <= index:
                        break

                    self.disk_blocks[index] = self.disk_blocks[pos_to_take]
                    self.disk_blocks[pos_to_take] = None

        except StopIteration:
            pass

    def checksum(self) -> int:
        sum_total = 0
        for index in range(len(self.disk_blocks)):
            block = self.disk_blocks[index]
            if block is not None:
                sum_total += index * block
        return sum_total


if __name__ == "__main__":
    c = Disk("input.text")
    c.move_blocks()
    print(c.checksum())
    c = Disk("input")
    c.move_blocks()
    print(c.checksum())
