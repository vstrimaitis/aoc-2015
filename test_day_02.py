import unittest
from day_02 import solve

class TestSamples(unittest.TestCase):
    def test_samples(self):
        for data, (exp1, exp2) in [("2x3x4", (58, 34)), ("1x1x10", (43, 14))]:
            p1, p2 = solve(data)
            self.assertEqual(p1, str(exp1))
            self.assertEqual(p2, str(exp2))
