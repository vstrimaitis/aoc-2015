from collections import *
from typing import *

Command = Tuple[str, Union[str, Tuple[str, str]]]
Memory = Dict[str, int]

def parse_command(s: str) -> Command:
    parts = s.split(", ")
    if len(parts) == 1:
        parts = s.split(" ")
        return parts[0], parts[1]
    offset = parts[1]
    parts = parts[0].split(" ")
    return parts[0], (parts[1], offset)
    
def run(program: List[Command], initial_mem: Memory = {}) -> Memory:
    mem = {"a": initial_mem.get("a", 0), "b": initial_mem.get("b", 0)}
    ip = 0
    while 0 <= ip < len(program):
        cmd, arg = program[ip]
        if cmd == "hlf":
            mem[arg] /= 2
            ip += 1
        elif cmd == "tpl":
            mem[arg] *= 3
            ip += 1
        elif cmd == "inc":
            mem[arg] += 1
            ip += 1
        elif cmd == "jmp":
            offset = int(arg)
            ip += offset
        elif cmd == "jie":
            r, offset = arg[0], int(arg[1])
            if mem[r] % 2 == 0:
                ip += offset
            else:
                ip += 1
        elif cmd == "jio":
            r, offset = arg[0], int(arg[1])
            if mem[r] == 1:
                ip += offset
            else:
                ip += 1
    return mem


def solve(data: str) -> Tuple[str, str]:
    commands = list(map(parse_command, data.split("\n")))
    ans1 = run(commands)["b"]
    ans2 = run(commands, {"a": 1})["b"]
    return str(ans1), str(ans2)

if __name__ == "__main__":
    print(solve("""jio a, +18
inc a
tpl a
inc a
tpl a
tpl a
tpl a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
tpl a
tpl a
inc a
jmp +22
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
jio a, +8
inc b
jie a, +4
tpl a
inc a
jmp +2
hlf a
jmp -7"""))
