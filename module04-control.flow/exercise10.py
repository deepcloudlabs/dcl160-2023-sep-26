"""
if n is odd then next=3n+1
otherwise next=n/2
7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
13:55
"""
number = int(input("enter a number:"))

series = []

while number > 1 and not series.count(number) > 0:
    series.append(number)
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1
series.append(number)
print(len(series))
print(series)
