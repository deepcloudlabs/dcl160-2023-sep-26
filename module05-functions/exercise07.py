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


def get_random_digit(lower_bound: int, upper_bound: int) -> int:
    return randint(lower_bound, upper_bound)


def create_secret(game_level: int) -> int:
    digits = [get_random_digit(1, 9)]
    while len(digits) < game_level:
        digit = get_random_digit(0, 9)
        if not digit in digits:
            digits.append(digit)
    secret_number = int("".join([str(digit) for digit in digits]))
    print(secret_number)
    return secret_number


game = {
    "level": 3,
    "secret": create_secret(3),
    "lives": 3,
    "moves": 0,
    "max_num_of_moves": 10
}


def evaluate_move(guess: int, secret: int) -> tuple[int, int, str]:
    guess_as_str: str = str(guess)
    secret_as_str: str = str(secret)
    perfect_match: int = 0
    partial_match: int = 0
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


def player_wins(game_state):
    game_state["level"] += 1
    game_state["moves"] = 0
    game_state["max_num_of_moves"] += 2
    game_state["lives"] += 1
    game_state["secret"] = create_secret(game_state["level"])


def player_loses(game_state):
    game_state["moves"] = 0
    game_state["lives"] -= 1
    game_state["secret"] = create_secret(game_state["level"])


def print_game_status(game_state):
    print(
        f"level: {game_state['level']}, moves: {game_state['moves']} / {game_state['max_num_of_moves']}, lives: {game_state['lives']}")


def play(game_state):
    while True:
        print_game_status(game_state)
        guess: int = int(input("Enter your guess: "))
        secret: int = game_state["secret"]
        evaluation: tuple[int, int, str] = evaluate_move(guess, secret)
        if evaluation[1] == game_state["level"]:
            if game_state["level"] == 10:
                print("You win!")
                break
            player_wins(game_state)
        else:
            print(evaluation[2])
            game_state["moves"] += 1
            if game_state["moves"] >= game_state["max_num_of_moves"]:
                player_loses(game_state)
                if game_state["lives"] <= 0:
                    print("You lose!")
                    break


play(game)
