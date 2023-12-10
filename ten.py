from pathlib import Path

from common.puzzle import Puzzle
from common.util import read_lines


class Position:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


class Ten(Puzzle):
    def __init__(self, data):
        self.data = data

    def part_one(self):
        start = self.get_start()

        current = self.start_pos(start)
        distance = 1
        while len(set(current)) != 1:
            next = []
            for pos in current:
                next.append(self.get_next_pos(pos))
            current = next
            distance += 1
        return distance

    def get_start(self):
        for n in range(len(self.data)):
            if 'S' in self.data[n]:
                return Position(self.data[n].index('S'), n, None)

    def part_two(self):
        pass

    def get_next_pos(self, pos):
        if pos.direction == 'U':
            top = self.data[pos.y - 1][pos.x]
            if top == '7':
                return Position(pos.x, pos.y - 1, 'L')
            if top == '|':
                return Position(pos.x, pos.y - 1, 'U')
            if top == 'F':
                return Position(pos.x, pos.y - 1, 'R')
        if pos.direction == 'R':
            right = self.data[pos.y][pos.x + 1]
            if right == 'J':
                return Position(pos.x + 1, pos.y, 'U')
            if right == '-':
                return Position(pos.x + 1, pos.y, 'R')
            if right == '7':
                return Position(pos.x + 1, pos.y, 'D')
        if pos.direction == 'D':
            bottom = self.data[pos.y + 1][pos.x]
            if bottom == 'J':
                return Position(pos.x, pos.y + 1, 'L')
            if bottom == '|':
                return Position(pos.x, pos.y + 1, 'D')
            if bottom == 'L':
                return Position(pos.x, pos.y + 1, 'R')
        if pos.direction == 'L':
            left = self.data[pos.y][pos.x - 1]
            if left == 'L':
                return Position(pos.x - 1, pos.y, 'U')
            if left == '-':
                return Position(pos.x - 1, pos.y, 'L')
            if left == 'F':
                return Position(pos.x - 1, pos.y, 'D')

    def start_pos(self, start):
        start_pos = []
        if start.y != 0:
            start.direction = 'U'
            self.try_pos(start, start_pos)
        if start.x != len(self.data[0]) - 1:
            start.direction = 'R'
            self.try_pos(start, start_pos)
        if start.y != len(self.data) - 1:
            start.direction = 'D'
            self.try_pos(start, start_pos)
        if start.x != 0:
            start.direction = 'L'
            self.try_pos(start, start_pos)
        return start_pos

    def try_pos(self, start, start_pos):
        pos = self.get_next_pos(start)
        if pos is not None:
            start_pos.append(pos)


if __name__ == '__main__':
    data = read_lines(Path(__file__).stem)
    ten = Ten(data)
    print(ten.part_one())
    print(ten.part_two())
