import re
from functools import reduce
from pathlib import Path

from common.puzzle import Puzzle
from common.util import read_lines


class Six(Puzzle):
    def __init__(self, filename):
        self.filename = filename

    def part_one(self):
        records = self.read_records(self.filename)
        total = 1
        for record in records:
            time = record[0]
            distance = record[1]
            total *= len(list(filter(lambda x: x > distance, self.get_distances(time))))
        return total

    def part_two(self):
        lines = read_lines(self.filename)
        time = int(reduce(lambda a, b: a + b, re.findall(r'(\d+)', lines[0])))
        distance = int(reduce(lambda a, b: a + b, re.findall(r'(\d+)', lines[1])))
        return len(list(filter(lambda x: x > distance, self.get_distances(time))))

    def get_distances(self, time):
        distances = []
        for n in range(time):
            distances.append(self.get_distance(n, time))
        return distances

    def get_distance(self, n, time):
        return (time - n) * n

    def read_records(self, filename):
        lines = read_lines(filename)
        times = list(map(lambda v: int(v), re.findall(r'(\d+)', lines[0])))
        distances = list(map(lambda v: int(v), re.findall(r'(\d+)', lines[1])))
        return zip(times, distances)


if __name__ == '__main__':
    six = Six(Path(__file__).stem)
    print(six.part_one())
    print(six.part_two())
