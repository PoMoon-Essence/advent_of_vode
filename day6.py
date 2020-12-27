input = open("day6-input.txt", "r")
custom_forms = input.read().split("\n\n")

### Part 1 ###
total_questions_answered = 0
for group in custom_forms:
    individuals = group.split("\n")
    all_answers = []
    for individual in individuals:
        for answer in individual:
            all_answers.append(answer)
    distinct_answers = set(all_answers)
    total_questions_answered = total_questions_answered + len(distinct_answers)

print(f"Part 1: The total number of questions answered is {total_questions_answered}")


### Part 2 ###
total_questions_answered = 0
for group in custom_forms:
    individuals = group.split("\n")

    # First set (individual)
    answers = []
    for answer in individuals[0]:
        answers.append(answer)
    overlap = set(answers)

    # Remaining sets (other individuals in the group)
    for individual in individuals[1:]:
        answers = []
        for answer in individual:
            answers.append(answer)
        other_set = set(answers)
        overlap = overlap.intersection(other_set)
    valid_answers = set(overlap)
    total_questions_answered = total_questions_answered + len(valid_answers)

print(f"Part 2: The total number of questions answered is {total_questions_answered}")
