from pathlib import Path

from common.puzzle import Puzzle
from common.util import read_lines


class Lens:
    def __init__(self, label, focal):
        self.label = label
        self.focal = focal

    def __eq__(self, other):
        return self.label == other.label

    def __hash__(self):
        return hash(self.label)

    def __repr__(self):
        return self.label + ':' + str(self.focal)


class Box:
    def __init__(self):
        self.lenses = []

    def add_lens(self, lens):
        if lens in self.lenses:
            index = self.lenses.index(lens)
            self.lenses[index] = lens
        else:
            self.lenses.append(lens)

    def remove_lens(self, lens):
        if lens in self.lenses:
            self.lenses.remove(lens)

    def get_focus_power(self):
        total = 0
        for n, lens in enumerate(self.lenses):
            total += (n + 1) * lens.focal
        return total

    def __repr__(self):
        return self.lenses.__repr__()


class Configuration:
    def __init__(self):
        self.boxes = {}

    def get_box(self, box_number):
        if box_number in self.boxes:
            return self.boxes[box_number]
        else:
            box = Box()
            self.boxes[box_number] = box
            return box

    def get_focus_power(self):
        total = 0
        for box_number in self.boxes.keys():
            total += (box_number + 1) * self.boxes[box_number].get_focus_power()
        return total

    def __repr__(self):
        return self.boxes.items().__repr__()


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
        configuration = Configuration()
        steps = self.data.split(',')
        for step in steps:
            if step[-1] == '-':
                label = step[:-1]
                box_num = self.hash_it(label)
                configuration.get_box(box_num).remove_lens(Lens(label, 0))
            else:
                split = step.split('=')
                label = split[0]
                focal = int(split[1])
                box_num = self.hash_it(label)
                configuration.get_box(box_num).add_lens(Lens(label, focal))
        return configuration.get_focus_power()

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
