def square_fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        yield a*a


print(list(square_fibonacci(int(input()))))
