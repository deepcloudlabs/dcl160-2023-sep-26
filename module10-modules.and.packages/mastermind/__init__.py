from mastermind.utility import create_secret

game = {
    "level": 3,
    "secret": create_secret(3),
    "lives": 3,
    "moves": 0,
    "max_num_of_moves": 10
}

print("mastermind module is loaded!")