from unittest import TestCase

from twentytwo import TwentyTwo


class TestTwentyTwo(TestCase):
    _data = '''1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9'''.splitlines()

    def setUp(self):
        self.puzzle = TwentyTwo(self._data)

    def test_part_one(self):
        self.assertEqual(5, self.puzzle.part_one())

    def test_part_two(self):
        self.assertEqual(7, self.puzzle.part_two())
