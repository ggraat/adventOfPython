from abc import ABC, abstractmethod


class Puzzle(ABC):

    @abstractmethod
    def part_one(self):
        pass

    @abstractmethod
    def part_two(self):
        pass
