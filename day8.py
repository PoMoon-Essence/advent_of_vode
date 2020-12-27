from typing import List, Tuple
import pandas as pd
import numpy as np
input = open("day8-input.txt", "r")
code: List[str] = input.read().split("\n")

### Part 1 ###
"""
accumulator = 0
line_traversed: List[int] = []

i = 0
while i not in set(line_traversed):
    line_traversed.append(i)
    counter_override = False

    instruction = code[i].split(' ')
    operation = instruction[0]
    argument = instruction[1]
    sign = argument[0]
    value = int(argument[1:])

    if operation == 'acc':
        if sign == '+':
            accumulator = accumulator + value
        elif sign == '-':
            accumulator = accumulator - value
        else:
            raise SyntaxError()

    elif operation == 'jmp':
        counter_override = True
        if sign == '+':
            i = i + value
        elif sign == '-':
            i = i - value
        else:
            raise SyntaxError()
    elif operation == 'nop':
        pass
    
    if counter_override == False:
        i = i + 1
print(f"Part 1: Accumulator value is {accumulator}")
"""

### Part 2 ###
accumulator = 0
line_traversed: List[int] = []
jmp_nop_loc: List[int] = []

def add_subtract(initial_val: int, operator: str, value: int) -> int:
    if operator == '+':
        return initial_val + value
    elif operator == '-':
        return initial_val - value
    else:
        import ipdbs; ipdb.set_trace()
        raise SyntaxError()

def extract_params(code: str) -> Tuple[str, str, int]:
    instruction = code.split(' ')
    operation = instruction[0]
    argument = instruction[1]
    sign = argument[0]
    value = int(argument[1:])

    return (operation, sign, value)

def eof_acc_value(code: List) -> int:
    accumulator = 0
    i = 0
    line_traversed: List[int] = []
    last_line = len(code) - 1
    # import ipdb;ipdb.set_trace()
    while (i not in set(line_traversed)) and i <= last_line:
        if i == last_line:
            import ipdb;ipdb.set_trace()
        line_traversed.append(i)
        counter_override = False
        operation, sign, value = extract_params(code[i])

        if operation == 'acc':
            accumulator = add_subtract(accumulator, sign, value)
        elif operation == 'jmp':
            counter_override = True
            i = add_subtract(i, sign, value)
        elif operation == 'nop':
            pass
        
        if i == last_line:
            break

        if counter_override == False:
            i = i + 1
    
    if i > last_line:
        return accumulator
    else:
        return np.NaN

# Find the location of all jmp and nop operations
index = 0
for line in code:
    operation, _, _ = extract_params(line)
    if operation == 'jmp' or operation == 'nop':
        jmp_nop_loc.append(index)
    index = index + 1

# Flip a nop or jmp, then see if the script gets stuck in a loop 
for i in jmp_nop_loc:
    operation, sign, value = extract_params(code[i])
    # import ipdb;ipdb.set_trace()
    if operation == 'jmp':
        mod = code.copy()
        mod[i] = 'nop ' + sign + str(value)
        final_accumulator = eof_acc_value(mod)
        if not(pd.isnull(final_accumulator)):
            break

    elif operation == 'nop':
        mod = code.copy()
        mod[i] = 'jmp ' + sign + str(value)
        final_accumulator = eof_acc_value(mod)
        if not(pd.isnull(final_accumulator)):
            break

print(f"Part 2: Final accumulator's value is {final_accumulator}")