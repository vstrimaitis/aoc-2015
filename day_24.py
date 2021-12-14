from collections import *
from typing import *

def gen(nums, k, target, first_sum=0, first=(0, 1), best=(10**10, 10**10)):
    if first[0] > best[0]:
        return best
    if first[0] == best[0] and first[1] > best[1]:
        return best
    if first_sum > target:
        return best
    if first_sum == target:
        return min(first, best)
    if k == len(nums):
        return best
    
    best = min(best, gen(nums, k+1, target, first_sum, first, best))
    best = min(best, gen(nums, k+1, target, first_sum + nums[k], (first[0]+1, first[1]*nums[k]), best))
    return best


def solve(data: str) -> Tuple[str, str]:
    nums = [int(x) for x in data.split("\n")]
    _, ans1 = gen(nums, 0, sum(nums)//3)
    _, ans2 = gen(nums, 0, sum(nums)//4)
    return str(ans1), str(ans2)

if __name__ == "__main__":
    print(solve("""1
2
3
7
11
13
17
19
23
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
101
103
107
109
113"""))
