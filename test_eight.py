from pathlib import Path
from unittest import TestCase

from eight import Eight


class TestEight(TestCase):
    def test_part_one(self):
        eight = Eight(Path(__file__).stem)
        self.assertEqual(6, eight.part_one())

    def test_part_two(self):
        eight = Eight(Path(__file__).stem + '_part2')
        self.assertEqual(6, eight.part_two())
