from collections import *
from typing import Tuple, List
from itertools import combinations

def _solve(containers: List[int], total: int) -> Tuple[int, int]:
    ans1 = 0
    min_count = len(containers)
    for l in range(1, len(containers)+1):
        for c in combinations(containers, l):
            if sum(c) == total:
                ans1 += 1
                if len(c) < min_count:
                    min_count = len(c)

    ans2 = 0
    for c in combinations(containers, min_count):
        if sum(c) == total:
            ans2 += 1

    return ans1, ans2

def solve(data: str) -> Tuple[str, str]:
    containers = [int(x) for x in data.split("\n")]
    ans1, ans2 = _solve(containers, 150)
    return str(ans1), str(ans2)

if __name__ == "__main__":
    print(solve("""43
3
4
10
21
44
4
6
47
41
34
17
17
44
36
31
46
9
27
38"""))
