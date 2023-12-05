from pathlib import Path

from common.puzzle import Puzzle
from common.util import read_lines


class Map:
    def __init__(self):
        self.ranges = []

    def add_range(self, range):
        self.ranges.append(range)

    def get_destination(self, x):
        for r in self.ranges:
            if r.is_in_range(x):
                return r.get_destination(x)
        return x


class Range:
    def __init__(self, destination, source, length):
        self.destination = destination
        self.source = source
        self.length = length

    def is_in_range(self, x):
        return self.source <= x < self.source + self.length

    def get_destination(self, x):
        return self.destination + (x - self.source)


class Five(Puzzle):
    def __init__(self, filename):
        self.filename = filename
        self.seeds = []
        self.maps = []

    def part_one(self):
        self.read_map()
        locations = list(map(lambda s: self.follow_map(s), self.seeds))
        return min(locations)

    def part_two(self):
        pass

    def read_map(self):
        for line in read_lines(self.filename):
            if line.startswith('seeds:'):
                self.seeds = list(map(lambda v: int(v), line.split(' ')[1:]))
            elif line == '':
                continue
            elif 'map:' in line:
                m = Map()
                self.maps.append(m)
            else:
                numbers = list(map(lambda v: int(v), line.split(' ')))
                r = Range(numbers[0], numbers[1], numbers[2])
                m.add_range(r)

    def follow_map(self, s):
        for m in self.maps:
            s = m.get_destination(s)
        return s


if __name__ == '__main__':
    five = Five(Path(__file__).stem)
    print(five.part_one())
    print(five.part_two())
