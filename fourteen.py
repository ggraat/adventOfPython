import copy
from pathlib import Path

from common.puzzle import Puzzle
from common.util import read_lines


class Fourteen(Puzzle):
    def __init__(self, _data):
        self.data = _data

    def part_one(self):
        total = 0
        cols = list(zip(*self.data))
        for col in cols:
            blocks = [n for n, c in enumerate(col) if c == '#']
            if len(blocks) == 0:
                total += self.get_rock_score(col, 0, len(col))
            else:
                start = 0
                for block in blocks:
                    total += self.get_rock_score(col, start, block)
                    start = block + 1
                total += self.get_rock_score(col, start, len(col))
        return total

    def get_rock_score(self, col, start, end):
        if start >= len(col):
            return 0
        total = 0
        rocks = col[start:end].count('O')
        for n in range(rocks):
            total += len(col) - (start + n)
        return total

    def part_two(self):
        dish = [list(line) for line in self.data]
        original_dish = copy.deepcopy(dish)
        cycles = 1000
        for i in range(cycles):
            self.tilt_north(dish)
            self.tilt_west(dish)
            self.tilt_south(dish)
            self.tilt_east(dish)
            if dish == original_dish:
                print(f'copy found at {i}!')
        return self.get_load(dish)

    def tilt_north(self, dish):
        for col in range(len(dish[0])):
            free_space = []
            for i in range(len(dish)):
                char = dish[i][col]
                if char == '.':
                    free_space.append(i)
                elif char == '#':
                    free_space = []
                else:
                    if len(free_space) > 0:
                        dish[free_space.pop(0)][col] = 'O'
                        dish[i][col] = '.'
                        free_space.append(i)

    def tilt_south(self, dish):
        for col in range(len(dish[0])):
            free_space = []
            for i in range(len(dish) - 1, -1, -1):
                char = dish[i][col]
                if char == '.':
                    free_space.append(i)
                elif char == '#':
                    free_space = []
                else:
                    if len(free_space) > 0:
                        dish[free_space.pop(0)][col] = 'O'
                        dish[i][col] = '.'
                        free_space.append(i)

    def tilt_west(self, dish):
        for row in dish:
            free_space = []
            for i, char in enumerate(row):
                if char == '.':
                    free_space.append(i)
                elif char == '#':
                    free_space = []
                else:
                    if len(free_space) > 0:
                        row[free_space.pop(0)] = 'O'
                        row[i] = '.'
                        free_space.append(i)

    def tilt_east(self, dish):
        for row in dish:
            free_space = []
            for i in range(len(row) - 1, -1, -1):
                char = row[i]
                if char == '.':
                    free_space.append(i)
                elif char == '#':
                    free_space = []
                else:
                    if len(free_space) > 0:
                        row[free_space.pop(0)] = 'O'
                        row[i] = '.'
                        free_space.append(i)

    def get_load(self, dish):
        total = 0
        for n, row in enumerate(dish):
            total += (len(dish) - n) * row.count('O')
        return total


if __name__ == '__main__':
    _data = read_lines(Path(__file__).stem)
    puzzle = Fourteen(_data)
    print(puzzle.part_one())
    print(puzzle.part_two())
