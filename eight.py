import math
import re
from pathlib import Path

from common.puzzle import Puzzle
from common.util import read_lines


class Node:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None

    def add_sub_nodes(self, left, right):
        self.left = left
        self.right = right


class Map:
    def __init__(self, directions, start_node):
        self.directions = directions
        self.start_node = start_node

    def get_next_direction(self, n):
        return self.directions[n % len(self.directions)]

    def navigate(self):
        step = 0
        node = self.start_node
        while not node.label.endswith('Z'):  # != 'ZZZ':
            direction = self.get_next_direction(step)
            if direction == 'L':
                node = node.left
            else:
                node = node.right
            step += 1
        return step


class GhostMap:
    def __init__(self, directions, start_nodes):
        self.directions = directions
        self.maps = []
        for start_node in start_nodes:
            self.maps.append(Map(directions, start_node))

    def get_next_direction(self, n):
        return self.directions[n % len(self.directions)]

    def navigate(self):
        steps = []
        for m in self.maps:
            steps.append(m.navigate())
        return math.lcm(*steps)


class Eight(Puzzle):
    def __init__(self, filename):
        self.nodes = {}
        self.map = self.read_map(filename)

    def part_one(self):
        return self.map.navigate()

    def part_two(self):
        start_nodes = []
        for label in self.nodes.keys():
            if label.endswith('A'):
                start_nodes.append(self.nodes.get(label))
        ghost_map = GhostMap(self.map.directions, start_nodes)
        return ghost_map.navigate()

    def read_map(self, filename):
        lines = read_lines(filename)
        directions = lines[0]
        self.read_nodes(lines[2:])
        return Map(directions, self.nodes.get('AAA'))

    def read_nodes(self, lines):
        for line in lines:
            labels = re.findall(r'([A-Z0-9]+)', line)
            self.nodes[labels[0]] = Node(labels[0])
        for line in lines:
            labels = re.findall(r'([A-Z0-9]+)', line)
            self.nodes.get(labels[0]).add_sub_nodes(self.nodes.get(labels[1]), self.nodes.get(labels[2]))


if __name__ == '__main__':
    eight = Eight(Path(__file__).stem)
    print(eight.part_one())
    print(eight.part_two())
