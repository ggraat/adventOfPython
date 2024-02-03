from pathlib import Path
from queue import PriorityQueue

from common.puzzle import Puzzle
from common.util import read_lines


class Map:
    slopes = ['>', 'v', '<', '^']
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def __init__(self, _data, ignore_slopes=False):
        self.map = [[x for x in line] for line in _data]
        self.width, self.height = len(self.map[0]), len(self.map)
        self.ignore_slopes = ignore_slopes

    def get_paths(self):
        todo = PriorityQueue()
        todo.put(((1, 0), set()))

        paths = []

        while not todo.empty():
            current, visited = todo.get()
            visited.add(current)

            # get next
            next = self.get_next(current)
            for n in next:
                if n not in visited:
                    x, y = n
                    if y == self.height - 1:
                        # reached finish
                        paths.append(visited)
                    else:
                        todo.put((n, set(visited)))
        return paths

    def get_next(self, current):
        next = []
        x, y = current
        tile = self.map[y][x]
        if tile in self.slopes and not self.ignore_slopes:
            dx, dy = self.dirs[self.slopes.index(tile)]
            next_x = x + dx
            next_y = y + dy
            if 0 <= next_x < self.width and 0 <= next_y < self.height:
                if self.map[next_y][next_x] != '#':
                    next.append((next_x, next_y))
        else:
            for dir in self.dirs:
                dx, dy = dir
                next_x = x + dx
                next_y = y + dy
                if 0 <= next_x < self.width and 0 <= next_y < self.height:
                    if self.map[next_y][next_x] != '#':
                        next.append((next_x, next_y))
        return next


class TwentyThree(Puzzle):
    def __init__(self, _data):
        self.data = _data

    def part_one(self):
        the_map = Map(self.data)
        paths = the_map.get_paths()
        return max(list(map(lambda s: len(s), paths)))

    def part_two(self):
        the_map = Map(self.data, True)
        paths = the_map.get_paths()
        return max(list(map(lambda s: len(s), paths)))


if __name__ == '__main__':
    _data = read_lines(Path(__file__).stem)
    puzzle = TwentyThree(_data)
    print(puzzle.part_one())
    print(puzzle.part_two())
