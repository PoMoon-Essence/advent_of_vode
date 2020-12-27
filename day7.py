import re
from typing import Dict
input = open("day7-input.txt", "r")
rules = input.read().split(".\n")

### Part 1 ###
def count_in_layer(rules: list, bags: set, master_list: set) -> Dict:
    parent_bags = []
    cnt = 0

    for rule in rules:
        bag_outside, inside = rule.split(" bags contain ")
        bags_inside = inside.split(", ")

        if bag_outside in color_master_list:
            continue

        for bag in bags_inside:
            m = re.match("(\d+) (.+) bags?", bag)
            if m is not None:
                color = m.group(2)
            else:
                color = 'None'

            if color in bags:
                cnt = cnt + 1
                parent_bags.append(bag_outside)
                # The bag_outside only needs to contain one of bags in our set 
                break
    
    return {'parent_bags':set(parent_bags), 'layer_count':cnt}

main_counter = 0
colors_searched_for = set(['shiny gold'])
color_master_list = set()

while len(colors_searched_for) != 0:
    layer_props = count_in_layer(rules, colors_searched_for, color_master_list)
    main_counter = main_counter + layer_props['layer_count']

    colors_searched_for = layer_props['parent_bags']    
    color_master_list = color_master_list.union(colors_searched_for)

print(
    f"Part 1: The number of bag colors that can eventually contain a gold shiny bag is: {main_counter}"
)

### Part 2 ###
# 2*(1+ 2*(1 + 2*(1 + 2*(1 + 2*(1 + 2*1))))
# 4*(1+ 3*(1 + 6*(1 + 2*(1 + 2*(1 + 2*1))))
# 1*(1 + 1*7) + 2*(1 + 1*11)

def count_bags(rules: list, color: str) -> int:
    for rule in rules:
        bag_outside, inside = rule.split(" bags contain ")
        bags_inside = inside.split(", ")

        if bag_outside == color:
            if "no other bags" in inside:
                return 0
            else:
                total_number_bags = 0
                for bag in bags_inside:
                    m = re.match("(\d+) (.+) bags?", bag)
                    number = int(m.group(1))
                    bag_inside_color = m.group(2)
                    total_number_bags = total_number_bags + number * (1 + count_bags(rules, bag_inside_color))
                return total_number_bags

answer = count_bags(rules, "shiny gold")
print(
    f"Part 2: The number of bags required inside a gold shiny bag: {answer}"
)


"""
1. Search for [shiny gold] 
2. Search for [shiny gold] child_1? 
    (A) if child_1 contains "no other bag", return 1
    (B) if child_1 contains X COLOR bags, then multiply X by
        i. Search for COLOR
            (a) if COLOR contains "no other bag", return 1
            (b) if COLOR contains Y COLOR_1 bags, then multiply Y by 
            
"""