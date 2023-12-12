from unittest import TestCase

from twelve import Twelve


class TestTwelve(TestCase):
    _data = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''.splitlines()

    def setUp(self):
        self.twelve = Twelve(self._data)

    def test_part_one(self):
        self.assertEqual(21, self.twelve.part_one())

    def test_part_two(self):
        self.assertEqual(525152, self.twelve.part_two())
