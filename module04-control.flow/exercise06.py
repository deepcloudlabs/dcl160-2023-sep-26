numbers = [4, 8, None, 15, None, None, 16, None, 23, None, 42, None, None]
series = []
# how
for number in numbers:  # regular, external loop
    if number is not None:
        series.append(number)
print(series)
