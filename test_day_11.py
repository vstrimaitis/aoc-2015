import unittest
from day_11 import is_valid, solve

class TestSamples(unittest.TestCase):
    def test_is_valid(self):
        for data, exp in [("hijklmmn", False), ("abbceffg", False), ("abbcegjk", False), ("abcdefgh", False), ("abcdffaa", True), ("ghijklmn", False), ("ghjaabcc", True)]:
            self.assertEqual(is_valid(data), exp, data)
    
    def test_samples_part_1(self):
        for data, exp in [("abcdefgh", "abcdffaa"), ("ghijklmn", "ghjaabcc")]:
            p1, _ = solve(data)
            self.assertEqual(p1, exp)
