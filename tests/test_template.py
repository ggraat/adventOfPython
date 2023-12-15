from unittest import TestCase


class TestDay(TestCase):

    _data = '''data'''.splitlines()

    def setUp(self):
        self.puzzle = Day(self._data)

    def test_part_one(self):
        self.assertEqual(-1, self.puzzle.part_one())

    def test_part_two(self):
        self.assertEqual(-1, self.puzzle.part_two())
