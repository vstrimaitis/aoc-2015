import unittest
from day_07 import _solve

class TestSamples(unittest.TestCase):
    def test_samples_part_1(self):
        data = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i"""
        for wire, expected in [("d", 72), ("e", 507), ("f", 492), ("g", 114), ("h", 65412), ("i", 65079), ("x", 123), ("y", 456)]:
            ans  = _solve(data, wire)
            self.assertEqual(ans, expected)
