from collections import *
from typing import Tuple
import re

def calc_distance(r, t):
    _, speed, fly_time, rest_time = r
    cycle_duration = fly_time + rest_time
    ans = (t // cycle_duration) * (speed*fly_time)
    left = t % cycle_duration
    ans += speed * min(fly_time, left)
    return ans

def _solve(data: str, t: int):
    pattern = r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds."
    reindeer = []
    for line in data.split("\n"):
        res = re.search(pattern, line)
        assert res
        name = res.group(1)
        speed = int(res.group(2))
        fly_time = int(res.group(3))
        rest_time = int(res.group(4))
        reindeer.append((name, speed, fly_time, rest_time))
    ans1 = 0
    for r in reindeer:
        final_distance = calc_distance(r, t)
        if final_distance > ans1:
            ans1 = final_distance

    pts = [0] * len(reindeer)
    for i in range(1, t+1):
        dists = [calc_distance(r, i) for r in reindeer]
        mx = max(dists)
        js = [j for j in range(len(dists)) if dists[j] == mx]
        for j in js:
            pts[j] += 1

    return ans1, max(pts)
    

def solve(data: str) -> Tuple[str, str]:
    ans1, ans2 = _solve(data, 2503)
    
    return str(ans1), str(ans2)

if __name__ == "__main__":
    print(solve("""Rudolph can fly 22 km/s for 8 seconds, but then must rest for 165 seconds.
Cupid can fly 8 km/s for 17 seconds, but then must rest for 114 seconds.
Prancer can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.
Donner can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.
Dasher can fly 11 km/s for 12 seconds, but then must rest for 125 seconds.
Comet can fly 21 km/s for 6 seconds, but then must rest for 121 seconds.
Blitzen can fly 18 km/s for 3 seconds, but then must rest for 50 seconds.
Vixen can fly 20 km/s for 4 seconds, but then must rest for 75 seconds.
Dancer can fly 7 km/s for 20 seconds, but then must rest for 119 seconds."""))
