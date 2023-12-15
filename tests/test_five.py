from pathlib import Path
from unittest import TestCase

from five import Five


class TestFive(TestCase):

    def setUp(self):
        self.five = Five(Path(__file__).stem)

    def test_part_one(self):
        self.assertEqual(35, self.five.part_one())

    def test_part_two(self):
        self.five = Five(Path(__file__).stem)
        self.assertEqual(46, self.five.part_two())
