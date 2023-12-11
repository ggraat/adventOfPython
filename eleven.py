import re
from pathlib import Path

from common.puzzle import Puzzle
from common.util import read_lines


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Eleven(Puzzle):
    def __init__(self, _data):
        self.data = _data

    def part_one(self):
        return self.find_short_paths()

    def find_short_paths(self, expand=2):
        galaxies = []
        empty_rows = []
        for y, row in enumerate(self.data):
            galaxy_index = [x for x, c in enumerate(row) if c == '#']
            if len(galaxy_index) > 0:
                for x in galaxy_index:
                    galaxies.append(Position(x, y))
            else:
                empty_rows.append(y)
        empty_cols = {n for n in range(len(self.data[0]))}.difference(set(map(lambda pos: pos.x, galaxies)))
        for galaxy in galaxies:
            galaxy.x = galaxy.x + (len([x for x in empty_cols if x < galaxy.x]) * (expand-1))
            galaxy.y = galaxy.y + (len([y for y in empty_rows if y < galaxy.y]) * (expand-1))
        total = 0
        for n in range(len(galaxies) - 1):
            for b in galaxies[n + 1:]:
                total += self.get_distance(galaxies[n], b)
        return total

    def part_two(self):
        return self.find_short_paths(1000000)

    def get_distance(self, a, b):
        return abs(a.x - b.x) + abs(a.y - b.y)


if __name__ == '__main__':
    _data = read_lines(Path(__file__).stem)
    eleven = Eleven(_data)
    print(eleven.part_one())
    print(eleven.part_two())
