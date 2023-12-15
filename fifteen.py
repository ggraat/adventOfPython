from pathlib import Path

from common.puzzle import Puzzle
from common.util import read_lines


class Fifteen(Puzzle):
    def __init__(self, _data):
        self.data = _data

    def part_one(self):
        steps = self.data.split(',')
        total = 0
        for step in steps:
            total += self.hash_it(step)
        return total

    def part_two(self):
        pass

    @staticmethod
    def hash_it(step):
        cur = 0
        for c in step:
            cur += ord(c)
            cur *= 17
            cur = cur % 256
        return cur


if __name__ == '__main__':
    _data = read_lines(Path(__file__).stem)[0]
    puzzle = Fifteen(_data)
    print(puzzle.part_one())
    print(puzzle.part_two())
