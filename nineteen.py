import re
from pathlib import Path

from common.puzzle import Puzzle
from common.util import read_lines


class PossiblePart:
    def __init__(self, min_x, max_x, min_m, max_m, min_a, max_a, min_s, max_s):
        self.part = [(min_x, max_x), (min_m, max_m), (min_a, max_a), (min_s, max_s)]

    def copy_part(self):
        return PossiblePart(self.part[0][0], self.part[0][1], self.part[1][0], self.part[1][1],
                            self.part[2][0], self.part[2][1], self.part[3][0], self.part[3][1])

    def get_configs(self):
        return (self.part[0][1] - self.part[0][0] + 1) * (self.part[1][1] - self.part[1][0] + 1) * (
                self.part[2][1] - self.part[2][0] + 1) * (self.part[3][1] - self.part[3][0] + 1)


class PossibleRule:
    def __init__(self, field, operator, value, result):
        self.field = field
        self.operator = operator
        self.value = value
        self.result = result

    def apply_rule(self, possible: PossiblePart):
        if self.operator == '':
            return self.result
        valid = True
        if self.operator == '<':
            if possible.part[self.field][1] < self.value:
                # in range, nothing happens
                pass
            elif possible.part[self.field][0] < self.value:
                possible.part[self.field] = (possible.part[self.field][0], self.value - 1)
            else:
                # not possible
                valid = False
        else:
            if possible.part[self.field][0] > self.value:
                # in range, nothing happens
                pass
            elif possible.part[self.field][1] > self.value:
                possible.part[self.field] = (self.value + 1, possible.part[self.field][1])
            else:
                # not possible
                valid = False
        if not valid:
            return 'R'
        else:
            return self.result

    def apply_rule_negated(self, possible: PossiblePart):
        if self.operator == '':
            return 'R'
        valid = True
        if self.operator == '<':
            if possible.part[self.field][0] >= self.value:
                # in range, nothing happens
                pass
            elif possible.part[self.field][1] >= self.value:
                possible.part[self.field] = (self.value, possible.part[self.field][1])
            else:
                # not possible
                valid = False
        else:
            if possible.part[self.field][1] <= self.value:
                # in range, nothing happens
                pass
            elif possible.part[self.field][0] <= self.value:
                possible.part[self.field] = (possible.part[self.field][0], self.value)
            else:
                # not possible
                valid = False
        if not valid:
            return 'R'
        else:
            return self.result


class PossibleWorkflow:
    def __init__(self, rules: list[PossibleRule]):
        self.rules = rules


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

    def parse_input_part2(self):
        d = {'x': 0, 'm': 1, 'a': 2, 's': 3}
        for line in self.data:
            if line == '':
                break
            else:
                index = line.index('{')
                name = line[0:index]
                steps = line[index + 1:-1].split(',')
                rules = []
                for step in steps:
                    split = step.split(':')
                    if len(split) == 2:
                        rules.append(PossibleRule(d[split[0][0]], split[0][1], int(split[0][2:]), split[1]))
                    else:
                        rules.append(PossibleRule('', '', '', split[0]))
                self.workflows[name] = PossibleWorkflow(rules)

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
        self.parse_input_part2()
        valid_parts = []
        start = PossiblePart(1, 4000, 1, 4000, 1, 4000, 1, 4000)
        todo = [('in', 0, start)]
        while len(todo) > 0:
            (wf, index, part) = todo.pop()
            if wf not in ['A', 'R']:
                workflow = self.workflows[wf]
                rule = workflow.rules[index]
                part_neg = part.copy_part()
                next = rule.apply_rule(part)
                todo.append((next, 0, part))
                if index < len(workflow.rules) - 1:
                    rule.apply_rule_negated(part_neg)
                    todo.append((wf, index + 1, part_neg))
            if wf == 'A':
                valid_parts.append(part)
        return self.count_valid_configs(valid_parts)

    def count_valid_configs(self, valid_parts):
        total = 0
        for part in valid_parts:
            total += part.get_configs()
        return total


if __name__ == '__main__':
    _data = read_lines(Path(__file__).stem)
    puzzle = Nineteen(_data)
    print(puzzle.part_one())
    print(puzzle.part_two())
