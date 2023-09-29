from mastermind import create_secret


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
