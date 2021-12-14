import unittest
from day_08 import solve

class TestSamples(unittest.TestCase):
    def test_samples_part_1(self):
        data = r"""
""
"abc"
"aaa\"aaa"
"\x27"
"""
        p1, p2 = solve(data)
        self.assertEqual(p1, str(12))
        self.assertEqual(p2, str(19))
