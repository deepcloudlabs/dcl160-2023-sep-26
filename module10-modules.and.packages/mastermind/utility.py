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
