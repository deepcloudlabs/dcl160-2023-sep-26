"""
if n is odd then next=3n+1
otherwise next=n/2
7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
13:55
"""
longest_series = []
for number in range(7, 1_000_000):
    n = number
    series = []
    while n > 1 and not series.count(n) > 0:
        series.append(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    series.append(n)
    if len(longest_series) < len(series):
        longest_series = series
        print(f"{longest_series[0]}, {len(longest_series)}, {longest_series[-1]}")
