import unittest
from day_03 import solve

class TestSamples(unittest.TestCase):
    def test_samples_part_1(self):
        for data, exp in [(">", 2), ("^>v<", 4), ("^v^v^v^v^v", 2)]:
            p1, _ = solve(data)
            self.assertEqual(p1, str(exp))

    def test_samples_part_2(self):
        for data, exp in [("^v", 3), ("^>v<", 3), ("^v^v^v^v^v", 11)]:
            _, p2 = solve(data)
            self.assertEqual(p2, str(exp))
