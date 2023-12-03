from pathlib import Path
from unittest import TestCase

from three import Three


class TestThree(TestCase):

    def setUp(self):
        self.three = Three(Path(__file__).stem)

    def test_part_one(self):
        self.assertEqual(4361, self.three.part_one())

    def test_part_two(self):
        self.three = Three(Path(__file__).stem)
        self.assertEqual(467835, self.three.part_two())
