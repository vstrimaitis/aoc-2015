import unittest
from day_05 import solve

class TestSamples(unittest.TestCase):
    def test_samples_part_1(self):
        for data, exp in [("ugknbfddgicrmopn", 1), ("aaa", 1), ("jchzalrnumimnmhp", 0), ("haegwjzuvuyypxyu", 0), ("dvszwmarrgswjxmb", 0)]:
            p1, _ = solve(data)
            self.assertEqual(p1, str(exp))

    def test_samples_part_2(self):
        for data, exp in [("qjhvhtzxzqqjkmpb", 1), ("xxyxx", 1), ("uurcxstgmygtbstg", 0), ("ieodomkazucvgmuy", 0)]:
            _, p2 = solve(data)
            self.assertEqual(p2, str(exp))
