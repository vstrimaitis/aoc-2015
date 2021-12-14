import unittest
from day_14 import _solve

class TestSamples(unittest.TestCase):
    def test_samples(self):
        data = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""
        p1, p2 = _solve(data, 1000)
        self.assertEqual(p1, 1120)
        self.assertEqual(p2, 689)
