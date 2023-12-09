reports = []

with open(r"Advent of Code\2023\spacestacy\inputs\day_09.txt",'r') as input_file:
    for line in input_file:
        reports.append([int(i) for i in line.split()])

def extrapolate(history, is_forward_extrapolation):
    extrapolation = [history]
    element_wise_difference = [True]
    current_position = 0
    
    while any(element_wise_difference):
        element_wise_difference = []
        for i in range(0, len(extrapolation[current_position]) - 1):
            element_wise_difference.append(extrapolation[current_position][i + 1] - extrapolation[current_position][i])
        extrapolation.append(element_wise_difference)
        current_position += 1

    if is_forward_extrapolation:
        for i in range(-2, -len(extrapolation) - 1, -1):
            extrapolation[i].append(extrapolation[i][-1] + extrapolation[i + 1][-1])
    else:
        for i in range(-2, -len(extrapolation) - 1, -1):
            extrapolation[i].append(extrapolation[i][0] - extrapolation[i + 1][-1])
    
    return extrapolation

## Part 1
# extrapolation_direction = 'forward'

## Part 2
extrapolation_direction = 'backward'

sum_of_extrapolations = 0
for report in reports:
    extrapolation = extrapolate(report, True if extrapolation_direction == 'forward' else False)
    sum_of_extrapolations += extrapolation[0][-1]

print(sum_of_extrapolations)