from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd -> cube -> sum
total: int = 0
for number in numbers:
    if number % 2 == 1:
        cubed: int = number ** 3
        total += cubed
print(f"[imperative] total: {total}")

total = reduce(lambda x, y: x + y, map(lambda u: u ** 3, filter(lambda n: n % 2 == 1, numbers)))
print(f"[functional] total: {total}")

count: int = reduce(lambda x, acc: x + acc, map(lambda n: 1, numbers))
min_value: int = reduce(lambda x, m: x if x < m else m, numbers)
max_value: int = reduce(lambda x, m: x if x > m else m, numbers)
print(count)
print(min_value)
print(max_value)
