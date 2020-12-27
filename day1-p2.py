import math

input = open("day1-p1-input.txt","r")
expense_report = input.read().split('\n')
expense_report = [int(e) for e in expense_report]

for e in expense_report:
    for e_2 in expense_report:
        for e_3 in expense_report:
            if e + e_2 + e_3 == 2020:
                break 
        if e + e_2 + e_3 == 2020:
            break
    if e + e_2 + e_3 == 2020:
        break

print(f'The three expenses are: {e}, {e_2} and {e_3}.')
print(f'Multiply them together will give you {e * e_2 * e_3}')