from collections import *
from typing import *
from random import shuffle

def gen_neighs(s: str, replacements: List[Tuple[str, str]]) -> List[str]:
    neighs = set()
    for u, v in replacements:
        prev = -1
        while True:
            i = s.find(u, prev+1)
            if i == -1:
                break
            ss = s[:i] + v + s[i+len(u):]
            neighs.add(ss)
            prev = i
    return list(neighs)

def gen_neighs_inv(s: str, replacements: List[Tuple[str, str]]) -> List[str]:
    r = [(dst, src) for src, dst in replacements]
    return gen_neighs(s, r)

def calc_distance(src: str, dst: str, replacements: List[Tuple[str, str]]) -> int:
    ans = 0
    S = src
    while S != dst:
        tmp = S
        for u, v in replacements:
            if v in S:
                S = S.replace(v, u, 1)
                ans += 1
        if tmp == S:
            S = src
            ans = 0
            shuffle(replacements)
    return ans

def solve(data: str) -> Tuple[str, str]:
    replacements, molecule = data.split("\n\n")
    replacements = [l.split(" => ") for l in replacements.split("\n")]
    replacements = list(reversed(sorted(replacements, key=lambda x: len(x[1]))))
    ans1 = len(gen_neighs(molecule, replacements))
    if "e" in data:
        ans2 = calc_distance(molecule, "e", replacements)
    else:
        ans2 = ""
    return str(ans1), str(ans2)

if __name__ == "__main__":
    print(solve("""Al => ThF
Al => ThRnFAr
B => BCa
B => TiB
B => TiRnFAr
Ca => CaCa
Ca => PB
Ca => PRnFAr
Ca => SiRnFYFAr
Ca => SiRnMgAr
Ca => SiTh
F => CaF
F => PMg
F => SiAl
H => CRnAlAr
H => CRnFYFYFAr
H => CRnFYMgAr
H => CRnMgYFAr
H => HCa
H => NRnFYFAr
H => NRnMgAr
H => NTh
H => OB
H => ORnFAr
Mg => BF
Mg => TiMg
N => CRnFAr
N => HSi
O => CRnFYFAr
O => CRnMgAr
O => HP
O => NRnFAr
O => OTi
P => CaP
P => PTi
P => SiRnFAr
Si => CaSi
Th => ThCa
Ti => BP
Ti => TiTi
e => HF
e => NAl
e => OMg

CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr"""))
