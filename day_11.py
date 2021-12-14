from collections import *
from typing import Tuple
from string import ascii_lowercase

def is_valid(s: str) -> bool:
    if "i" in s or "o" in s or "l" in s:
        return False
    flag = False
    for i in range(len(s)-2):
        ss = s[i:i+3]
        if ss in ascii_lowercase:
            flag = True
            break
    if not flag:
        return False
    pairs = set()
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            ss = s[i:i+2]
            pairs.add(ss)
    return len(pairs) >= 2

def incr(s: str) -> str:
    if s[-1] == "z":
        return incr(s[:-1]) + "a"
    return s[:-1] + chr(ord(s[-1])+1)

def solve(data: str) -> Tuple[str, str]:
    ans1 = incr(data)
    while not is_valid(ans1):
        ans1 = incr(ans1)
    ans2 = incr(ans1)
    while not is_valid(ans2):
        ans2 = incr(ans2)
    return str(ans1), str(ans2)

if __name__ == "__main__":
    print(solve("""vzbxkghb"""))
