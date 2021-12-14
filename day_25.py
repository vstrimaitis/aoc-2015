from collections import *
from typing import *
import re

def solve(data: str) -> Tuple[str, str]:
    pattern = r"Enter the code at row (\d+), column (\d+)"
    res = re.search(pattern, data)
    row = int(res.group(1))
    col = int(res.group(2))
    ans1 = ""
    ans2 = ""

    row = row + col - 1
    start = row*(row-1)//2+1
    index = start + (col - 1)

    ans1 = 20151125*pow(252533, index-1, 33554393) % 33554393

    return str(ans1), str(ans2)

if __name__ == "__main__":
    print(solve("""To continue, please consult the code grid in the manual.  Enter the code at row 3010, column 3019."""))
