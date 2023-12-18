import re
from operator import itemgetter
from pathlib import Path

from common.puzzle import Puzzle
from common.util import read_lines


class Eighteen(Puzzle):
    def __init__(self, _data):
        self.directions = []
        for line in _data:
            split = line.split()
            self.directions.append((split[0], int(split[1])))
        self.marked = []

    def part_one(self):
        self.draw_map()
        map = self.fill_map()
        total = 0
        for line in map:
            total += line.count('#')
        return total

    def part_two(self):
        pass

    def draw_map(self):
        RIGHT = 'R'
        DOWN = 'D'
        LEFT = 'L'
        UP = "U"
        current = (0, 0)
        for direction, steps in self.directions:
            if direction == RIGHT:
                next = (current[0] + steps, current[1])
                for n in range(current[0], next[0]):
                    self.marked.append((n, current[1]))
            if direction == DOWN:
                next = (current[0], current[1] + steps)
                for n in range(current[1], next[1]):
                    self.marked.append((current[0], n))
            if direction == LEFT:
                next = (current[0] - steps, current[1])
                for n in range(current[0], next[0], -1):
                    self.marked.append((n, current[1]))
            if direction == UP:
                next = (current[0], current[1] - steps)
                for n in range(current[1], next[1], -1):
                    self.marked.append((current[0], n))
            current = next

    def create_trench(self):
        min_x = min(self.marked, key=itemgetter(0))[0]
        max_x = max(self.marked, key=itemgetter(0))[0]
        min_y = min(self.marked, key=itemgetter(1))[1]
        max_y = max(self.marked, key=itemgetter(1))[1]
        map = []
        for y in range(min_y, max_y + 1):
            row = ''
            for x in range(min_x, max_x + 1):
                if (x, y) in self.marked:
                    row += '#'
                else:
                    row += '.'
            map.append(row)
            print(row)
        print()
        return map

    def fill_map(self):
        trench_map = self.create_trench()
        chars = [[c for c in line] for line in trench_map]
        start = (chars[0].index('#') + 1, 1)
        to_visit = {start}
        visited = set()
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while len(to_visit) > 0:
            current = to_visit.pop()
            visited.add(current)
            if chars[current[1]][current[0]] == '#':
                continue
            else:
                chars[current[1]][current[0]] = '@'
                for d in dirs:
                    d_x = current[0] + d[0]
                    d_y = current[1] + d[1]
                    if 0 <= d_x < len(chars[0]) and 0 <= d_y < len(chars) and (d_x, d_y) not in visited:
                        to_visit.add((d_x, d_y))
        lines = []
        for line in chars:
            new_line = ''.join(line).replace('@', '#')
            print(new_line)
            lines.append(new_line)
        print()
        return lines


if __name__ == '__main__':
    _data = read_lines(Path(__file__).stem)
    puzzle = Eighteen(_data)
    print(puzzle.part_one())
    print(puzzle.part_two())
