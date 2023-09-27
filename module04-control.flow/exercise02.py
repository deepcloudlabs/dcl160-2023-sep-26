user_input = input("enter an integer: ")
print(type(user_input))
number = int(user_input)
print(type(number))
if number < 0:
    print(f"{number} is a negative integer.")
elif number > 0:
    print(f"{number} is a positive integer.")
else:
    print(f"{number} is zero.")
if number % 2 == 1:
    print(f"{number} is an odd integer.")
else:
    print(f"{number} is an even integer.")
