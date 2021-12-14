import unittest
from day_01 import solve

class TestSamples(unittest.TestCase):
    def test_samples_part_1(self):
        for data, expected in [("(())", 0), ("()()", 0), ("(((", 3), ("(()(()(", 3), ("))(((((", 3), ("())", -1), ("))(", -1), (")))", -3), (")())())", -3)]:
            x, _ = solve(data)
            self.assertEqual(x, str(expected))
            
    def test_samples_part_2(self):
        for data, expected in [(")", 1), ("()())", 5)]:
            _, x = solve(data)
            self.assertEqual(x, str(expected))