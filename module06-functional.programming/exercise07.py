numbers = [41, 81, 15, 161, 23, 421]
print(f"Any odd number in numbers: {any(map(lambda n: n%2 == 1, numbers))}")
print(f"All are odd numbers in numbers: {all(map(lambda n: n%2 == 1, numbers))}")
