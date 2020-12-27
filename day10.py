import numpy as np
from typing import List
input = open("day10-input.txt", "r")
numbers = input.read().split("\n")
adapters = [int(i) for i in numbers]

### Part 1: jolt distribution ###
"""
adapters.sort()

cnt_1diff = 1
cnt_2diff = 0
cnt_3diff = 1
prev_adapater = adapters[0]
# import ipdb;ipdb.set_trace()
for adapter in adapters[1:]:
    diff = adapter - prev_adapater
    if diff == 1:
        cnt_1diff = cnt_1diff + 1
    elif diff == 2:
        cnt_2diff = cnt_2diff + 1
    elif diff == 3:
        cnt_3diff = cnt_3diff + 1
    else:
        raise ValueError('Input incorrect: jolt difference cannot be larger than 3')

    prev_adapater = adapter
print(f"cnt_1diff = {cnt_1diff}")
print(f"cnt_2diff = {cnt_2diff}")
print(f"cnt_3diff = {cnt_3diff}")
print(f"Part 1: No. of 1-jolt differences x No. of 3-jolt differences = {cnt_1diff*cnt_3diff}")
"""

### Part 2: No. of distinct ways of arranging adapters ###
adapters.append(0)
adapters.append(max(adapters)+3)
adapters.sort()

index = 0
valid_adapt_index = 1
tot_distinct_ways: List[int] = []
lower: List[int] = []
upper: List[int] = []

# def eval_distinct_ways(lower: List[int], upper: List[int], relative_to: int, follow_number: int) -> int:

while index < len(adapters):
    # import ipdb; ipdb.set_trace()
    try:
        next_digit = adapters[index+valid_adapt_index]
    except IndexError:
        # The last number in the list will always be 3 larger than 
        # the previous number, so we can go ahead and break the loop
        break
    
    # Find all valid adapters (up to 3)
    if next_digit - adapters[index] <= 3:
        lower.append(next_digit)
        valid_adapt_index = valid_adapt_index + 1
    else:
        # Evaluate the no. of distinct ways within this combination
        if len(lower) > 1:
            lower.reverse()
            for num in lower:
                if next_digit - num <= 3:
                    upper.append(num)
                else:
                    break
            distinct_ways = (pow(2, len(upper)) - 1) * pow(2, len(lower) - len(upper))
            tot_distinct_ways.append(distinct_ways)
            index = index + valid_adapt_index
        else:
            index = index + 1
        
        # Update/reset variables 
        valid_adapt_index = 1
        lower = []
        upper = []

print(f"Part 2: The total number of distinct ways of connecting the adapter is: {np.prod(tot_distinct_ways)}")