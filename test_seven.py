from pathlib import Path
from unittest import TestCase

from seven import Seven


class TestSix(TestCase):
    def setUp(self):
        self.seven = Seven(Path(__file__).stem)

    def test_part_one(self):
        self.assertEqual(6440, self.seven.part_one())

    def test_part_two(self):
        self.assertEqual(5905, self.seven.part_two())
