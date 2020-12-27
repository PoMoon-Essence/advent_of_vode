from typing import List, Optional
import copy

input = open("day11-input.txt", "r")
seat_map = input.read().split("\n")

### Part 1: No. of occupied seats ###
"""
original_map = [[char for char in row] for row in seat_map]

def update_layout(layout: List[List[str]], limit_right: int, limit_bottom: int) -> List[List[str]]:
    new_layout = copy.deepcopy(layout)
    row_index = 0

    for row in layout:
        col_index = 0
        for seat in row:
            if seat == '.':
                col_index = col_index + 1
                continue 
            # import ipdb; ipdb.set_trace()
            adjacent_seats: List[str] = []
            # Upper row (North)
            if row_index > 0:
                # North
                adjacent_seats.append(layout[row_index-1][col_index])

                if col_index + 1 < limit_right:
                    # North East
                    adjacent_seats.append(layout[row_index-1][col_index+1])

                if col_index - 1 >= 0:
                    # North West
                    adjacent_seats.append(layout[row_index-1][col_index-1])
            
            # Current row
            if col_index + 1 < limit_right:
                # East
                adjacent_seats.append(layout[row_index][col_index+1])

            if col_index - 1 >= 0:
                # West
                adjacent_seats.append(layout[row_index][col_index-1])
            
            # Row beneath (South)
            if row_index + 1 < limit_bottom:
                # South
                adjacent_seats.append(layout[row_index+1][col_index])

                if col_index + 1 < limit_right:
                    # South East
                    adjacent_seats.append(layout[row_index+1][col_index+1])

                if col_index - 1 >= 0:
                    # South West
                    adjacent_seats.append(layout[row_index+1][col_index-1])
            
            if seat == 'L':
                unoccupied_seats = [True if pos != '#' else False for pos in adjacent_seats]
                if all(unoccupied_seats):
                    new_layout[row_index][col_index] = '#'
            elif seat == '#':
                number_of_occupied = [1 if pos == '#' else 0 for pos in adjacent_seats]
                if sum(number_of_occupied) >= 4:
                    new_layout[row_index][col_index] = 'L'
            
            col_index = col_index + 1
        row_index = row_index + 1

    return new_layout

limit_right = len(original_map[0])
limit_bottom = len(original_map)
layout = copy.deepcopy(original_map)
new_layout = None
while layout != new_layout:
    if new_layout is not None:
        layout = new_layout
    new_layout = update_layout(layout, limit_right, limit_bottom)

tot_occupied_seats = 0
for row in layout:
    for seat in row:
        if seat == '#':
            tot_occupied_seats += 1

print(f'Part 1: The total number of occupied seats in this map is {tot_occupied_seats}')
"""

### Part 2: New rules... ###
original_map = [[char for char in row] for row in seat_map]


def line_of_sight(
    layout: List[List[str]],
    start_row: int,
    start_col: int,
    north: bool,
    south: bool,
    east: bool,
    west: bool,
) -> Optional[str]:

    """
    line_of_sight checks if there is an empty seat, 'L', an occupied seat, '#',
    or simply floor, '.' in the direction specified in the arguments. 

    It returns None if the direction is out of bounds. Otherwise, it will return
    the first thing it encounters.
    """
    east_bound = len(layout[0])
    south_bound = len(layout)
    row_step = 0
    col_step = 0

    if north:
        row_step = -1
    elif south:
        row_step = 1

    if east:
        col_step = 1
    elif west:
        col_step = -1

    row = start_row + row_step
    col = start_col + col_step

    if not ((row >= 0 and row < south_bound) and (col >= 0 and col < east_bound)):
        return None  # this happens when the seat is on the edge or at the corner of the map

    while (row >= 0 and row < south_bound) and (col >= 0 and col < east_bound):
        seat = layout[row][col]
        if seat != ".":
            return seat
        row = row + row_step
        col = col + col_step
    return "."

def update_layout(layout: List[List[str]]) -> List[List[str]]:
    new_layout = copy.deepcopy(layout)
    limit_right = len(layout[0])
    limit_bottom = len(layout)
    row_index = 0

    for row in layout:
        col_index = 0
        for seat in row:
            if seat == '.':
                col_index = col_index + 1
                continue 
            # import ipdb; ipdb.set_trace()
            adjacent_seats: List[str] = []
            # Upper row (North)
            if row_index > 0:
                # North
                north = line_of_sight(layout, row_index, col_index, True, False, False, False)
                if north is not None:
                    adjacent_seats.append(north)

                if col_index + 1 < limit_right:
                    # North East
                    north_east = line_of_sight(layout, row_index, col_index, True, False, True, False)
                    if north_east is not None:
                        adjacent_seats.append(north_east)

                if col_index - 1 >= 0:
                    # North West
                    north_west = line_of_sight(layout, row_index, col_index, True, False, False, True)
                    if north_west is not None:
                        adjacent_seats.append(north_west)
            
            # Current row
            if col_index + 1 < limit_right:
                # East
                east = line_of_sight(layout, row_index, col_index, False, False, True, False)
                if east is not None:
                    adjacent_seats.append(east)

            if col_index - 1 >= 0:
                # West
                west = line_of_sight(layout, row_index, col_index, False, False, False, True)
                if west is not None:
                    adjacent_seats.append(west)
            
            # Row beneath (South)
            if row_index + 1 < limit_bottom:
                # South
                south = line_of_sight(layout, row_index, col_index, False, True, False, False)
                if south is not None:
                    adjacent_seats.append(south)

                if col_index + 1 < limit_right:
                    # South East
                    south_east = line_of_sight(layout, row_index, col_index, False, True, True, False)
                    if south_east is not None:
                        adjacent_seats.append(south_east)

                if col_index - 1 >= 0:
                    # South West
                    south_west = line_of_sight(layout, row_index, col_index, False, True, False, True)
                    if south_west is not None:
                        adjacent_seats.append(south_west)
            
            if seat == 'L':
                unoccupied_seats = [True if pos != '#' else False for pos in adjacent_seats]
                if all(unoccupied_seats):
                    new_layout[row_index][col_index] = '#'
            elif seat == '#':
                number_of_occupied = [1 if pos == '#' else 0 for pos in adjacent_seats]
                if sum(number_of_occupied) >= 5:
                    new_layout[row_index][col_index] = 'L'
            
            col_index = col_index + 1
        row_index = row_index + 1

    return new_layout

layout = copy.deepcopy(original_map)
new_layout = None
while layout != new_layout:
    if new_layout is not None:
        layout = new_layout
    new_layout = update_layout(layout)

tot_occupied_seats = 0
for row in layout:
    for seat in row:
        if seat == '#':
            tot_occupied_seats += 1

print(f'Part 2: The total number of occupied seats is {tot_occupied_seats}')