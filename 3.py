a = [i for i in range(10, 100)]

res = filter((lambda x: x if x % 9 == 0 else None), a)
res = map(lambda x: x * x, res)
res = sum(res)

print(res)
