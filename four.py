import re
from pathlib import Path

from common.util import read_line


class Card:
    def __init__(self, num, winning, mine, original=True):
        self.num = num
        self.winning = winning
        self.mine = mine
        self.original = original

    def duplicate(self):
        return Card(self.num, self.winning, self.mine, original=False)

    def get_score(self):
        matches = self.winning.intersection(self.mine)
        return len(matches)


class Game:
    def __init__(self):
        self.cards = {}

    def add_card(self, card):
        self.cards[int(card.num)] = [card]

    def play(self, num):
        num_cards = self.cards.get(num)
        score = num_cards[0].get_score()
        if score > 0:
            total_num = len(num_cards)
            for i in range(num + 1, num + 1 + score):
                self.copy_cards(i, total_num)

    def copy_cards(self, num, total_num):
        if num not in self.cards.keys():
            return
        num_cards = self.cards.get(num)
        for i in range(total_num):
            num_cards.append(num_cards[0].duplicate())

    def get_total(self):
        return sum(map(lambda v: len(v), self.cards.values()))

class Four:
    def __init__(self, filename):
        self.filename = filename

    def part_one(self):
        total = 0
        for line in read_line(self.filename):
            numbers = line.split(':')[1].split('|')
            winning = set(re.findall(r'(\d+)', numbers[0]))
            mine = set(re.findall(r'(\d+)', numbers[1]))
            matches = winning.intersection(mine)
            if len(matches) > 0:
                total += pow(2, len(matches) - 1)
        return total

    def part_two(self):
        game = Game()
        for line in read_line(self.filename):
            card_num = re.match(r'Card\s+(\d+):', line).group(1)
            numbers = line.split(':')[1].split('|')
            winning = set(re.findall(r'(\d+)', numbers[0]))
            mine = set(re.findall(r'(\d+)', numbers[1]))
            card = Card(card_num, winning, mine)
            game.add_card(card)
        for num in range(1, len(game.cards) + 1):
            game.play(num)
        return game.get_total()

if __name__ == '__main__':
    four = Four(Path(__file__).stem)
    print(four.part_one())
    print(four.part_two())
