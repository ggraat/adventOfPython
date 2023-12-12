import re
from functools import reduce
from pathlib import Path

from common.puzzle import Puzzle
from common.util import read_lines


class Twelve(Puzzle):
    def __init__(self, _data):
        self.data = _data

    def part_one(self):
        total = 0
        for line in self.data:
            split = line.split()
            record = split[0]
            groups = [*map(int, split[1].split(','))]
            num_springs = reduce(lambda x, y: x + y, groups)
            known_springs = line.count('#')
            possible = [index for index, char in enumerate(record) if char == '?']
            configs = self.generate_configs(record, num_springs - known_springs, possible)
            valid = self.count_valid_configs(configs, groups)
            total += valid
        return total

    def part_two(self):
        pass
    def generate_configs(self, record, candidates, possible):
        chars = [char for char in record]
        configs = []
        self.recurse(possible, candidates, chars, configs)
        return configs

    def recurse(self, possible, candidates, chars, configs):
        if candidates == 1:
            if len(possible) == 1:
                c = chars.copy()
                c[possible[0]] = '#'
                configs.append(''.join(c).replace('?', '.'))
            else:
                for pos in possible:
                    self.recurse([pos], candidates, chars, configs)
        else:
            for n in range(len(possible) - candidates + 1):
                c = chars.copy()
                c[possible[n]] = '#'
                self.recurse(possible[n + 1:], candidates - 1, c, configs)

    def count_valid_configs(self, configs, groups):
        matches = []
        total = 0
        for group in groups:
            matches.append('(#{' + str(group) + '})')
        pattern = r'^\.*' + r'\.+'.join(matches) + r'\.*$'
        for config in configs:
            if re.match(pattern, config):
                total += 1
        return total


if __name__ == '__main__':
    _data = read_lines(Path(__file__).stem)
    twelve = Twelve(_data)
    print(twelve.part_one())
    print(twelve.part_two())
