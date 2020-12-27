from typing import List
input = open("day9-input.txt", "r")
numbers = input.read().split("\n")
xmas = [int(i) for i in numbers]

preamble_length = 25

### Part 1: Find the first number that violates the rule ###
pos_post_preamble = range(preamble_length, len(xmas))
first_number = None 

for i in pos_post_preamble:
    preamble = xmas[i-preamble_length:i]
    for j in range(preamble_length):
        for k in range(j + 1, preamble_length):
            if preamble[j] + preamble[k] == xmas[i]:
                break
        if preamble[j] + preamble[k] == xmas[i]:
            break
    if preamble[j] + preamble[k] != xmas[i]:
        first_number = xmas[i]
        break

print(f"Part 1: The first number to violate the rule is {first_number}")


### Part 2: Find the XMAS weakness ###
invalid_number = 507622668 #127
lowest_index = 0
highest_index = lowest_index + 1
running_total: List[int] = []

while True:
    if sum(running_total) == invalid_number:
        break
    
    if sum(running_total) < invalid_number:
        highest_index = highest_index + 1
        running_total.append(xmas[highest_index])
    elif sum(running_total) > invalid_number:
        running_total = []
        lowest_index = lowest_index + 1
        highest_index = lowest_index + 1
        # It's a contiguous set, not a single number, so
        # we'll always have at least two numbers in the list
        running_total.append(xmas[lowest_index])
        running_total.append(xmas[highest_index])

print(f"Part 2: The encryption weakness is {max(running_total) + min(running_total)}")