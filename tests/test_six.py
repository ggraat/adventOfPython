from pathlib import Path
from unittest import TestCase

from six import Six


class TestSix(TestCase):
    def setUp(self):
        self.six = Six(Path(__file__).stem)

    def test_part_one(self):
        self.assertEqual(288, self.six.part_one())

    def test_part_two(self):
        self.assertEqual(71503, self.six.part_two())
