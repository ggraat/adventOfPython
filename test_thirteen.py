from unittest import TestCase

from thirteen import Thirteen


class TestThirteen(TestCase):
    _data = '''#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#'''.splitlines()

    def setUp(self):
        self.thirteen = Thirteen(self._data)

    def test_part_one(self):
        self.assertEqual(405, self.thirteen.part_one())

    def test_part_two(self):
        self.fail()
