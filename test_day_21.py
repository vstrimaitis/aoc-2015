import unittest
from day_21 import check_winner

class TestSamples(unittest.TestCase):
    def test_sample_1(self):
        ans = check_winner(8, 5, 5, 12, 7, 2)
        self.assertEqual(ans, True)
