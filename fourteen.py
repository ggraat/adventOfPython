from pathlib import Path

from common.puzzle import Puzzle
from common.util import read_lines


class Fourteen(Puzzle):
    def __init__(self, _data):
        self.data = _data

    def part_one(self):
        total = 0
        cols = list(zip(*self.data))
        for col in cols:
            blocks = [n for n, c in enumerate(col) if c == '#']
            if len(blocks) == 0:
                total += self.get_rock_score(col, 0, len(col))
            else:
                start = 0
                for block in blocks:
                    total += self.get_rock_score(col, start, block)
                    start = block + 1
                total += self.get_rock_score(col, start, len(col))
        return total

    def get_rock_score(self, col, start, end):
        if start >= len(col):
            return 0
        total = 0
        rocks = col[start:end].count('O')
        for n in range(rocks):
            total += len(col) - (start + n)
        return total

    def part_two(self):
        pass


if __name__ == '__main__':
    _data = read_lines(Path(__file__).stem)
    puzzle = Fourteen(_data)
    print(puzzle.part_one())
    print(puzzle.part_two())
