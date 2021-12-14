import unittest
from day_12 import solve

class TestSamples(unittest.TestCase):
    def test_samples_part_1(self):
        for data, exp in [("[1,2,3]", 6), ("""{"a":2,"b":4}""", 6), ("[[[3]]]", 3), ("""{"a":{"b":4},"c":-1}""", 3), ("""{"a":[-1,1]}""", 0), ("""[-1,{"a":1}]""", 0), ("[]", 0), ("{}", 0)]:
            p1, _ = solve(data)
            self.assertEqual(p1, str(exp), data)

    def test_samples_part_2(self):
        for data, exp in [("[1,2,3]", 6), ("""[1,{"c":"red","b":2},3]""", 4), ("""{"d":"red","e":[1,2,3,4],"f":5}""", 0), ("""[1,"red",5]""", 6)]:
            _, p2 = solve(data)
            self.assertEqual(p2, str(exp), data)
