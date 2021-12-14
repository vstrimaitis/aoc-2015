from collections import *
from typing import *
import re

WEAPONS = [
    ("Dagger", 8, 4, 0),
    ("Shortsword", 10, 5, 0),
    ("Warhammer", 25, 6, 0),
    ("Longsword", 40, 7, 0),
    ("Greataxe", 74, 8, 0),
]

ARMOR = [
    ("Dummy 1", 0, 0, 0),
    ("Leather", 13, 0, 1),
    ("Chainmail", 31, 0, 2),
    ("Splintmail", 53, 0, 3),
    ("Bandedmail", 75, 0, 4),
    ("Platemail", 102, 0, 5),
]

RINGS = [
    ("Dummy 1", 0, 0, 0),
    ("Dummy 2", 0, 0, 0),
    ("Damage +1", 25, 1, 0),
    ("Damage +2", 50, 2, 0),
    ("Damage +3", 100, 3, 0),
    ("Defense +1", 20, 0, 1),
    ("Defense +2", 40, 0, 2),
    ("Defense +3", 80, 0, 3),
]

def gen_purchases():
    for _, c1, d1, a1 in WEAPONS:
        for _, c2, d2, a2 in ARMOR:
            for r1, c3, d3, a3 in RINGS:
                for r2, c4, d4, a4 in RINGS:
                    if r1 != r2:
                        yield (c1+c2+c3+c4, d1+d2+d3+d4, a1+a2+a3+a4)


def check_winner(hp: int, damage: int, armor: int, boss_hp: int, boss_damage: int, boss_armor: int) -> bool:
    turn = 0
    while True:
        if turn == 0:
            d = max(1, damage - boss_armor)
            boss_hp -= d
            if boss_hp <= 0:
                return True
        else:
            d = max(1, boss_damage - armor)
            hp -= d
            if hp <= 0:
                return False
        turn ^= 1

def solve(data: str) -> Tuple[str, str]:
    pattern_hp = r"Hit Points: (\d+)"
    pattern_dmg = r"Damage: (\d+)"
    pattern_arm = r"Armor: (\d+)"
    boss_hp = int(re.search(pattern_hp, data).group(1))
    boss_dmg = int(re.search(pattern_dmg, data).group(1))
    boss_arm = int(re.search(pattern_arm, data).group(1))
    ans1 = 10**100
    for cost, damage, armor in gen_purchases():
        if check_winner(100, damage, armor, boss_hp, boss_dmg, boss_arm):
            ans1 = min(ans1, cost)
    ans2 = -10**100
    for cost, damage, armor in gen_purchases():
        if not check_winner(100, damage, armor, boss_hp, boss_dmg, boss_arm):
            ans2 = max(ans2, cost)
    return str(ans1), str(ans2)

if __name__ == "__main__":
    print(solve("""Hit Points: 109
Damage: 8
Armor: 2"""))
