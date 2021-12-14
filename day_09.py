from collections import *
from typing import Tuple
import re
from itertools import permutations

def solve(data: str) -> Tuple[str, str]:
    pattern = r"(\w+) to (\w+) = (\d+)"
    adj = dict()
    nodes = set()
    for line in data.split("\n"):
        res = re.search(pattern, line, re.IGNORECASE)
        assert res
        u = res.group(1)
        v = res.group(2)
        w = int(res.group(3))
        adj[(u, v)] = w
        adj[(v, u)] = w
        nodes.add(u)
        nodes.add(v)
    nodes = list(nodes)

    ans1 = 10**100
    ans2 = 0
    for p in permutations(nodes):
        total = 0
        for u, v in zip(p, p[1:]):
            if (u, v) not in adj:
                total = 10**100
                break
            total += adj[(u, v)]
        if total < ans1:
            ans1 = total
        if total > ans2:
            ans2 = total
    
    return str(ans1), str(ans2)

if __name__ == "__main__":
    print(solve("""Tristram to AlphaCentauri = 34
Tristram to Snowdin = 100
Tristram to Tambi = 63
Tristram to Faerun = 108
Tristram to Norrath = 111
Tristram to Straylight = 89
Tristram to Arbre = 132
AlphaCentauri to Snowdin = 4
AlphaCentauri to Tambi = 79
AlphaCentauri to Faerun = 44
AlphaCentauri to Norrath = 147
AlphaCentauri to Straylight = 133
AlphaCentauri to Arbre = 74
Snowdin to Tambi = 105
Snowdin to Faerun = 95
Snowdin to Norrath = 48
Snowdin to Straylight = 88
Snowdin to Arbre = 7
Tambi to Faerun = 68
Tambi to Norrath = 134
Tambi to Straylight = 107
Tambi to Arbre = 40
Faerun to Norrath = 11
Faerun to Straylight = 66
Faerun to Arbre = 144
Norrath to Straylight = 115
Norrath to Arbre = 135
Straylight to Arbre = 127"""))
