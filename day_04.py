parsed_input = []
total_points = 0

with open(r"Advent of Code 2023/inputs/day_04.txt",'r') as input_file:
    for line in input_file:
        split_on_colon = line.strip().split(":")
        all_numbers = split_on_colon[1].split("|")
        winning_numbers = [int(i) for i in all_numbers[0].split()]
        our_numbers = [int(i) for i in all_numbers[1].split()]
        parsed_input.append((winning_numbers, our_numbers))

## Part 1
def card_scorer(winning_numbers, our_numbers):
    point_multiplier = 0
    number_of_matches = 0
    for number in our_numbers:
        if number in winning_numbers:
            point_multiplier *= 2
            point_multiplier = 1 if point_multiplier == 0 else point_multiplier
            number_of_matches += 1
    return (number_of_matches, point_multiplier)

game_points = {}

for game_number in range(0, len(parsed_input)):
    current_points = card_scorer(*parsed_input[game_number])
    total_points += current_points[1]
    game_points[game_number] = current_points

print(total_points)

## Part 2
total_number_of_cards = 0
card_indices = [1 for i in range(0, 205)]

for current_game in range(0, len(card_indices)):
    number_of_matches = game_points[current_game][0]
    for i in range(current_game + 1, current_game + number_of_matches + 1):
        card_indices[i] += card_indices[current_game]

for number_of_each_card in card_indices:
    total_number_of_cards += number_of_each_card

print(total_number_of_cards)