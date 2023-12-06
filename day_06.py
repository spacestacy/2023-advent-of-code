import math

## Part 1
# with open(r"Advent of Code 2023/inputs/day_06.txt",'r') as input_file:
#     line_1 = input_file.readline()
#     time = [int(i) for i in line_1.split(':')[1].strip().split()]
#     line_2 = input_file.readline()
#     distance = [int(i) for i in line_2.split(':')[1].strip().split()]

# def calc_speed(time):
#     return time

# final_ways = 1
# for i in range(len(time)):
    
#     ways = 0
    
#     for t in range(0, time[i] + 1):
#         speed = t
#         possible_distance = (time[i] - t) * speed
#         if possible_distance > distance[i]:
#             ways += 1
    
#     if ways != 0:
#         final_ways *= ways
    
# print(final_ways)

## Part 2
with open(r"Advent of Code 2023/inputs/day_06.txt",'r') as input_file:
    line_1 = input_file.readline()
    time = int(''.join(line_1.split(':')[1].strip().split()))
    line_2 = input_file.readline()
    distance = int(''.join(line_2.split(':')[1].strip().split()))

ways = 0

# Naive solution
for t in range(0, time + 1):
    possible_distance = (time - t) * t
    if possible_distance > distance:
        ways += 1
print('Ways:', ways)

# Efficient solution
# Treat the above equation (distance = (time - t) * t) as a quadratic inequality to be solved, find the two solutions which will form the bounds of the parabola, which on subtraction will yield the number of intergral values that will satisfy the inequality.
def evaluate_race(time, distance):
    x1 = math.floor((0.5 * (time - math.sqrt(time * time - 4 * distance)) + 1.0 ))
    x2 = math.floor((0.5 * (time + math.sqrt(time * time - 4 * distance)) - 1.0 ))
    return x1, x2

x1, x2 = evaluate_race(time, distance)
print('Ways:', x2 - x1 + 1)