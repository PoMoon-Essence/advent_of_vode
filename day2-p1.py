input = open("day2-p1-input.txt", "r")
password_database = input.read().split("\n")

### Part 1 ###
valid_passwords = 0
for line in password_database:
    # Extract relevant parameters
    policy, password = line.split(": ")
    freq, letter = policy.split(" ")
    lower_bound, upper_bound = freq.split("-")

    # Process parameters to the appropriate type
    lower_bound = int(lower_bound)
    upper_bound = int(upper_bound)

    # Determine if the password is valid
    counter = 0
    for char in password:
        if char == letter:
            counter = counter + 1

    if counter <= upper_bound and counter >= lower_bound:
        valid_passwords = valid_passwords + 1

print(f"Part 1: The total number of valid passwords in the database is: {valid_passwords}")

### Part 2 ###
valid_passwords = 0
for line in password_database:
    # Extract relevant parameters
    policy, password = line.split(": ")
    positions, letter = policy.split(" ")
    first_position, second_position = positions.split("-")

    # Process parameters to the appropriate type
    first_position = int(first_position)
    second_position = int(second_position)

    # Determine if the password is valid
    try:
        meet_1st_pos = (password[first_position - 1] == letter)
    except IndexError:
        meet_1st_pos = False
    
    try:
        meet_2nd_pos = (password[second_position - 1] == letter)
    except IndexError:
        meet_2nd_pos = False
    
    if meet_1st_pos + meet_2nd_pos == 1:
        valid_passwords = valid_passwords + 1

print(f"Part 2: The total number of valid passwords in the database is: {valid_passwords}")