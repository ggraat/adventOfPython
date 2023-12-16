from pathlib import Path

from common.puzzle import Puzzle
from common.util import read_lines


class Spot:
    def __init__(self, char):
        self.char = char
        self.marks = []

    def add_mark(self, direction):
        self.marks.append(direction)

    def is_marked(self, direction):
        return direction in self.marks

    def is_energized(self):
        return len(self.marks) > 0

    def __eq__(self, other):
        return self.char == other.char

    def __hash__(self):
        return hash(self.char)

    def __repr__(self):
        return self.char


class Grid:
    EMPTY = Spot('.')
    MIRROR_LEFT = Spot('\\')
    MIRROR_RIGHT = Spot('/')
    SPLIT_HORIZONTAL = Spot('-')
    SPLIT_VERTICAL = Spot('|')

    DIRECTION_UP = '^'
    DIRECTION_DOWN = 'v'
    DIRECTION_LEFT = '<'
    DIRECTION_RIGHT = '>'

    def __init__(self, _data):
        self.grid = [[Spot(char) for char in line] for line in _data]
        self.todo = [(0, 0, self.DIRECTION_RIGHT)]

    def move(self):
        while len(self.todo) > 0:
            x, y, direction = self.todo.pop(0)
            spot = self.grid[y][x]
            if spot.is_marked(direction):
                continue
            spot.add_mark(direction)

            directions = self.get_next_direction(direction, self.grid[y][x])
            for d in directions:
                if d == self.DIRECTION_RIGHT:
                    if x == len(self.grid[0]) - 1:
                        continue
                    x += 1
                elif d == self.DIRECTION_LEFT:
                    if x == 0:
                        continue
                    x -= 1
                elif d == self.DIRECTION_UP:
                    if y == 0:
                        continue
                    y -= 1
                elif d == self.DIRECTION_DOWN:
                    if y == len(self.grid) - 1:
                        continue
                    y += 1

                self.todo.append((x, y, d))

    def get_next_direction(self, direction, next_spot):
        if next_spot == self.EMPTY:
            return direction
        if next_spot == self.SPLIT_HORIZONTAL:
            if self.is_horizontal(direction):
                return direction
            return [self.DIRECTION_LEFT, self.DIRECTION_RIGHT]
        if next_spot == self.SPLIT_VERTICAL:
            if self.is_vertical(direction):
                return direction
            return [self.DIRECTION_DOWN, self.DIRECTION_UP]
        if next_spot == self.MIRROR_LEFT:
            if direction == self.DIRECTION_DOWN:
                return self.DIRECTION_RIGHT
            if direction == self.DIRECTION_LEFT:
                return self.DIRECTION_UP
            if direction == self.DIRECTION_UP:
                return self.DIRECTION_LEFT
            if direction == self.DIRECTION_RIGHT:
                return self.DIRECTION_DOWN
        if next_spot == self.MIRROR_RIGHT:
            if direction == self.DIRECTION_DOWN:
                return self.DIRECTION_LEFT
            if direction == self.DIRECTION_LEFT:
                return self.DIRECTION_DOWN
            if direction == self.DIRECTION_UP:
                return self.DIRECTION_RIGHT
            if direction == self.DIRECTION_RIGHT:
                return self.DIRECTION_UP

    def count_energized(self):
        total = 0
        for row in self.grid:
            for spot in row:
                total += spot.is_energized()
        return total

    def print_energized(self):
        for row in self.grid:
            line = ''
            for spot in row:
                if spot.is_energized():
                    line += '#'
                else:
                    line += '.'
            print(line)

    def is_horizontal(self, direction):
        return direction == self.DIRECTION_RIGHT or direction == self.DIRECTION_LEFT

    def is_vertical(self, direction):
        return direction == self.DIRECTION_UP or direction == self.DIRECTION_DOWN


class Sixteen(Puzzle):
    def __init__(self, _data):
        self.data = _data

    def part_one(self):
        grid = Grid(self.data)
        grid.move()
        grid.print_energized()
        return grid.count_energized()

    def part_two(self):
        pass


if __name__ == '__main__':
    _data = read_lines(Path(__file__).stem)
    puzzle = Sixteen(_data)
    print(puzzle.part_one())
    print(puzzle.part_two())
