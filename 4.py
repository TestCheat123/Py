a = a = [i for i in range(1, 30)]

res = filter(lambda x: x > 17, a)
res = map(lambda x: x / 2, res)
res_2 = []

print(list(res))
