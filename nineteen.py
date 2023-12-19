import re
from pathlib import Path

from common.puzzle import Puzzle
from common.util import read_lines


class Part:
    def __init__(self, x, m, a, s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s

    def get_rating(self):
        return self.x + self.m + self.a + self.s


class Rule:
    def __init__(self, test, result):
        self.test = test
        self.result = result

    def applies(self, part: Part):
        return self.test(part)

    def __repr__(self):
        return f'Test: {self.test}, Result: {self.result}'


class Workflow:
    def __init__(self, rules: list[Rule]):
        self.rules = rules

    def apply(self, part: Part):
        for rule in self.rules:
            if rule.applies(part):
                return rule.result


class Nineteen(Puzzle):
    def __init__(self, _data):
        self.data = _data
        self.workflows = {}
        self.parts = []

    def parse_input(self):
        parse_parts = False
        for line in self.data:
            if line == '':
                parse_parts = True
                continue
            if parse_parts:
                ints = map(int, re.findall(r'(\d+)', line))
                self.parts.append(Part(*ints))
            else:
                index = line.index('{')
                name = line[0:index]
                steps = line[index + 1:-1].split(',')
                rules = []
                for step in steps:
                    split = step.split(':')
                    if len(split) == 2:
                        rules.append(Rule(eval('lambda part: part.' + split[0]), split[1]))
                    else:
                        rules.append(Rule(lambda part: True, split[0]))
                self.workflows[name] = Workflow(rules)

    def part_one(self):
        self.parse_input()
        total = 0
        for part in self.parts:
            current = 'in'
            while current not in ['A', 'R']:
                current = self.workflows[current].apply(part)
            if current == 'A':
                total += part.get_rating()
        return total

    def part_two(self):
        pass


if __name__ == '__main__':
    _data = read_lines(Path(__file__).stem)
    puzzle = Nineteen(_data)
    print(puzzle.part_one())
    print(puzzle.part_two())
