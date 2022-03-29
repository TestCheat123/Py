a = [i for i in range(1, 10)]
res = map(lambda x: x / 2, a)
res_2 = [i / 2 for i in a]

print(list(res))

