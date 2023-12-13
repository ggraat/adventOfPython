from pathlib import Path

from common.puzzle import Puzzle
from common.util import read_lines


class Thirteen(Puzzle):
    def __init__(self, _data):
        self.data = _data

    def part_one(self):
        inputs = self.get_inputs()
        total = 0
        for input in inputs:
            horizontal = self.detect_mirror(input)
            if horizontal == -1:
                transposed = self.transpose(input)
                vertical = self.detect_mirror(transposed, True)
                total += vertical
            else:
                total += horizontal
        return total

    def transpose(self, data):
        return list(zip(*data))

    def detect_mirror(self, lines, transpose=False):
        candidates = []
        for n, (a, b) in enumerate(zip(lines, lines[1:])):
            if a == b:
                candidates.append(n)
        for candidate in candidates:
            if self.is_valid(candidate, lines):
                if transpose:
                    return candidate + 1
                else:
                    return (candidate + 1) * 100
        return -1

    def is_valid(self, candidate, lines):
        for n in range(candidate + 1):
            if candidate + n + 1 < len(lines):
                if lines[candidate - n] != lines[candidate + n + 1]:
                    return False
        return True

    def part_two(self):
        pass

    def get_inputs(self):
        inputs = []
        input = []
        for line in self.data:
            if line == '':
                inputs.append(input)
                input = []
            else:
                input.append(line)
        inputs.append(input)
        return inputs


if __name__ == '__main__':
    _data = read_lines(Path(__file__).stem)
    puzzle = Thirteen(_data)
    print(puzzle.part_one())
    print(puzzle.part_two())
