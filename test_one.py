from pathlib import Path
from unittest import TestCase

from one import One


class TestOne(TestCase):

    def setUp(self):
        self.one = One(Path(__file__).stem)

    def test_part_one(self):
        self.assertEqual(142, self.one.part_one())

    def test_part_two(self):
        self.one = One(Path(__file__).stem + '_part2')
        self.assertEqual(281, self.one.part_two())
