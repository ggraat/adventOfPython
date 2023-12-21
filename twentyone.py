from pathlib import Path

from common.puzzle import Puzzle
from common.util import read_lines


class TwentyOne(Puzzle):
    def __init__(self, _data):
        self.plots = [[char for char in line] for line in _data]
        self.size = len(self.plots)
        self.start = None
        for y, line in enumerate(self.plots):
            if line.count('S') == 1:
                self.start = (line.index('S'), y)

    def part_one(self):
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        reach = set()
        reach.add(self.start)
        for s in range(64):
            next = set()
            while len(reach) > 0:
                i, j = reach.pop()
                for d in dirs:
                    x, y = i + d[0], j + d[1]
                    if 0 <= x < self.size and 0 <= y < self.size:
                        if self.plots[y][x] != '#' and (x, y) not in next:
                            next.add((x, y))
            reach = next
        return len(next)

    def part_two(self):
        # find the first 3 points to compute the quadratic fit function using Wolfram Alpha
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        reach = set()
        reach.add(self.start)
        for s in range(1, 400):
            next = set()
            while len(reach) > 0:
                i, j = reach.pop()
                for d in dirs:
                    x, y = i + d[0], j + d[1]
                    if self.plots[y % self.size][x % self.size] != '#':
                        next.add((x, y))
            reach = next
            if s % self.size == self.size // 2:
                print(f'{s} -> {len(next)}')
        return self.quadratic_fit(26501365 // self.size)

    def quadratic_fit(self, n):
        a0 = 3849
        a1 = 34331
        a2 = 95175

        b0 = a0
        b1 = a1 - a0
        b2 = a2 - a1
        return b0 + b1 * n + (n * (n - 1) // 2) * (b2 - b1)


if __name__ == '__main__':
    _data = read_lines(Path(__file__).stem)
    puzzle = TwentyOne(_data)
    print(puzzle.part_one())
    print(puzzle.part_two())
