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


def evaluate_move(guess, secret):
    guess_as_str = str(guess)
    secret_as_str = str(secret)
    perfect_match = 0
    partial_match = 0
    for i, digit_guess in enumerate(guess_as_str):
        for j, digit_secret in enumerate(secret_as_str):
            if digit_guess == digit_secret:
                if i == j:
                    perfect_match += 1
                else:
                    partial_match += 1
    return partial_match, perfect_match, create_message(partial_match, perfect_match)


def create_message(partial_match: int, perfect_match: int) -> str:
    message: str = ""
    if perfect_match == 0 and partial_match == 0:
        message = "No match"
    else:
        if partial_match > 0:
            message = f"-{partial_match}"
        if perfect_match > 0:
            message = f"{message}+{perfect_match}"
    return message


def play(game_state):
    while True:
        guess = int(input("Enter your guess: "))
        secret = game_state["secret"]
        # (1,2,"-1+2")
        # (0,0,"No match")
        # (0,3,"+3")
        evaluation = evaluate_move(guess, secret)
        if evaluation[1] == game_state["level"]:
            player_wins(game_state)
            if game_state["level"] > 10:
                print("You win!")
                break
        else:
            print(evaluation[2])
            game_state["moves"] += 1
            if game_state["moves"] >= game_state["max_num_of_moves"]:
                player_loses(game_state)
