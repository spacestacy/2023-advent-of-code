map = None

with open(r"Advent of Code\2023\spacestacy\inputs\day_13.txt",'r') as input_file:
    map = input_file.read()
    map = map[:-1].split('\n\n')
    map = [i.split('\n') for i in map]
    
def valid_index(position1, position2, length):
    if 0 <= position1 < length and 0 <= position2 < length:
        return True
    return False

def transpose(matrix):
    transposed = list(zip(*matrix))
    transposed = [''.join(i) for i in transposed]
    return transposed

def replace_char_at_index(input_string, index, replacement_char):
    if 0 <= index < len(input_string):
        # Construct the modified string with the replacement character
        modified_string = input_string[:index] + replacement_char + input_string[index + 1:]
        return modified_string
    else:
        print("Index out of range.")
        return input_string

## Part 1
def perfect_reflection(matches, segment):
    for match in matches:
        flag = True
        for index in range(0, len(segment) - 1):
            if valid_index(match - index, match + index + 1, len(segment)):
                if segment[match - index] != segment[match + index + 1]:
                    flag = False
                    break
            else:
                break
        if flag:
            return match + 1
    return False
    
def find_mirror_location(segment):
    
    matches = []
    
    for pattern_row in range(0, len(segment) - 1):
        if segment[pattern_row] == segment[pattern_row + 1]:
            matches.append(pattern_row)

    is_perfect_reflection = perfect_reflection(matches, segment)
    
    if is_perfect_reflection:
        return 100 * is_perfect_reflection
    else:
        matches = []
        segment = transpose(segment)
        for pattern_row in range(0, len(segment) - 1):
            if segment[pattern_row] == segment[pattern_row + 1]:
                matches.append(pattern_row)
        is_perfect_reflection = perfect_reflection(matches, segment)
        return is_perfect_reflection
    
total = 0
original_matches = []
for segment in range(0, len(map)):
    x = find_mirror_location(map[segment])
    original_matches.append(x)
    total += x
        
print(total)

## Part 2
def perfect_reflection(match, segment):
    flag = True
    for index in range(0, len(segment) - 1):
        if valid_index(match - index, match + index + 1, len(segment)):
            if segment[match - index] != segment[match + index + 1]:
                flag = False
                break
        else:
            break
    if flag:
        return match + 1
    return False

def find_mirror_location(segment, ignore_candidate):
    row_ignore = False
    if ignore_candidate >= 100:
        ignore_candidate /= 100
        ignore_candidate = int(ignore_candidate)
        row_ignore = True

    for row in range(0, len(segment) - 1):
        for index in range(0, len(segment[row])):
            is_perfect_reflection = False
            original = segment[row]
            segment[row] = replace_char_at_index(segment[row], index, '#' if segment[row][index] == '.' else '.')
            for pattern_row in range(0, len(segment) - 1):
                if row_ignore and pattern_row == ignore_candidate - 1:
                    continue
                if segment[pattern_row] == segment[pattern_row + 1]:
                    is_perfect_reflection = perfect_reflection(pattern_row, segment)
            if is_perfect_reflection:
                return 100 * is_perfect_reflection
            segment[row] = original
    
    segment = transpose(segment)
    for row in range(0, len(segment) - 1):
        for index in range(0, len(segment[row])):
            is_perfect_reflection = False
            original = segment[row]
            segment[row] = replace_char_at_index(segment[row], index, '#' if segment[row][index] == '.' else '.')
            for pattern_row in range(0, len(segment) - 1):
                if not row_ignore and pattern_row == ignore_candidate - 1:
                    continue
                if segment[pattern_row] == segment[pattern_row + 1]:
                    is_perfect_reflection = perfect_reflection(pattern_row, segment)
            if is_perfect_reflection:
                return is_perfect_reflection
            segment[row] = original

total = 0
for segment in range(0, len(map)):
    x = find_mirror_location(map[segment], original_matches[segment])
    total += x
        
print(total)

## Better implementation based on the find_differences() idea where we focus on the number of difference between rows/columns. Turns out, it will work. No need to brute force.
## Implementation: https://www.youtube.com/watch?v=KObhCimyl2I.
# import sys
# import re
# from copy import deepcopy
# from math import gcd
# from collections import defaultdict, Counter, deque
# D = open(r"Advent of Code\2023\spacestacy\inputs\day_13.txt").read().strip()
# L = D.split('\n')
# G = [[c for c in row] for row in L]
# for part2 in [False, True]:
#   num = -1
#   ans = 0
#   for grid in D.split('\n\n'):
#     num += 1
#     G = [[c for c in row] for row in grid.split('\n')]
#     print(G)
#     R = len(G)
#     C = len(G[0])
#     # vertical symmetry
#     for c in range(C-1):
#       badness = 0
#       for dc in range(C):
#         left = c-dc
#         right = c+1+dc
#         if 0<=left<right<C:
#           for r in range(R):
#             if G[r][left] != G[r][right]:
#               badness += 1
#       if badness == (1 if part2 else 0):
#         # print(num, c + 1)
#         ans += c+1
#     for r in range(R-1):
#       badness = 0
#       for dr in range(R):
#         up = r-dr
#         down = r+1+dr
#         if 0<=up<down<R:
#           for c in range(C):
#             if G[up][c] != G[down][c]:
#               badness += 1
#       if badness == (1 if part2 else 0):
#         # print(num, r + 1)
#         ans += 100*(r+1)
#   print(ans)