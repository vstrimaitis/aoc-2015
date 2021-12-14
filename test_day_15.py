import unittest
from day_15 import solve

class TestSamples(unittest.TestCase):
    def test_sample(self):
        data = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""
        p1, p2 = solve(data)
        self.assertEqual(p1, "62842880")
        self.assertEqual(p2, "57600000")
