from pathlib import Path

from common.puzzle import Puzzle
from common.util import read_lines


class Thirteen(Puzzle):
    def __init__(self, _data):
        self.data = _data

    def part_one(self):
        return self.mirroring()

    def part_two(self):
        return self.detect_mirrors()

    def detect_mirrors(self):
        inputs = self.get_inputs()
        total = 0
        for i in inputs:
            horizontal = self.mirror(i)
            if horizontal == -1:
                transposed = self.transpose(i)
                vertical = self.mirror(transposed)
                total += vertical
            else:
                total += horizontal * 100
        return total

    def mirror(self, lines):
        for n in range(len(lines)):
            if self.mirror_valid(lines, n):
                return n + 1
        return -1

    def mirror_valid(self, lines, candidate):
        difference = 0
        for n in range(candidate + 1):
            if candidate + n + 1 < len(lines):
                difference += self.difference(lines[candidate - n], lines[candidate + n + 1])
                if difference > 1:
                    return False
        return difference == 1

    def mirroring(self, smudged=True):
        inputs = self.get_inputs()
        total = 0
        for input in inputs:
            horizontal = self.detect_mirror(input, smudged=smudged)
            if horizontal == -1:
                transposed = self.transpose(input)
                vertical = self.detect_mirror(transposed, transpose=True, smudged=smudged)
                total += vertical
            else:
                total += horizontal
        return total

    def transpose(self, data):
        return list(zip(*data))

    def detect_mirror(self, lines, transpose=False, smudged=True):
        original_smudged = smudged
        candidates = []
        for n, (a, b) in enumerate(zip(lines, lines[1:])):
            if a == b:
                candidates.append(n)
            elif not smudged and self.difference(a, b) == 1:
                smudged = True
                candidates.append(n)
        for candidate in candidates:
            if self.is_valid(candidate, lines, original_smudged):
                if transpose:
                    return candidate + 1
                else:
                    return (candidate + 1) * 100
        return -1

    def is_valid(self, candidate, lines, smudged=True):
        if not smudged:
            difference = 0
            for n in range(candidate + 1):
                if candidate + n + 1 < len(lines):
                    difference += self.difference(lines[candidate - n], lines[candidate + n + 1])
                    if difference > 1:
                        return False
            return difference == 1
        else:
            for n in range(candidate + 1):
                if candidate + n + 1 < len(lines):
                    if lines[candidate - n] != lines[candidate + n + 1]:
                        if not smudged and self.difference(lines[candidate - n], lines[candidate + n + 1]) == 1:
                            smudged = True
                            continue
                        else:
                            return False
            return True

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

    def difference(self, str1, str2):
        differences = 0
        for a, b in zip([c for c in str1], [c for c in str2]):
            if a != b:
                differences += 1
        return differences


if __name__ == '__main__':
    _data = read_lines(Path(__file__).stem)
    puzzle = Thirteen(_data)
    print(puzzle.part_one())
    print(puzzle.part_two())
