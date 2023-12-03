from pathlib import Path

import regex as re
from regex import regex

from common.util import read_line, read_lines


class GearSpot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.adjacent = set()

    def add_adjacent(self, candidate):
        self.adjacent.add(candidate)

    def is_valid(self):
        return len(self.adjacent) == 2

    def get_gear(self):
        if self.is_valid():
            return int(self.adjacent.pop().part_num) * int(self.adjacent.pop().part_num)
        return 0


class EnginePartCandidate:
    def __init__(self, part_num, row, col):
        self.part_num = part_num
        self.row = row
        self.col = col
        self.symbol = None

    def set_adjacent_symbol(self, symbol):
        self.symbol = symbol

    def is_valid(self):
        return self.symbol is not None


class Three:
    def __init__(self, filename):
        self.schematic = read_lines(filename)
        self.engine_part_candidates = []
        self.gear_spots = []
        self.read_candidates()
        self.read_gears()

    def part_one(self):
        self.find_adjacent()
        total = 0
        for part in self.engine_part_candidates:
            if part.is_valid():
                total += int(part.part_num)
        return total

    def part_two(self):
        return self.find_gears()

    def read_candidates(self):
        for index in range(len(self.schematic)):
            result = regex.finditer(r'(\d+)', self.schematic[index])
            for match in result:
                candidate = EnginePartCandidate(match.group(0), index, match.start())
                self.engine_part_candidates.append(candidate)

    def read_gears(self):
        for index in range(len(self.schematic)):
            result = regex.finditer(r'(\*)', self.schematic[index])
            for match in result:
                spot = GearSpot(index, match.start())
                self.gear_spots.append(spot)

    def find_adjacent(self):
        for candidate in self.engine_part_candidates:
            adjacent = (self.find_top(candidate)
                        + self.find_left(candidate)
                        + self.find_right(candidate)
                        + self.find_bottom(candidate))
            if adjacent != '':
                candidate.set_adjacent_symbol(adjacent)

    def find_gears(self):
        total = 0
        for spot in self.gear_spots:
            self.get_adjacent_gears(spot)
            total += spot.get_gear()
        return total

    def find_top(self, candidate):
        if candidate.row == 0:
            return ''
        result = ''
        start = self.get_start(candidate)
        end = self.get_end(candidate)
        for char in self.schematic[candidate.row - 1][start:end]:
            result += self.check_spot(char)
        return result

    def get_end(self, candidate):
        return min(len(self.schematic[0]) - 1, candidate.col + len(candidate.part_num) + 1)

    def get_start(self, candidate):
        return max(0, candidate.col - 1)

    def find_left(self, candidate):
        if candidate.col == 0:
            return ''
        return self.check_spot(self.schematic[candidate.row][candidate.col - 1])

    def find_right(self, candidate):
        if candidate.col + len(candidate.part_num) == len(self.schematic[0]):
            return ''
        return self.check_spot(self.schematic[candidate.row][candidate.col + len(candidate.part_num)])

    def find_bottom(self, candidate):
        if candidate.row == len(self.schematic) - 1:
            return ''
        result = ''
        start = self.get_start(candidate)
        end = self.get_end(candidate)
        for char in self.schematic[candidate.row + 1][start:end]:
            result += self.check_spot(char)
        return result

    def check_spot(self, char):
        if char == '.':
            return ''
        return char

    def get_adjacent_gears(self, spot):
        self.add_adjacent_top(spot)
        self.add_adjacent_left(spot)
        self.add_adjacent_right(spot)
        self.add_adjacent_bottom(spot)

    def add_adjacent_top(self, spot):
        if spot.x == 0:
            return
        start = 0 if spot.y == 0 else spot.y - 1
        end = spot.y if spot.y == len(self.schematic[0]) - 1 else spot.y + 1
        for i in range(start, end + 1):
            overlaps = self.overlaps(spot.x - 1, i)
            if overlaps is not None:
                spot.add_adjacent(overlaps)

    def add_adjacent_left(self, spot):
        if spot.y == 0:
            return
        overlaps = self.overlaps(spot.x, spot.y - 1)
        if overlaps is not None:
            spot.add_adjacent(overlaps)

    def add_adjacent_right(self, spot):
        if spot.y == len(self.schematic[0]) - 1:
            return
        overlaps = self.overlaps(spot.x, spot.y + 1)
        if overlaps is not None:
            spot.add_adjacent(overlaps)

    def add_adjacent_bottom(self, spot):
        if spot.x == len(self.schematic) - 1:
            return
        start = 0 if spot.y == 0 else spot.y - 1
        end = spot.y if spot.y == len(self.schematic[0]) - 1 else spot.y + 1
        for i in range(start, end + 1):
            overlaps = self.overlaps(spot.x + 1, i)
            if overlaps is not None:
                spot.add_adjacent(overlaps)

    def overlaps(self, x, y):
        for candidate in self.engine_part_candidates:
            if candidate.row == x:
                if candidate.col <= y < candidate.col + len(candidate.part_num):
                    return candidate
        return None


if __name__ == '__main__':
    three = Three(Path(__file__).stem)
    print(three.part_one())
    print(three.part_two())
