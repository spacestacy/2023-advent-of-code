map = None

with open(r"Advent of Code\2023\spacestacy\inputs\day_11.txt",'r') as input_file:
    map = input_file.readlines()
    map = [list(i.strip()) for i in map]

## Part 1
# def check_column(column):
#     for row in range(len(map)):
#         if map[row][column] == "#":
#             return False
#     return True

# def expand_galaxy():
#     row = 0
#     column = 0
#     while True:
#         if '#' not in map[row]:
#             map.insert(row + 1, ['.' for i in range(len(map[row]))])
#             row += 1
#         row += 1
#         if row == len(map):
#             break
#     while True:
#         if check_column(column):
#             for row in range(len(map)):
#                 map[row].insert(column + 1, '.')
#             column += 1
#         column += 1
#         if column == len(map[0]):
#             break
            
# def locate_galaxies_and_create_pairs(map):
#     galaxies, galaxy_pairs = [], {}
    
#     for row in range(len(map)):
#         if '#' in map[row]:
#             for column in range(len(map[row])):
#                 if map[row][column] == '#':
#                     galaxies.append((row, column))
#     for galaxy in range(len(galaxies)):
#         for galaxy_pair in range(galaxy + 1, (len(galaxies))):
#             galaxy_pairs[(galaxies[galaxy], galaxies[galaxy_pair])] = 0
#     return galaxies, galaxy_pairs

# def find_min_distance(map, galaxy_pair):
#     min_distance = 0
    
#     galaxy_one = galaxy_pair[0]
#     galaxy_two = galaxy_pair[1]
    
#     min_distance = abs(galaxy_two[0] - galaxy_one[0]) + abs(galaxy_two[1] - galaxy_one[1])
    
#     return min_distance

# expand_galaxy()
# galaxies, galaxy_pairs = locate_galaxies_and_create_pairs(map)

# for galaxy_pair in galaxy_pairs:
#     galaxy_pairs[galaxy_pair] = find_min_distance(map, galaxy_pair)

# print(sum(galaxy_pairs.values()))

## Part 2
def check_column(column):
    for row in range(len(map)):
        if map[row][column] == '#':
            return False
    return True

def expand_galaxy():
    row = 0
    column = 0
    while True:
        if '#' not in map[row]:
            map.insert(row + 1, ['X' for i in range(len(map[row]))])
            row += 1
        row += 1
        if row == len(map):
            break
    while True:
        if check_column(column):
            for row in range(len(map)):
                map[row].insert(column + 1, 'Y')
            column += 1
        column += 1
        if column == len(map[0]):
            break
            
def locate_galaxies_and_create_pairs(map):
    galaxies, galaxy_pairs = [], {}
    
    for row in range(len(map)):
        if '#' in map[row]:
            for column in range(len(map[row])):
                if map[row][column] == '#':
                    galaxies.append((row, column))
    for galaxy in range(len(galaxies)):
        for galaxy_pair in range(galaxy + 1, (len(galaxies))):
            galaxy_pairs[(galaxies[galaxy], galaxies[galaxy_pair])] = 0
    return galaxies, galaxy_pairs

def find_number_of_expansions(map, row_range, column_range):
    expand_rows_by = 0
    expand_columns_by = 0
    
    for row in range(row_range[0], row_range[1]):
        if 'X' in map[row]:
            expand_rows_by += 1
            
    column_start = min(column_range[0], column_range[1])
    column_end = max(column_range[0], column_range[1])
    for column in range(column_start, column_end):
        for row in range(len(map)):
            if map[row][column] == 'Y':
                expand_columns_by += 1
                break
    
    return (expand_rows_by, expand_columns_by)        

def find_min_distance(map, galaxy_pair):
    min_distance = 0
    galaxy_multiplier = 100
    
    galaxy_one = galaxy_pair[0]
    galaxy_two = galaxy_pair[1]

    multiplier = find_number_of_expansions(map, (galaxy_one[0], galaxy_two[0]), (galaxy_one[1], galaxy_two[1]))
    min_distance = (abs(galaxy_two[0] - galaxy_one[0]) + multiplier[0] * (galaxy_multiplier - 2)) + (abs(galaxy_two[1] - galaxy_one[1]) + multiplier[1] * (galaxy_multiplier - 2))
    
    return min_distance

expand_galaxy()
galaxies, galaxy_pairs = locate_galaxies_and_create_pairs(map)

for galaxy_pair in galaxy_pairs:
    galaxy_pairs[galaxy_pair] = find_min_distance(map, galaxy_pair)

print(sum(galaxy_pairs.values()))