import unittest
from day_17 import _solve

class TestSamples(unittest.TestCase):
    def test_sample_part_1(self):
        containers = [20, 15, 10, 5, 5]
        p1, p2 = _solve(containers, 25)
        self.assertEqual(p1, 4)
        self.assertEqual(p2, 3)
