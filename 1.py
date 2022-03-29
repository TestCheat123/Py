a = [i for i in range(1, 10)]

res = filter(lambda x: x < 5, a)
res_2 = [i for i in a if i < 5]

print(list(res))

