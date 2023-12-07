from functools import cmp_to_key
from pathlib import Path

from common.puzzle import Puzzle
from common.util import read_line


class Seven(Puzzle):
    cards = {'A': 14,
             'K': 13,
             'Q': 12,
             'J': 11,
             'T': 10,
             '9': 9,
             '8': 8,
             '7': 7,
             '6': 6,
             '5': 5,
             '4': 4,
             '3': 3,
             '2': 2}

    @staticmethod
    def get_strength(hand: []):
        set_size = len(set(hand))
        match set_size:
            case 1:
                return 500
            case 2:
                count = hand.count(set(hand).pop())
                if count in [1, 4]:
                    return 400
                else:
                    return 350
            case 3:
                counts = list(map(lambda v: hand.count(v), set(hand)))
                if 3 in counts:
                    return 300
                else:
                    return 200
            case 4:
                return 100
            case 5:
                return 50

    @staticmethod
    def compare_cards(a, b):
        for n in range(len(a)):
            card_a = Seven.cards.get(a[n])
            card_b = Seven.cards.get(b[n])
            if card_a > card_b:
                return 1
            elif card_a < card_b:
                return -1

    @staticmethod
    def comparator(a, b):
        strength_a = Seven.get_strength(a)
        strength_b = Seven.get_strength(b)
        if strength_a > strength_b:
            return 1
        elif strength_a < strength_b:
            return -1
        else:
            return Seven.compare_cards(a, b)

    def __init__(self, filename):
        self.filename = filename
        self.bids = {}

    def part_one(self):
        for line in read_line(self.filename):
            split = line.split(' ')
            self.bids[split[0]] = int(split[1])
        ranked = sorted(self.bids.keys(), key=cmp_to_key(Seven.comparator))
        total = 0
        for n in range(len(ranked)):
            total += (n+1) * self.bids.get(ranked[n])
        return total

    def part_two(self):
        pass


if __name__ == '__main__':
    seven = Seven(Path(__file__).stem)
    print(seven.part_one())
    print(seven.part_two())
