import unittest
from day_19 import solve

class TestSamples(unittest.TestCase):
    def test_sample_1(self):
        data = """H => HO
H => OH
O => HH

HOH"""
        p1, _ = solve(data)
        self.assertEqual(p1, "4")

    def test_sample_2(self):
        data = """H => HO
H => OH
O => HH

HOHOHO"""
        p1, _ = solve(data)
        self.assertEqual(p1, "7")

    def test_sample_3(self):
        data = """e => H
e => O
H => HO
H => OH
O => HH

HOH"""
        _, p2 = solve(data)
        self.assertEqual(p2, "3")
