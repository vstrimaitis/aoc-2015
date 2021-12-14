import unittest
from day_18 import _solve

class TestSamples(unittest.TestCase):
    def test_sample_part_1(self):
        data = """.#.#.#
...##.
#....#
..#...
#.#..#
####.."""
        p1 = _solve(data, 4)
        p2 = _solve(data, 5, True)
        self.assertEqual(p1, 4)
        self.assertEqual(p2, 17)
