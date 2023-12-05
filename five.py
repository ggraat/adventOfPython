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

    def get_source(self, x):
        for r in self.ranges:
            if r.is_in_destination(x):
                return r.get_source(x)
        return x


class Range:
    def __init__(self, destination, source, length):
        self.destination = destination
        self.source = source
        self.length = length

    def is_in_range(self, x):
        return self.source <= x < self.source + self.length

    def is_in_destination(self, x):
        return self.destination <= x < self.destination + self.length

    def get_destination(self, x):
        return self.destination + (x - self.source)

    def get_source(self, x):
        return self.source + (x - self.destination)


class Five(Puzzle):
    def __init__(self, filename):
        self.filename = filename
        self.seeds = []
        self.maps = []
        self.read_map()

    def part_one(self):
        locations = list(map(lambda s: self.follow_map(s), self.seeds))
        return min(locations)

    def part_two(self):
        ranges = []
        maximum = 0
        for start, length in zip(self.seeds[::2], self.seeds[1::2]):
            ranges.append(range(start, start + length))
            if start + length > maximum:
                maximum = start + length
        for location in range(maximum):
            seed = self.reverse_map(location)
            for r in ranges:
                if seed in r:
                    return location

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

    def reverse_map(self, n):
        for m in self.maps[::-1]:
            n = m.get_source(n)
        return n


if __name__ == '__main__':
    five = Five(Path(__file__).stem)
    print(five.part_one())
    print(five.part_two())
