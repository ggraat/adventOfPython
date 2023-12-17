from unittest import TestCase

from seventeen import Seventeen


class TestSeventeen(TestCase):
    _data = '''2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533'''.splitlines()

    def setUp(self):
        self.puzzle = Seventeen(self._data)

    def test_part_one(self):
        self.assertEqual(102, self.puzzle.part_one())

    def test_part_two(self):
        self.assertEqual(94, self.puzzle.part_two())

    def test_simple(self):
        _data = '''111111111111
999999999991
999999999991
999999999991
999999999991'''.splitlines()
        simple = Seventeen(_data)
        self.assertEqual(71, simple.part_two())