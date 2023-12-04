parsed_input = {}

with open(r"Advent of Code 2023/inputs/day_02.txt",'r') as input_file:
    for line in input_file:
        split_on_colon = line.strip().split(":")
        cubes = split_on_colon[1].split(";")
        game_count = {}
        for i in cubes:
            individual_cubes = [j.strip() for j in i.split(',')]
            for k in individual_cubes:
                num_color = k.split()
                if num_color[1] not in game_count:
                    game_count[num_color[1]] = 0
                game_count[num_color[1]] = max(game_count[num_color[1]], int(num_color[0]))
        parsed_input[int(split_on_colon[0].split()[1])] = (game_count['red'], game_count['green'], game_count['blue'])

## Part 1
# id_sum = 0
# actual_game_count = (12, 13, 14)

# for key, value in parsed_input.items():
#     print(key, value, end = ' ')
#     if all(map(lambda i, j: i <= j, value, actual_game_count)):
#         print(True)
#         id_sum += key
#     else:
#         print()

# print(id_sum)

# Part 2
power = 0

for key, value in parsed_input.items():
    power += value[0] * value[1] * value[2]

print(power)