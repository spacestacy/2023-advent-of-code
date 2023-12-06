## Brute force
## Why the heck did I waste my time on this?
# all_encompassing_map = {"seed-to-soil": {},
#                         "soil-to-fertilizer": {},
#                         "fertilizer-to-water": {},
#                         "water-to-light": {},
#                         "light-to-temperature": {},
#                         "temperature-to-humidity": {},
#                         "humidity-to-location": {},
# }
# 
# input_seed = None
# current_dict = None
# location_numbers = []
# 
# with open(r"Advent of Code 2023/inputs/day_05.txt",'r') as input_file:
#     input_seed = [int(i) for i in input_file.readline().split(':')[1].strip().split()]
#     for line in input_file:
#         if len(line) == 1:
#             continue
#         if 'map' in line:
#             current_dict = line.split()[0]
#             continue
#         destination_start, source_start, value_range = (int(i) for i in line.split())
#         for i in range(0, value_range, 1):
#             all_encompassing_map[current_dict][source_start + i] = destination_start + i
# 
#     for seed in input_seed:
#         soil = all_encompassing_map['seed-to-soil'][seed] if seed in all_encompassing_map['seed-to-soil'] else seed
#         fertilizer = all_encompassing_map['soil-to-fertilizer'][soil] if soil in all_encompassing_map['soil-to-fertilizer'] else soil
#         water = all_encompassing_map['fertilizer-to-water'][fertilizer] if fertilizer in all_encompassing_map['fertilizer-to-water'] else fertilizer
#         light = all_encompassing_map['water-to-light'][water] if water in all_encompassing_map['water-to-light'] else water
#         temperature = all_encompassing_map['light-to-temperature'][light] if light in all_encompassing_map['light-to-temperature'] else light
#         humidity = all_encompassing_map['temperature-to-humidity'][temperature] if temperature in all_encompassing_map['temperature-to-humidity'] else temperature
#         location_numbers.append(all_encompassing_map['humidity-to-location'][humidity] if humidity in all_encompassing_map['humidity-to-location'] else humidity)
    
#     print(min(location_numbers))
#     print(all_encompassing_map)

all_encompassing_map = [[] for _ in range(7)]

input_seed = None
location_number = float('inf')
current_map = -1

with open(r"Advent of Code 2023/inputs/day_05.txt",'r') as input_file:
    input_seed = [int(i) for i in input_file.readline().split(':')[1].strip().split()]
    
    for line in input_file:
        if len(line) == 1:
            continue
        if 'map' in line:
            current_map += 1
            continue
        all_encompassing_map[current_map].append([int(i) for i in line.split()])

## Part 1
def convert_next(number, conversion_map):
    for destination_start, source_start, value_range in conversion_map:
        if source_start <= number < source_start + value_range:
            return destination_start + (number - source_start)
    
    return number

for seed in input_seed:
    let_the_mapping_begin = seed
    
    for current_map in all_encompassing_map:
        let_the_mapping_begin = convert_next(let_the_mapping_begin, current_map)
    
    if let_the_mapping_begin < location_number:
        location_number = let_the_mapping_begin

print(location_number)

## Part 2
## I had to refer to this implementation: https://www.youtube.com/watch?v=iqTopXV13LE.
## I could not implement it myself. I understood the implemenation in the video and attempted its implementation.
location_number = []
input_seed = list(zip(input_seed[::2], input_seed[1::2]))

def convert_next(number_range, conversion_map):
    converted_range = []
    
    for destination_start, source_start, value_range in conversion_map:
        intermediate_number_range = []
        source_end = source_start + value_range
        
        while number_range:
            range_start, range_end = number_range.pop()
            
            first_split = (range_start, min(source_start, range_end))
            second_split = (max(range_start, source_start), min(source_end, range_end))
            third_split = (max(range_start, source_end), range_end)
            
            if first_split[1] > first_split[0]:
                intermediate_number_range.append(first_split)
            if second_split[1] > second_split[0]:
                converted_range.append((second_split[0] - source_start + destination_start, second_split[1] - source_start + destination_start))
            if third_split[1] > third_split[0]:
                intermediate_number_range.append(third_split)
        
        number_range = intermediate_number_range
        
    return converted_range + number_range

for input_seed_pairs in input_seed:
    current_seed_range = [(input_seed_pairs[0], input_seed_pairs[0] + input_seed_pairs[1])]
    
    for conversion_map in all_encompassing_map:
        current_seed_range = convert_next(current_seed_range, conversion_map)
    
    location_number.append(min(current_seed_range)[0])

print(min(location_number))