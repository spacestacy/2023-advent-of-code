input_strings = []

with open(r"Advent of Code 2023\inputs\day_01.txt",'r') as input_file:
  input_strings.extend(line.strip() for line in input_file)

final_sum = 0

## Part 1
# def number_parser(string):
#     for i in string:
#         if i.isnumeric():
#             first_num = i
#             break
#     for i in string[::-1]:
#         if i.isnumeric():
#             last_num = i
#             break
#     return int(first_num + last_num);

# Part 2
def is_substring_present(main_string, string_list):
    for substring in string_list:
        if substring in main_string:
            return substring
    return False

def number_parser(string):
    numbers = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

    first_num = None
    last_num = None
    
    for i in range(len(string)):
        number = is_substring_present(string[:i + 1], numbers)
        if number or string[i].isnumeric():
            first_num = numbers.get(number, string[i])
            break
    for i in range(-1, -len(string) - 1, -1):
        number = is_substring_present(string[i:], numbers)
        if number or string[i].isnumeric():
            last_num = numbers.get(number, string[i])
            break
    return int(first_num + last_num)

for string in input_strings:
    final_sum += number_parser(string)

print(final_sum)