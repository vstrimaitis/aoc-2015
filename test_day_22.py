import unittest
from day_22 import check_winner

class TestSamples(unittest.TestCase):
    def test_sample_1(self):
        ans = check_winner(10, 250, 10**10, 13, 8)
        self.assertEqual(ans, True)

    def test_sample_2(self):
        ans = check_winner(10, 250, 10**10, 14, 8)
        self.assertEqual(ans, True)
