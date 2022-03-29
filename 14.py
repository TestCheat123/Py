lst = [[23, 5], [0, 1], [1, 0], [3, 6], [6, 7], [2, -1], [2, 1]]
lst.sort(key=lambda lst: (lst[0] ** 2 + lst[1] ** 2) ** 0.5)
print(*lst)
