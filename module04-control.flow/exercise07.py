numbers = [4, 8, None, 15, None, None, 16, None, 23, None, 42, None, None]
while numbers.count(None) > 0:  # irregular loop
    numbers.remove(None)
print(numbers)
