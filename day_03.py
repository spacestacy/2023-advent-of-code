DIRECTIONS = ((-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
NOT_SYMBOLS = "0123456789."
input_list = []

with open(r"Advent of Code 2023/inputs/day_03.txt",'r') as input_file:
    input_list = input_file.readlines()
    input_list = [list(i.strip()) for i in input_list]

GRID_ROW_SIZE = len(input_list)
GRID_COLUMN_SIZE = len(input_list[0])
valid_index = lambda row, column: 0 <= row <= GRID_ROW_SIZE - 1 and 0 <= column <= GRID_COLUMN_SIZE - 1

## Part 1
# part_number_sum = 0

# def parse_part_number(row, column):
#     current_part_number = input_list[row][column]
#     for current_column in range(column + 1, GRID_ROW_SIZE):
#         if input_list[row][current_column].isnumeric():
#             current_part_number += input_list[row][current_column]
#             input_list[row][current_column] = '.'
#         else:
#             break
#     for current_column in range(column - 1, -1, -1):
#         if input_list[row][current_column].isnumeric():
#             current_part_number = input_list[row][current_column] + current_part_number
#             input_list[row][current_column] = '.'
#         else:
#             break
#     print(current_part_number)
#     return int(current_part_number)

# for row_number in range(0, GRID_ROW_SIZE):
#     for column_number in range(0, GRID_COLUMN_SIZE):
#         if (input_list[row_number][column_number] not in NOT_SYMBOLS):
#             for i, j in DIRECTIONS:
#                 end_row = row_number + i
#                 end_column = column_number + j
#                 if valid_index(end_row, end_column) and input_list[end_row][end_column].isnumeric():
#                     part_number_sum += parse_part_number(end_row, end_column)

## Part 2
gear_ratio_sum = 0

def parse_part_number(row, column):
    current_part_number = input_list[row][column]
    for current_column in range(column + 1, GRID_ROW_SIZE):
        if input_list[row][current_column].isnumeric():
            current_part_number += input_list[row][current_column]
            input_list[row][current_column] = '.'
        else:
            break
    for current_column in range(column - 1, -1, -1):
        if input_list[row][current_column].isnumeric():
            current_part_number = input_list[row][current_column] + current_part_number
            input_list[row][current_column] = '.'
        else:
            break
    print(current_part_number)
    return int(current_part_number)

for row_number in range(0, GRID_ROW_SIZE):
    for column_number in range(0, GRID_COLUMN_SIZE):
        if (input_list[row_number][column_number] == "*"):
            gear_ratio = 1
            gear_ratio_count = 0
            for i, j in DIRECTIONS:
                end_row = row_number + i
                end_column = column_number + j
                if valid_index(end_row, end_column) and input_list[end_row][end_column].isnumeric():
                    gear_ratio *= parse_part_number(end_row, end_column)
                    gear_ratio_count += 1
            if gear_ratio_count == 2:
                gear_ratio_sum += gear_ratio
                    
print(gear_ratio_sum)