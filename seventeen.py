from pathlib import Path
from queue import PriorityQueue

from common.puzzle import Puzzle
from common.util import read_lines


class Graph:
    def __init__(self, _data):
        self.weights = {}
        for y, row in enumerate(_data):
            for x, weight in enumerate(row):
                node = (x, y)
                self.weights[node] = int(weight)
        self.width = len(_data[0])
        self.height = len(_data)
        self.end = (self.width - 1, self.height - 1)

    def dijkstra(self, min_same_direction, max_same_direction):
        todo = PriorityQueue()
        todo.put((0, (0, 0), 0, 0))
        todo.put((0, (0, 0), 1, 0))
        visited = set()
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while not todo.empty():
            heat, current, direction, same_dir = todo.get()

            if (current, direction, same_dir) in visited:
                continue

            visited.add((current, direction, same_dir))

            if current == self.end and same_dir >= min_same_direction:
                return heat

            x, y = current
            dx, dy = dirs[direction]
            if 0 <= x + dx < self.width and 0 <= y + dy < self.height:
                next = (x + dx, y + dy)
            else:
                continue

            heat += self.weights[next]

            same_dir += 1
            if same_dir < max_same_direction:
                todo.put((heat, next, direction, same_dir))

            if same_dir > min_same_direction - 1:
                todo.put((heat, next, (direction + 1) % 4, 0))
                todo.put((heat, next, (direction - 1) % 4, 0))
        return -1


class Seventeen(Puzzle):
    def __init__(self, _data):
        self.data = _data

    def part_one(self):
        graph = Graph(self.data)
        return graph.dijkstra(0, 3)

    def part_two(self):
        graph = Graph(self.data)
        return graph.dijkstra(4, 10)


if __name__ == '__main__':
    _data = read_lines(Path(__file__).stem)
    puzzle = Seventeen(_data)
    print(puzzle.part_one())
    print(puzzle.part_two())
