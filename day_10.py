from collections import *
from typing import Tuple
from itertools import groupby

def transform(s: str) -> str:
    return "".join([str(len(list(g))) + k for k, g in groupby(s)])

def _solve(data: str, n: int) -> str:
    for _ in range(n):
        data = transform(data)
    return data

def solve(data: str) -> Tuple[str, str]:
    ans1 = len(_solve(data, 40))
    ans2 = len(_solve(data, 50))
    return str(ans1), str(ans2)

if __name__ == "__main__":
    print(solve("""1321131112"""))
