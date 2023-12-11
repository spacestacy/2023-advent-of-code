directions = {'|': [(-1, 0), (1, 0)], '-': [(0, 1), (0, -1)], 'L': [(-1, 0), (0, 1)], 'J': [(-1, 0), (0, -1)], '7': [(1, 0), (0, -1)], 'F': [(1, 0), (0, 1)], '.': [], 'S': [(1, 0), (0, 1), (-1, 0), (0, -1)]}
graph = {}
map = None

with open(r"Advent of Code\2023\spacestacy\inputs\day_10.txt",'r') as input_file:
    map = input_file.readlines()
    map = [i.strip() for i in map]

for s in map:
    if 'S' in s:
        start = (map.index(s), s.index('S'))
        break

## Part 1
# max_distance = -1
# current_distance = 1
# current_point = start
# for initial_direction in directions['S']:
#     previous_point = current_point
#     current_point = (previous_point[0] + initial_direction[0], previous_point[1] + initial_direction[1])
    
#     current_distance = 1
#     while map[current_point[0]][current_point[1]] != '.' and map[current_point[0]][current_point[1]] != 'S':
#         current_distance += 1
#         for direction in directions[map[current_point[0]][current_point[1]]]:
#             new_point = (current_point[0] + direction[0], current_point[1] + direction[1])
#             if new_point != previous_point:
#                 max_distance = max(max_distance, current_distance)
#                 next_point = new_point
#         previous_point = current_point
#         current_point = next_point

# print(max_distance//2)

## Part 2
current_point = start
pipes = [start]
for initial_direction in directions['S']:
    previous_point = current_point
    current_point = (previous_point[0] + initial_direction[0], previous_point[1] + initial_direction[1])
    
    while map[current_point[0]][current_point[1]] != '.' and map[current_point[0]][current_point[1]] != 'S' and map[current_point[0]][current_point[1]] != 'X':
        for direction in directions[map[current_point[0]][current_point[1]]]:
            new_point = (current_point[0] + direction[0], current_point[1] + direction[1])
            if new_point != previous_point:
                pipes.append(new_point)
                next_point = new_point
        previous_point = current_point
        current_point = next_point
    
    if map[current_point[0]][current_point[1]] == 'S':
        break
pipes = pipes[:-1]

# DIRECTIONS = ((-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
# surrounded = []

# valid_index = lambda row, column: 0 <= row <= len(map) - 1 and 0 <= column <= len(map[0]) - 1

# def check_surroundings(i, j):
#     direction_count = 0
#     for direction in DIRECTIONS:
#         multiplier = 1
#         while True:
#             new_i = i + multiplier * direction[0]
#             new_j = j + multiplier * direction[1]
#             if not valid_index(new_i, new_j):
#                 return False
#             if (new_i, new_j) in pipes:
#                 direction_count += 1
#                 break
#             multiplier += 1
#     if direction_count == 8:
#         print(i, j)
#         return True

# for i in range(len(map)):
#     for j in range(len(map[i])):
#         if (i, j) not in pipes:
#             if check_surroundings(i, j):
#                 surrounded.append((i, j))

# print(len(surrounded))