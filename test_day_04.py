import unittest
from day_04 import solve

class TestSamples(unittest.TestCase):
    def test_samples_part_1(self):
        for data, exp in [("abcdef", 609043), ("pqrstuv", 1048970)]:
            p1, _ = solve(data)
            self.assertEqual(p1, str(exp))
