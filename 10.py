def same_by(characteristics, objects):
    for i in objects:
        if characteristics(i):
            return False

    return True


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
