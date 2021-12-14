import unittest
from day_06 import solve

class TestSamples(unittest.TestCase):
    def test_samples_part_1(self):
        for data, exp in [("turn on 0,0 through 999,999", 1000000), ("toggle 0,0 through 999,0", 1000), ("turn off 499,499 through 500,500", 0)]:
            p1, _ = solve(data)
            self.assertEqual(p1, str(exp))

    def test_samples_part_2(self):
        for data, exp in [("turn on 0,0 through 0,0", 1), ("toggle 0,0 through 999,999", 2000000), ("turn off 0,0 through 999,999", 0)]:
            _, p2 = solve(data)
            self.assertEqual(p2, str(exp))
