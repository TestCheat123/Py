def factorials(n):
    a, b = 0, 1
    for i in range(2, n + 2):
        a, b = b, b * i
        yield a


print(list(factorials(int(input()))))
