from pathlib import Path

from common.puzzle import Puzzle
from common.util import read_lines


class Day(Puzzle):
    def __init__(self, _data):
        self.data = _data

    def part_one(self):
        pass

    def part_two(self):
        pass


if __name__ == '__main__':
    _data = read_lines(Path(__file__).stem)
    puzzle = Day(_data)
    print(puzzle.part_one())
    print(puzzle.part_two())
