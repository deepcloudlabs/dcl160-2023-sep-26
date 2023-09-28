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


print(evaluate_move(456, 549))
print(evaluate_move(549, 549))
print(evaluate_move(954, 549))
print(evaluate_move(123, 549))
