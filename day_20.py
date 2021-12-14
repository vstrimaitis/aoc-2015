from collections import *
from typing import *

def calc(x: int) -> int:
    ans = 0
    i = 1
    while i*i <= x:
        if x % i == 0:
            ans += 10*i
            if i != x // i:
                ans += 10*(x//i)
        i += 1
    return ans

def calc2(x: int) -> int:
    ans = 0
    i = 1
    while i*i <= x:
        if x % i == 0:
            if x // i <= 50:
                ans += 11*i
            if i <= 50 and i != x // i:
                ans += 11*(x//i)
        i += 1
    return ans

def solve(data: str) -> Tuple[str, str]:
    target = int(data)
    print("Solving part 1...")
    i = 1
    while calc(i) < target:
        i += 1
    ans1 = i
    print("Solving part 2...")
    i = 1
    while calc2(i) < target:
        i += 1
    ans2 = i
    return str(ans1), str(ans2)

if __name__ == "__main__":
    print(solve("""29000000"""))
