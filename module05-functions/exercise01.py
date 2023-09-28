def fun(n):
    series = []
    while n > 1 and not series.count(n) > 0:
        series.append(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    series.append(n)
    return series[0], len(series), series[-1], series


def get_longest_series(lower_bound=7, upper_bound=100_000):
    solution = (1, 0, 1, [])
    for number in range(lower_bound, upper_bound):
        start, steps, stop, series = fun(number)
        if solution[1] < steps:
            solution = (start, steps, stop, series)
            print(f"start={start}, steps={steps}, stop={stop}")
            print(series[-6:-1])
    return solution


print(f"solution: {get_longest_series(upper_bound=10_000_000, lower_bound=1_000_000)}")
