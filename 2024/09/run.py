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

    def move_blocks2(self) -> None:
        def block_to_move():
            pos = len(self.disk_blocks) - 1
            while pos >= 0:
                while self.disk_blocks[pos] is None and pos >= 0:
                    pos -= 1
                end = pos
                while self.disk_blocks[pos] == self.disk_blocks[end] and pos >= 0:
                    pos -= 1
                start = pos + 1
                if pos < 0:
                    return
                yield start, end + 1

        def space():
            pos = 0
            while pos < len(self.disk_blocks):
                while pos < len(self.disk_blocks) and self.disk_blocks[pos] is not None:
                    pos += 1
                start = pos
                while pos < len(self.disk_blocks) and self.disk_blocks[pos] is None:
                    pos += 1
                end = pos
                if pos >= len(self.disk_blocks):
                    return
                yield start, end

        for block_start, block_end in block_to_move():
            for space_start, space_end in space():
                if space_end > block_start:
                    break
                if space_end - space_start >= block_end - block_start:
                    for i in range(block_end - block_start):
                        self.disk_blocks[space_start + i] = self.disk_blocks[
                            block_start + i
                        ]
                        self.disk_blocks[block_start + i] = None
                    break
            # print("".join([str(b) if b is not None else "." for b in self.disk_blocks]))

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

    c = Disk("input.text")
    c.move_blocks2()
    print(c.checksum())
    c = Disk("input")
    c.move_blocks2()
    print(c.checksum())
