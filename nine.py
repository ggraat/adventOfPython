from pathlib import Path

from common.puzzle import Puzzle
from common.util import read_line


class Observation:
    def __init__(self, line):
        self.current = list(map(lambda v: int(v), line.split(' ')))
        self.sequences = []

    def is_ready(self):
        return self.current.count(0) == len(self.current)

    def predict(self):
        self.find_sequences()
        total = 0
        for seq in self.sequences[::-1]:
            total += seq[-1]
        # print(total)
        # self.print_sequence()
        return total

    def backtrack(self):
        self.find_sequences()
        value = 0
        for seq in self.sequences[::-1]:
            value = seq[0] - value
        # print(total)
        # self.print_sequence()
        return value

    def find_sequences(self):
        while not self.is_ready():
            self.sequences.append(self.current)
            next_seq = []
            for a, b in zip(self.current[:-1], self.current[1:]):
                next_seq.append(b - a)
            self.current = next_seq

    def print_sequence(self):
        for s in self.sequences:
            print(s)
        print('\n')


class Nine(Puzzle):
    def __init__(self, filename):
        self.filename = filename

    def part_one(self):
        total = 0
        for line in read_line(self.filename):
            obs = Observation(line)
            predict = obs.predict()
            total += predict
        return total

    def part_two(self):
        total = 0
        for line in read_line(self.filename):
            obs = Observation(line)
            predict = obs.backtrack()
            total += predict
        return total


if __name__ == '__main__':
    nine = Nine(Path(__file__).stem)
    print(nine.part_one())
    print(nine.part_two())
