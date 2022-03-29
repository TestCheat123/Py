words = input()
res = sorted(words.split(), key=str.lower)
print(' '.join(res))
