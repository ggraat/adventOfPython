from unittest import TestCase

from ten import Ten


class TestTen(TestCase):

    def test_part_one_simple(self):
        data = '''-L|F7
7S-7|
L|7||
-L-J|
L|-JF'''.splitlines()

        ten = Ten(data)
        self.assertEqual(4, ten.part_one())

    def test_part_one_advanced(self):
        data = '''7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ'''.splitlines()
        ten = Ten(data)
        self.assertEqual(8, ten.part_one())

    def test_part_two(self):
        self.fail()
