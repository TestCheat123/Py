words = input()
res = map(int, sorted(words.split()))
res = sorted(res, key=abs)

print(' '.join(map(str, res)))
