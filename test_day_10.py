import unittest
from day_10 import _solve

class TestSamples(unittest.TestCase):
    def test_samples_part_1(self):
        for data, exp in [("1", "11"), ("11", "21"), ("21", "1211"), ("1211", "111221"), ("111221", "312211")]:
            s = _solve(data, 1)
            self.assertEqual(s, exp)
