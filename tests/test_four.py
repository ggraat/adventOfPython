from pathlib import Path
from unittest import TestCase

from four import Four


class test_four(TestCase):
    def setUp(self):
        self.four = Four(Path(__file__).stem)

    def test_part_one(self):
        self.assertEqual(13, self.four.part_one())

    def test_part_two(self):
        self.four = Four(Path(__file__).stem)
        self.assertEqual(30, self.four.part_two())
