from functools import cmp_to_key

## Part 1
# hands_with_bid = []
# card_letter_map = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}

# def convert_hand_to_ints(hand):
#     converted_hand = []
#     for i in hand:
#         if i.isnumeric():
#             converted_hand.append(int(i))
#         else:
#             converted_hand.append(card_letter_map[i])
#     return converted_hand

# with open(r"Advent of Code 2023/inputs/day_07.txt",'r') as input_file:
#     for line in input_file:
#         hand, bid = line.split()
#         hands_with_bid.append([convert_hand_to_ints(hand), int(bid)]) 

# def card_count_helper(hand):
#     hand_count = {}
#     for i in hand:
#         if i not in hand_count:
#             hand_count[i] = 1
#         else:
#             hand_count[i] += 1
#     return hand_count

# def determine_append_rank(hands_with_bid):
#     types = [[] for i in range(7)]
    
#     for i in range(0, len(hands_with_bid)):
#         hand_count = card_count_helper(hands_with_bid[i][0])
#         hand_count_values = list(hand_count.values())
#         if 5 in hand_count_values:
#             types[6].append(hands_with_bid[i])
#         elif 4 in hand_count_values:
#             types[5].append(hands_with_bid[i])
#         elif 3 in hand_count_values:
#             if 2 in hand_count_values:
#                 types[4].append(hands_with_bid[i])
#             else:
#                 types[3].append(hands_with_bid[i])
#         elif 2 in hand_count_values:
#             if hand_count_values.count(2) == 2:
#                 types[2].append(hands_with_bid[i])
#             else:
#                 types[1].append(hands_with_bid[i])
#         else:
#             types[0].append(hands_with_bid[i])
    
#     return types

# def compare(item1, item2):
#     for i in range(0, len(item1[0])):
#         if item1[0][i] < item2[0][i]:
#             return -1
#         elif item1[0][i] > item2[0][i]:
#             return 1

# types = determine_append_rank(hands_with_bid)
# for i in types:
#     i.sort(key = cmp_to_key(compare))

# winnings = 0
# rank = 1
# for i in types:
#     for j in i:
#         winnings += rank * j[1]
#         rank += 1
    
# print(winnings)

## Part 2
hands_with_bid = []
card_letter_map = {'A': 13, 'K': 12, 'Q': 11, 'J': 1, 'T': 10}

def convert_hand_to_ints(hand):
    converted_hand = []
    for i in hand:
        if i.isnumeric():
            converted_hand.append(int(i))
        else:
            converted_hand.append(card_letter_map[i])
    return converted_hand

with open(r"Advent of Code 2023/inputs/day_07.txt",'r') as input_file:
    for line in input_file:
        hand, bid = line.split()
        hands_with_bid.append([convert_hand_to_ints(hand), int(bid)]) 

def card_count_helper(hand):
    hand_count = {}
    for i in hand:
        if i not in hand_count:
            hand_count[i] = 1
        else:
            hand_count[i] += 1
    return hand_count

# This quintessential function stands to show what desperation does to a mediocre programmer.
# Using classes, and dealing with the joker case after running the code for part 1 will make this a whole lot easier.
def determine_append_rank(hands_with_bid):
    types = [[] for i in range(7)]
    
    for i in range(0, len(hands_with_bid)):
        hand_count = card_count_helper(hands_with_bid[i][0])
        num_jokers = hand_count[1] if 1 in hand_count else 0
        if num_jokers == 5:
            types[6].append(hands_with_bid[i])
            continue
        hand_count[1] = 0
        hand_count_values = list(hand_count.values())
        if 5 in hand_count_values:
            types[6].append(hands_with_bid[i])
        elif 4 in hand_count_values:
            types[5 + num_jokers].append(hands_with_bid[i])
        elif 3 in hand_count_values:
            if 2 in hand_count_values:
                types[4].append(hands_with_bid[i])
            else:
                if num_jokers == 0:
                    types[3].append(hands_with_bid[i])
                else:
                    types[3 + num_jokers + 1].append(hands_with_bid[i])
        elif 2 in hand_count_values:
            if hand_count_values.count(2) == 2:
                if num_jokers == 0:
                    types[2].append(hands_with_bid[i])
                else:
                    types[2 + num_jokers + 1].append(hands_with_bid[i])
            else:
                if num_jokers == 0:
                    types[1].append(hands_with_bid[i])
                elif num_jokers == 1:
                    types[1 + num_jokers + 1].append(hands_with_bid[i])
                else:
                    types[1 + num_jokers + 2].append(hands_with_bid[i])
        else:
            if num_jokers == 0:
                types[0].append(hands_with_bid[i])
            elif num_jokers == 1:
                types[1].append(hands_with_bid[i])
            elif num_jokers == 2:
                types[3].append(hands_with_bid[i])
            elif num_jokers == 3:
                types[5].append(hands_with_bid[i])
            elif num_jokers == 4:
                types[6].append(hands_with_bid[i])
    
    return types

def compare(item1, item2):
    for i in range(0, len(item1[0])):
        if item1[0][i] < item2[0][i]:
            return -1
        elif item1[0][i] > item2[0][i]:
            return 1

types = determine_append_rank(hands_with_bid)
for i in types:
    i.sort(key = cmp_to_key(compare))

winnings = 0
rank = 1
for i in types:
    for j in i:
        print(j[1])
        winnings += rank * j[1]
        rank += 1
    
print(winnings)