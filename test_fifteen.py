from unittest import TestCase

from fifteen import Fifteen


class TestFifteen(TestCase):
    def setUp(self):
        self.fifteen = Fifteen('rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7')

    def test_part_one(self):
        self.assertEqual(1320, self.fifteen.part_one())

    def test_part_two(self):
        self.assertEqual(145, self.fifteen.part_two())
