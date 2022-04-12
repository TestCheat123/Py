class SparseArray:
    
    def __init__(self):
        self.array = dict()
        
    def __getitem__(self, key):
        return self.array.get(key, 0)
        
    def __setitem__(self, key, value):
        self.array[key] = value
        
        
arr = SparseArray()
arr[1] = 10
arr[8] = 20
for i in range(10):
    print('arr[{}] = {}'.format(i, arr[i]))
