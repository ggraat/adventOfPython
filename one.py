import regex as re

from common.util import read_line


class One:
    def __init__(self, filename):
        self.filename = filename

    def read_calibration(self, allow_words=False):
        total = 0
        for line in read_line(self.filename):
            if allow_words:
                digit_list = list(map(lambda word: One.get_digit(word),
                                      re.findall(r'(one|two|three|four|five|six|seven|eight|nine|\d)', line,
                                                 overlapped=True)))
            else:
                digit_list = [char for char in line if char.isdigit()]
            value = int(digit_list[0] + digit_list[-1])
            total += value
        return total

    def part_one(self):
        return self.read_calibration()

    def part_two(self):
        return self.read_calibration(True)

    @staticmethod
    def get_digit(string):
        if string.isdigit():
            return string
        match string:
            case 'one':
                return '1'
            case 'two':
                return '2'
            case 'three':
                return '3'
            case 'four':
                return '4'
            case 'five':
                return '5'
            case 'six':
                return '6'
            case 'seven':
                return '7'
            case 'eight':
                return '8'
            case 'nine':
                return '9'
        raise ValueError


if __name__ == '__main__':
    one = One('one')
    print(one.part_one())
    print(one.part_two())
