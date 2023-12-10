from pathlib import Path

from common.puzzle import Puzzle
from common.util import read_lines


class Position:
    def __init__(self, x, y, direction=None):
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

    def part_two(self):
        start = self.get_start()

        current = self.start_pos(start)
        loop = {start, *current}
        while len(set(current)) != 1:
            next = []
            for pos in current:
                next.append(self.get_next_pos(pos))
            current = next
            loop.update(next)

        grid = self.create_grid(loop)
        self.widen_grid(grid)
        self.flood_it(grid)
        total = 0
        for row in grid:
            total += row.count('I')
        for row in grid:
            print(''.join(row))
        return total

    def create_grid(self, loop):
        grid = []
        for y, row in enumerate(self.data):
            grid.append([])
            for x, col in enumerate(row):
                if Position(x, y) in loop:
                    grid[y].insert(x, self.data[y][x])
                else:
                    grid[y].insert(x, 'I')
        return grid

    def get_start(self):
        for n in range(len(self.data)):
            if 'S' in self.data[n]:
                return Position(self.data[n].index('S'), n, None)

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

    def widen_grid(self, grid):
        for row in grid:
            for x, (a, b) in enumerate(zip(row, row[1:])):
                if self.squeeze_vertical(a, b):
                    self.add_col(grid, x)
        for x in range(len(grid[0])):
            col = [row[x] for row in grid]
            for y, (a, b) in enumerate(zip(col, col[1:])):
                if self.squeeze_horizontal(a, b):
                    self.add_row(grid, y)

    def squeeze_vertical(self, left, right):
        return left in ['7', '|', 'J', 'S'] and right in ['F', '|', 'L', 'S']

    def squeeze_horizontal(self, up, down):
        return up in ['J', '-', 'L', 'S'] and down in ['F', '-', '7', 'S']

    def add_col(self, grid, index):
        for row in grid:
            if row[index] == 'S' and (row[index + 1] == 'J' or row[index + 1] == '-' or row[index + 1] == '7'):
                row.insert(index + 1, '-')
            elif row[index] == 'F' or row[index] == '-' or row[index] == 'L':
                row.insert(index + 1, '-')
            else:
                row.insert(index + 1, 'x')

    def add_row(self, grid, index):
        new_row = []
        for x, col in enumerate(grid[index]):
            if col == 'S' and (grid[index + 1][x] == 'J' or grid[index + 1][x] == '|' or grid[index + 1][x] == 'L'):
                new_row.append('|')
            elif col == 'F' or col == '|' or col == '7':
                new_row.append('|')
            else:
                new_row.append('x')
        grid.insert(index + 1, new_row)

    def flood_it(self, grid):
        flooded = set()
        for x, col in enumerate(grid[0]):
            if col == 'I' or col == 'x':
                grid[0][x] = 'O'
                flooded.add(Position(x, 0))
        for x, col in enumerate(grid[len(grid) - 1]):
            if col == 'I' or col == 'x':
                grid[len(grid) - 1][x] = 'O'
                flooded.add(Position(x, len(grid) - 1))
        for y, row in enumerate(grid):
            if row[0] == 'I' or row[0] == 'x':
                grid[y][0] = 'O'
                flooded.add(Position(0, y))
            if row[len(row) - 1] == 'I' or row[len(row) - 1] == 'x':
                grid[y][len(row) - 1] = 'O'
                flooded.add(Position(len(row) - 1, y))
        while len(flooded) > 0:
            pos = flooded.pop()
            if self.flood(pos.x, pos.y - 1, grid):
                flooded.add(Position(pos.x, pos.y - 1))
            if self.flood(pos.x + 1, pos.y, grid):
                flooded.add(Position(pos.x + 1, pos.y))
            if self.flood(pos.x, pos.y + 1, grid):
                flooded.add(Position(pos.x, pos.y + 1))
            if self.flood(pos.x - 1, pos.y, grid):
                flooded.add(Position(pos.x - 1, pos.y))

    def flood(self, x, y, grid):
        if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
            return False
        if grid[y][x] == 'I' or grid[y][x] == 'x':
            grid[y][x] = 'O'
            return True
        return False


if __name__ == '__main__':
    data = read_lines(Path(__file__).stem)
    ten = Ten(data)
    print(ten.part_one())
    print(ten.part_two())
