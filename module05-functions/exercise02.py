def fun(n):
    series = []
    while n > 1 and not series.count(n) > 0:
        print(f"fun(): {n}")
        series.append(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    series.append(n)
    return series


for number in fun(512_977):
    print(f"number: {number}")
