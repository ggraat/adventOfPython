from pathlib import Path

from common.puzzle import Puzzle
from common.util import read_lines


class TwentyOne(Puzzle):
    def __init__(self, _data, steps):
        self.data = _data
        self.steps = steps

    def part_one(self):
        plots = [[char for char in line] for line in self.data]
        for y, line in enumerate(plots):
            if line.count('S') == 1:
                start = (line.index('S'), y)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        reach = [start]
        for s in range(self.steps):
            next = []
            while len(reach) > 0:
                current = reach.pop(0)
                for d in dirs:
                    x, y = current[0] + d[0], current[1] + d[1]
                    if 0 <= x < len(self.data[0]) and 0 <= y < len(self.data):
                        if plots[y][x] != '#' and (x,y) not in next:
                            next.append((x,y))
            reach = next
        return len(next)


    def part_two(self):
        pass


if __name__ == '__main__':
    _data = read_lines(Path(__file__).stem)
    puzzle = TwentyOne(_data, 64)
    print(puzzle.part_one())
    print(puzzle.part_two())
