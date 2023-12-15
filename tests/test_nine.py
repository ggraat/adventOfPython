from pathlib import Path
from unittest import TestCase

from nine import Nine


class TestNine(TestCase):
    def setUp(self):
        self.nine = Nine(Path(__file__).stem)

    def test_part_one(self):
        self.assertEqual(114, self.nine.part_one())

    def test_part_two(self):
        self.assertEqual(2, self.nine.part_two())
