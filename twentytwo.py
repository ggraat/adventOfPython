from pathlib import Path
from typing import Tuple, List

from common.puzzle import Puzzle
from common.util import read_lines


class Brick:
    def __init__(self, start: Tuple[int, int, int], end: Tuple[int, int, int]):
        self.supported = set()
        self.supports = set()
        self.start = start
        self.end = end
        self.horizontal = end[2] == start[2]
        self.count_above = 0

    def move_down(self, z):
        if self.horizontal:
            self.start = (self.start[0], self.start[1], z)
            self.end = (self.end[0], self.end[1], z)
        else:
            diff = self.end[2] - self.start[2]
            self.start = (self.start[0], self.start[1], z)
            self.end = (self.end[0], self.end[1], z + diff)

    def set_supported_by(self, others):
        self.supported = others
        for other in others:
            other.supports.add(self)

    def __repr__(self):
        position = 'horizontal' if self.horizontal else 'vertical'
        return f'Brick({self.start}, {self.end}, {position})'


class Tetris:
    def __init__(self, bricks: List[Brick], height):
        self.bricks = bricks
        self.height = height
        self.bricks_copy = {}

    def drop_it(self):
        start = 2  # get bricks at level 2 up to height + 1
        for n in range(start, self.height + 1):
            level = self.get_bricks_at_level(n)
            for brick in level:
                self.move_down(brick)

    def test_disintegrate(self):
        # for each block, examine if it supports other blocks
        # if it does, examine the blocks it supports to see if
        # they are supported by other blocks as well
        total = 0
        for brick in self.bricks:
            if self.can_disintegrate(brick):
                total += 1
        return total

    def can_disintegrate(self, brick):
        return len(brick.supports) == 0 or len(list(filter(lambda b: len(b.supported) == 1, brick.supports))) == 0

    def disintegrate(self):
        total = 0
        # start from the highest block to the ground
        for n in range(self.height, 0, -1):
            level = self.get_bricks_at_level(n)
            for brick in level:
                if not self.can_disintegrate(brick):
                    total += self.count_bricks_above(brick)
        return total

    def count_bricks_above(self, brick):
        total = 0
        above_disintegrate = set()
        above_bricks = set()
        todo = brick.supports
        while len(todo) > 0:
            above = todo.pop()
            if above.count_above > 0:
                above_disintegrate.add(above)
            else:
                above_bricks.add(above)
                todo.update(above.supports)
        for b in above_disintegrate:
            total += b.count_above
        above_total = total + len(above_bricks) + len(above_disintegrate)
        brick.count_above = above_total
        return above_total

    def move_down(self, brick: Brick):
        current_z = brick.end[2]
        below = self.get_bricks_below(current_z)

        under_bricks = set()
        for x in range(brick.start[0], brick.end[0] + 1):
            for y in range(brick.start[1], brick.end[1] + 1):
                under_bricks.update(self.get_bricks_below_point(x, y, below))
        if len(under_bricks) > 0:
            max_depth = max(under_bricks, key=lambda b: b.end[2]).end[2]
            support = list(filter(lambda b: b.end[2] == max_depth, under_bricks))
            brick.set_supported_by(support)
            if max_depth + 1 < current_z:
                brick.move_down(max_depth + 1)
        else:
            # move to ground
            brick.move_down(1)

    def get_bricks_at_level(self, level):
        levels = []
        for brick in self.bricks:
            if brick.start[2] == level:
                levels.append(brick)
        return levels

    def get_bricks_below(self, z):
        below = []
        for brick in self.bricks:
            if brick.horizontal and brick.start[2] < z:
                # horizontal brick below z
                below.append(brick)
            elif not brick.horizontal and brick.end[2] < z:
                # vertical brick entirely below z
                # if not entirely, it does not block another brick on level z
                below.append(brick)
        return below

    def get_bricks_below_point(self, x, y, below):
        bricks = set()
        for brick in below:
            if brick.start[0] <= x <= brick.end[0] and brick.start[1] <= y <= brick.end[1]:
                bricks.add(brick)
        return bricks


class TwentyTwo(Puzzle):
    def __init__(self, _data):
        self.height = 0
        self.bricks = self.parse_bricks(_data)
        self.tetris = Tetris(self.bricks, self.height)
        self.tetris.drop_it()

    def part_one(self):
        return self.tetris.test_disintegrate()

    def part_two(self):
        return self.tetris.disintegrate()

    def parse_bricks(self, _data):
        bricks = []
        for line in _data:
            split = line.split('~')
            x, y, z = map(int, split[0].split(','))
            i, j, k = map(int, split[1].split(','))
            assert x <= i and y <= j and z <= k
            if z > self.height:
                self.height = z
            brick = Brick((x, y, z), (i, j, k))
            bricks.append(brick)
        return bricks


if __name__ == '__main__':
    _data = read_lines(Path(__file__).stem)
    puzzle = TwentyTwo(_data)
    print(puzzle.part_one())
    print(puzzle.part_two())