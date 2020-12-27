from typing import List
import numpy as np
input = open("day12-input.txt","r")
instructions = input.read().split('\n')

### Part 1: Find the Manhattan distance ###
"""
F_degree = 90
starting_position = [0,0]
position = starting_position
x = 0
y = 1

for instruction in instructions:
    # import ipdb;ipdb.set_trace()
    action = instruction[0]
    values = int(instruction[1:])

    if action == 'F':
        if F_degree == 0:
            action = 'N'
        elif F_degree == 90:
            action = 'E'
        elif F_degree == 180:
            action = 'S'
        elif F_degree == 270:
            action = 'W'

    if action == 'N':
        position[y] = position[y] + values
    elif action == 'S':
        position[y] = position[y] - values
    elif action == 'E':
        position[x] = position[x] + values
    elif action == 'W':
        position[x] = position[x] - values
    elif action == 'L':
        F_degree = (F_degree - values + 360) % 360
    elif action == 'R':
        F_degree = (F_degree + values) % 360
    
manhattan_distance = [abs(distance) for distance in position]
print(f"Part 1: The Manhattan distance between that location and the ship's starting position is {sum(manhattan_distance)}")
"""

### Part 2: Waypoint ###
waypoint = [10, 1]
ship = [0, 0]
x = 0
y = 1

def flip_digits(original_pos: List[int]) -> List[int]:
    old_x = original_pos[x]
    old_y = original_pos[y]

    return [old_y, old_x]

for instruction in instructions:
    action = instruction[0]
    values = int(instruction[1:])

    if action == 'F':
        step = [values * position for position in waypoint]
        ship[x] = ship[x] + step[x]
        ship[y] = ship[y] + step[y]

    if action == 'N':
        waypoint[y] = waypoint[y] + values
    elif action == 'S':
        waypoint[y] = waypoint[y] - values
    elif action == 'E':
        waypoint[x] = waypoint[x] + values
    elif action == 'W':
        waypoint[x] = waypoint[x] - values
    elif action == 'L' or action == 'R':
        # Do nothing if it's a 360 turn
        if values == 360:
            continue
        # Flip the axes if it's a 180 turn
        elif values == 180:
            waypoint = [position * -1 for position in waypoint]
            continue
        
        # 90/180 turns are a bit more tricky
        if instruction == 'L90' or instruction == 'R270':
            waypoint[y] = waypoint[y] * -1
            waypoint = flip_digits(waypoint)
        elif instruction == 'L270' or instruction == 'R90':
            waypoint = flip_digits(waypoint)
            waypoint[y] = waypoint[y] * -1
    print(instruction)
    print(waypoint)
    
manhattan_distance = [abs(distance) for distance in ship]
print(f"Part 1: The Manhattan distance between that location and the ship's starting waypoint is {sum(manhattan_distance)}")