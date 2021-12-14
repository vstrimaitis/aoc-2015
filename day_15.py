from collections import *
from typing import Tuple

def _get_number_after_word(s: str, word: str) -> int:
    word_idx = s.find(word)
    comma_idx = s.find(",", word_idx)
    if comma_idx == -1:
        comma_idx = len(s)
    num_start_idx = word_idx + len(word) + 1
    return int(s[num_start_idx:comma_idx])

def parse_ingredient(line: str):
    cap = _get_number_after_word(line, "capacity")
    dur = _get_number_after_word(line, "durability")
    fla = _get_number_after_word(line, "flavor")
    tex = _get_number_after_word(line, "texture")
    cal = _get_number_after_word(line, "calories")
    return (cap, dur, fla, tex, cal)

def gen(ingredients, k, need, cap, dur, fla, tex, cal, count_calories=False):
    if k == len(ingredients):
        if need != 0:
            return 0
        if count_calories and cal != 500:
            return 0
        return max(cap, 0) * max(dur, 0) * max(fla, 0) * max(tex, 0)
    i_cap, i_dur, i_fla, i_tex, i_cal = ingredients[k]
    min_take = 0
    if k == len(ingredients)-1:
        min_take = need
    ans = 0
    for take in range(min_take, need+1):
        subans = gen(
            ingredients,
            k+1,
            need-take,
            cap+i_cap*take,
            dur+i_dur*take,
            fla+i_fla*take,
            tex+i_tex*take,
            cal+i_cal*take,
            count_calories,
        )
        if subans > ans:
            ans = subans
    return ans

def solve(data: str) -> Tuple[str, str]:
    ingredients = [parse_ingredient(l) for l in data.split("\n")]
    ans1 = gen(ingredients, 0, 100, 0, 0, 0, 0, 0)
    ans2 = gen(ingredients, 0, 100, 0, 0, 0, 0, 0, True)
    return str(ans1), str(ans2)

if __name__ == "__main__":
    print(solve("""Sugar: capacity 3, durability 0, flavor 0, texture -3, calories 2
Sprinkles: capacity -3, durability 3, flavor 0, texture 0, calories 9
Candy: capacity -1, durability 0, flavor 4, texture 0, calories 1
Chocolate: capacity 0, durability 0, flavor -2, texture 2, calories 8"""))
