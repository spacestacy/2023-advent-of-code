from math import lcm

node_dict = {}

with open(r"Advent of Code\2023\spacestacy\inputs\day_08.txt",'r') as input_file:
    direction_instructions = input_file.readline().strip()
    input_file.readline()
    for line in input_file:
        node, destination_tuple = line.split('=')
        destination_tuple = tuple(destination_tuple[2:-2].split(', '))
        node_dict[node.strip()] = destination_tuple

## Part 1
# current_node = 'AAA'
# current_direction = 0
# steps = 0
# while current_node != 'ZZZ':
#     if current_direction == len(direction_instructions):
#         current_direction = 0
#     current_node = node_dict[current_node][0] if direction_instructions[current_direction] == 'L' else node_dict[current_node][1]
#     steps += 1
#     current_direction += 1

# print(steps)

## Part 2
end_nodes = []

for node in node_dict.keys():
    if node[-1] == 'A':
        end_nodes.append(node)
print(end_nodes)
def get_cycle_lengths(end_nodes):
    cycle_lenghts = []
    for node in end_nodes:
        current_direction = 0
        steps = 0
        while node[-1] != 'Z':
            if current_direction == len(direction_instructions):
                current_direction = 0
            node = node_dict[node][0] if direction_instructions[current_direction] == 'L' else node_dict[node][1]
            current_direction += 1
            steps += 1
        cycle_lenghts.append(steps)
    return cycle_lenghts

print(lcm(*get_cycle_lengths(end_nodes)))