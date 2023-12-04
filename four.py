import re
from pathlib import Path

from common.util import read_line


class Four:
    def __init__(self, filename):
        self.filename = filename

    def part_one(self):
        total = 0
        for line in read_line(self.filename):
            numbers = line.split(':')[1].split('|')
            winning = set(re.findall(r'(\d+)', numbers[0]))
            mine = set(re.findall(r'(\d+)', numbers[1]))
            matches = winning.intersection(mine)
            if len(matches) > 0:
                total += pow(2, len(matches) - 1)
        return total

    def part_two(self):
        pass


if __name__ == '__main__':
    four = Four(Path(__file__).stem)
    print(four.part_one())
    print(four.part_two())
