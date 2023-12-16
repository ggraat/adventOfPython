from unittest import TestCase

from sixteen import Sixteen


class TestSixteen(TestCase):
    _data = r'''.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....'''.splitlines()

    def setUp(self):
        self.puzzle = Sixteen(self._data)

    def test_part_one(self):
        self.assertEqual(46, self.puzzle.part_one())

    def test_part_two(self):
        self.assertEqual(51, self.puzzle.part_two())
