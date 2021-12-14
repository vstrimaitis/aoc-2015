from collections import *
from typing import *
import re

SPELLS = [
    ("Magic Missile", 53, 4, 0),
    ("Drain", 73, 2, 2),
    ("Shield", 113, )
]

def check_winner(player_hp: int, player_mana: int, max_mana_spendage: int, boss_hp: int, boss_damage: int, hard_mode=False) -> bool:
    Q = deque([(player_hp, player_mana, 0, 0, boss_hp, boss_damage, [], 0)])
    while Q:
        hp, mana, armor, mana_spent, b_hp, b_dmg, effects, turn = Q.popleft()
        if mana_spent > max_mana_spendage:
            continue

        if turn == 0 and hard_mode:
            hp -= 1

        if hp <= 0:
            continue
        if mana <= 0:
            continue
        for i, (name, timer) in enumerate(effects):
            if name == "Shield" and timer == 1:
                armor -= 7
            elif name == "Poison":
                b_hp -= 3
            elif name == "Recharge":
                mana += 101
            effects[i] = (name, timer-1)
        effects = [e for e in effects if e[1] > 0]

        if b_hp <= 0:
            return True
        
        if turn == 0:
            if mana < 53:
                continue
            if mana >= 53:
                # Magic Missile
                Q.append((hp, mana-53, armor, mana_spent+53, b_hp-4, b_dmg, effects.copy(), turn^1))
            if mana >= 73:
                # Drain
                Q.append((hp+2, mana-73, armor, mana_spent+73, b_hp-2, b_dmg, effects.copy(), turn^1))
            if mana >= 113 and "Shield" not in [name for name, _ in effects]:
                # Shield
                new_effects = effects.copy()
                new_effects.append(("Shield", 6))
                Q.append((hp, mana-113, armor+7, mana_spent+113, b_hp, b_dmg, new_effects, turn^1))
            if mana >= 173 and "Poison" not in [name for name, _ in effects]:
                # Poison
                new_effects = effects.copy()
                new_effects.append(("Poison", 6))
                Q.append((hp, mana-173, armor, mana_spent+173, b_hp, b_dmg, new_effects, turn^1))
            if mana >= 229 and "Recharge" not in [name for name, _ in effects]:
                # Recharge
                new_effects = effects.copy()
                new_effects.append(("Recharge", 5))
                Q.append((hp, mana-229, armor, mana_spent+229, b_hp, b_dmg, new_effects, turn^1))
        else:
            d = max(1, b_dmg - armor)
            Q.append((hp-d, mana, armor, mana_spent, b_hp, b_dmg, effects, turn^1))
    return False

def solve(data: str) -> Tuple[str, str]:
    pattern_hp = r"Hit Points: (\d+)"
    pattern_dmg = r"Damage: (\d+)"
    boss_hp = int(re.search(pattern_hp, data).group(1))
    boss_dmg = int(re.search(pattern_dmg, data).group(1))
    
    lo, hi = 0, 1000000
    while lo < hi:
        mid = (lo + hi) // 2
        if check_winner(50, 500, mid, boss_hp, boss_dmg):
            hi = mid
        else:
            lo = mid+1
    ans1 = lo

    lo, hi = 0, 1000000
    while lo < hi:
        mid = (lo + hi) // 2
        if check_winner(50, 500, mid, boss_hp, boss_dmg, True):
            hi = mid
        else:
            lo = mid+1
    ans2 = lo
    return str(ans1), str(ans2)

if __name__ == "__main__":
    print(solve("""Hit Points: 55
Damage: 8"""))
