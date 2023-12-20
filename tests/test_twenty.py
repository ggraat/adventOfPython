from unittest import TestCase

from twenty import Twenty


class TestTwenty(TestCase):

    def test_part_one_simple(self):
        _data = '''broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a'''.splitlines()
        puzzle = Twenty(_data)
        self.assertEqual(32000000, puzzle.part_one())

    def test_part_one_complex(self):
        _data = '''broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output'''.splitlines()
        puzzle = Twenty(_data)
        self.assertEqual(11687500, puzzle.part_one())
