from unittest import TestCase

from twentyone import TwentyOne


class TestTwentyOne(TestCase):
    _data = '''...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........'''.splitlines()

    def setUp(self):
        self.puzzle = TwentyOne(self._data, 6)

    def test_part_one(self):
        self.assertEqual(16, self.puzzle.part_one())

    def test_part_two(self):
        self.assertEqual(-1, self.puzzle.part_two())
