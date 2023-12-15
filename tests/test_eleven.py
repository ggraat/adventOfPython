from unittest import TestCase

from eleven import Eleven


class TestEleven(TestCase):
    _data = '''...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....'''.splitlines()

    def test_part_one(self):
        eleven = Eleven(self._data)
        self.assertEqual(374, eleven.part_one())

    def test_part_two(self):
        eleven = Eleven(self._data)
        self.assertEqual(1030, eleven.find_short_paths(10))
