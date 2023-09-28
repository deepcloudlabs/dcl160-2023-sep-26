"""
level : 3
lives : 3
max moves: 10
secret: 549
guess: 123 -> No match
       456 -> -2
       647 -> +1
       ...
       549 -> Wins -> level: 4 -> secret: 3615
"""
from random import randint


def get_random_digit(lower_bound, upper_bound):
    return randint(lower_bound, upper_bound)


def create_secret(game_level):
    digits = [get_random_digit(1, 9)]
    while len(digits) < game_level:
        digit = get_random_digit(0, 9)
        if not digit in digits:
            digits.append(digit)
    return int("".join([str(digit) for digit in digits]))


game = {
    "level": 3,
    "secret": create_secret(3),
    "lives": 3,
    "moves": 0,
    "max_num_of_moves": 10
}

print(game)
