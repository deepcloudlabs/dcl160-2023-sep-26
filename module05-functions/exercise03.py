# generator function
def fun(n):
    while n > 1:
        print(f"fun(): {n}")
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        yield n
    yield n

for number in fun(512_977):
    print(f"number: {number}")
