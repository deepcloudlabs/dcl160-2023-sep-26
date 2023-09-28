# 3716842
from functools import reduce

digits = [3, 7, 1, 6, 8, 4, 2]
number = reduce(lambda number, digit: 10 * number + digit, digits)
print(number)