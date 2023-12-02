from pathlib import Path

import regex as re

from common.util import read_line


class Two:
    def __init__(self, filename):
        self.filename = filename

    def part_one(self):
        return self.determine_possible()

    def determine_possible(self):
        total = 0
        for line in read_line(self.filename):
            if Two.get_max(line, 'red') <= 12 and Two.get_max(line, 'green') <= 13 and Two.get_max(line, 'blue') <= 14:
                game_id = int(re.match(r'Game\s(\d+):', line).group(1))
                total += game_id
        return total

    def determine_fewest(self):
        total = 0
        for line in read_line(self.filename):
            total += Two.get_max(line, 'red') * Two.get_max(line, 'green') * Two.get_max(line, 'blue')
        return total

    def part_two(self):
        return self.determine_fewest()

    @staticmethod
    def get_max(line, value):
        values = list(map(lambda v: int(v), re.findall(r'(\d+)\s' + value, line)))
        return max(values)


if __name__ == '__main__':
    two = Two(Path(__file__).stem)
    print(two.part_one())
    print(two.part_two())
