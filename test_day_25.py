import unittest
from day_25 import solve

class TestSamples(unittest.TestCase):
    def test_sample(self):
        table = [
            [20151125,  18749137,  17289845,  30943339,  10071777,  33511524],
            [31916031,  21629792,  16929656,   7726640,  15514188,   4041754],
            [16080970,   8057251,   1601130,   7981243,  11661866,  16474243],
            [24592653,  32451966,  21345942,   9380097,  10600672,  31527494],
            [   77061,  17552253,  28094349,   6899651,   9250759,  31663883],
            [33071741,   6796745,  25397450,  24659492,   1534922,  27995004],
        ]
        for i in range(len(table)):
            for j in range(len(table)):
                inp = f"To continue, please consult the code grid in the manual.  Enter the code at row {i+1}, column {j+1}."
                res, _ = solve(inp)
                self.assertEqual(res, str(table[i][j]))
