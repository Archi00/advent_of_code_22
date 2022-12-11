#!/usr/bin/python3

# CPU has single register = X | starts with the value 1
# only supports 2 instructions:
#   addx V -> takes 2 cycles to complete 
#             after 2 cycles X += V (V can be negative)
#   noop -> takes 1 cycle to complete -> has no other effect

with open("input.txt") as f:
    instructions = f.read().split("\n")

cycle = 1
X = 1
STEP = 20

ret_list = list()

def parse_input(inst):
    if inst == "noop":
        return (1, 0)
    _, num_to_add = inst.split(" ")
    return (2, int(num_to_add))

def register_cycle(cycle, X):
    global STEP
    ret_list.append(cycle * X)
    print(f"Cycle: {cycle} X: {X}")
    STEP += 40

def register_next_cycle(cycle, X):
    global STEP
    ret_list.append((cycle + 1) * X)
    print(f"Cycle: {cycle + 1} X: {X}")
    STEP += 40

for idx in range(len(instructions)):
    if idx == len(instructions) - 1:
        break
    (c, to_add) = parse_input(instructions[idx])
    next_c, _ = parse_input(instructions[idx + 1])
    cycle += c
    X += to_add
    if cycle == STEP - 1 and next_c == 2:
        register_next_cycle(cycle, X)
    if cycle == STEP:
        register_cycle(cycle, X)

ret = sum(ret_list) 
print(f"Result: {ret}")