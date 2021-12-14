from hashlib import md5
from typing import Tuple

def _hash(s: str) -> str:
    return md5(s.encode()).hexdigest()

def find(input_prefix: str, output_prefix: str) -> int:
    i = 1
    while not _hash(input_prefix + str(i)).startswith(output_prefix):
        i += 1
    return i

def solve(data: str) -> Tuple[str, str]:
    return str(find(data, "00000")), str(find(data, "000000"))

if __name__ == "__main__":
    print(solve("""iwrupvqb"""))
