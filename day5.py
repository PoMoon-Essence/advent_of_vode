input = open("day5-input.txt", "r")
seats = input.read().split("\n")

total_rows = 128
total_cols = 8


def number_finder(key: str, upper: int, lower: int = 0) -> int:
    i = 0
    while (upper - lower) != 1:
        half = (upper - lower + 1) / 2 + lower
        if key[i] == "B" or key[i] == "R":
            lower = half
        elif key[i] == "F" or key[i] == "L":
            upper = half - 1
        i = i + 1

    if key[i] == "B" or key[i] == "R":
        return upper
    else:
        return lower


seat_ids = []

### Part 1 ###
highest_id = 0
for seat in seats:
    # Find out the row number
    row_key = seat[0:7]
    upper = total_rows - 1
    row = number_finder(row_key, upper)

    # Find out the column number
    col_key = seat[-3:]
    upper = total_cols - 1
    col = number_finder(col_key, upper)

    # Compute the seat ID
    seat_id = row * 8 + col
    if seat_id > highest_id:
        highest_id = seat_id

    # For Part 2 #
    seat_ids.append(seat_id)

print(f"The highest seat ID is {highest_id}")

### Part 2 ###
seat_ids = set(seat_ids)
min_id = min(seat_ids)
max_id = max(seat_ids)

# import ipdb; ipdb.set_trace()
for row_num in range(total_rows):
    for col_num in range(total_cols):
        seat = row_num * 8 + col_num
        if seat >= min_id and seat <= max_id:
            if seat not in seat_ids:
                # check if id +1 and -1 also exist
                if ((seat + 1) in seat_ids) and ((seat - 1) in seat_ids):
                    possible_seats = seat

print(f"The only possible seat id for you is: {possible_seats}")
