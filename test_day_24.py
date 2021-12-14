import unittest
from day_24 import solve

class TestSamples(unittest.TestCase):
    def test_sample(self):
        p1, p2 = solve("""1
2
3
4
5
7
8
9
10
11""")
        self.assertEqual(p1, "99")
        self.assertEqual(p2, "44")
