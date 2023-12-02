from pathlib import Path
from unittest import TestCase

from two import Two


class TestTwo(TestCase):

    def setUp(self):
        self.two = Two(Path(__file__).stem)

    def test_part_one(self):
        self.assertEqual(8, self.two.part_one())

    def test_part_two(self):
        self.two = Two(Path(__file__).stem)
        self.assertEqual(2286, self.two.part_two())
