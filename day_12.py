records = None

with open(r"Advent of Code/2023/spacestacy/inputs/day_12.txt",'r') as input_file:
    records = input_file.readlines()
    records = [i.strip().split() for i in records]
    #records = [i.split() for i in records]

# def find_damaged_configuration(piece):
#     configuration = []
#     current_count = 0
#     for i in piece:
#         if i == '?':
#             configuration.append('?')
#             if current_count != 0:
#                 configuration.append(current_count)
#                 current_count = 0
#         else:
#             current_count += 1
#     if current_count != 0:
#         configuration.append(current_count)
#     # if '#' not in piece:
#     #     return
#     # for i in piece+' ':
#     #     if i != '#':
#     #         if i == '?':
#     #             configuration.append(i)
#     #         else:
#     #             configuration.append(current_count)
#     #         current_count = 0
#     #     else:
#     #         current_count += 1
#     return configuration

# def find_current_damaged_configuration(pieces):
#     configuration = []
#     for piece in pieces:
#         configuration.append(find_damaged_configuration(piece))
#     return configuration

# for record in records:
#     pieces = [i for i in record[0].split('.') if i]
#     groups = [int(i) for i in record[1].split(',')]

#     current_damaged = find_current_damaged_configuration(pieces)

#     for group in groups:
#         for c in current_damaged:
#             if 

#     print(current_damaged, pieces, groups)

# import sys
# import re
# from copy import deepcopy
# from math import gcd
# from collections import defaultdict, Counter, deque
# D = open(r"Advent of Code/2023/spacestacy/inputs/day_12.txt").read().strip()
# L = D.split('\n')
# G = [[c for c in row] for row in L]

# # i == current position within dots
# # bi == current position within blocks
# # current == length of current block of '#'
# # state space is len(dots) * len(blocks) * len(dots)
# DP = {}
# def f(dots, blocks, i, bi, current):
#   key = (i, bi, current)
#   if key in DP:
#     return DP[key]
#   if i==len(dots):
#     if bi==len(blocks) and current==0:
#       return 1
#     elif bi==len(blocks)-1 and blocks[bi]==current:
#       return 1
#     else:
#       return 0
#   ans = 0
#   for c in ['.', '#']:
#     if dots[i]==c or dots[i]=='?':
#       if c=='.' and current==0:
#         ans += f(dots, blocks, i+1, bi, 0)
#       elif c=='.' and current>0 and bi<len(blocks) and blocks[bi]==current:
#         ans += f(dots, blocks, i+1, bi+1, 0)
#       elif c=='#':
#         ans += f(dots, blocks, i+1, bi, current+1)
#   DP[key] = ans
#   return ans

# for part2 in [False,True]:
#   ans = 0
#   for line in L:
#     dots,blocks = line.split()
#     if part2:
#       dots = '?'.join([dots, dots, dots, dots, dots])
#       blocks = ','.join([blocks, blocks, blocks, blocks, blocks])
#     blocks = [int(x) for x in blocks.split(',')]
#     DP.clear()
#     print(dots, blocks)
#     score = f(dots, blocks, 0, 0, 0)
#     #print(dots, blocks, score, len(DP))
#     ans += score
#   print(ans)

import functools

@functools.cache
def count_matches(pattern, size, splits):
    if len(splits) == 0:
        if all(c in '.?' for c in pattern):
            return 1
        return 0

    a = splits[0]
    rest = splits[1:]
    after = sum(rest) + len(rest)

    count = 0

    for before in range(size-after-a+1):
        cand = '.' * before + '#' * a + '.'
        if all(c0 == c1 or c0=='?' for c0,c1 in zip(pattern, cand)):
            print(list(zip(pattern, cand)))
            count += count_matches(pattern[len(cand):], size-a-before-1, rest)

    return count

def solve(s, copies=1):
    answer = 0

    for line in s.splitlines():
        pattern, splits = line.split()
        pattern = '?'.join((pattern,) * copies)
        splits = tuple(map(int, splits.split(','))) * copies
        print(pattern, tuple(splits))
        answer += count_matches(pattern, len(pattern), tuple(splits))

    return answer

def part1(s):
    answer = solve(s)
    print(answer)

def part2(s):
    answer = solve(s, copies=5)
    print(answer)

INPUT = open(r"Advent of Code/2023/spacestacy/inputs/day_12.txt").read()
part1(INPUT)
part2(INPUT)