from unittest import TestCase

from fourteen import Fourteen


class TestFourteen(TestCase):
    _data = '''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....'''.splitlines()

    def setUp(self):
        self.fourteen = Fourteen(self._data)

    def test_part_one(self):
        self.assertEqual(136, self.fourteen.part_one())

    def test_part_two(self):
        self.assertEqual(400, self.fourteen.part_two())
