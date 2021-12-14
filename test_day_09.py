import unittest
from day_09 import solve

class TestSamples(unittest.TestCase):
    def test_samples_part_1(self):
        data = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""
        p1, p2 = solve(data)
        self.assertEqual(p1, "605")
        self.assertEqual(p2, "982")
