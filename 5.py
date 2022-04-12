class ReversedList:
    
    def __init__(self, lst):
        self.lst = lst
        
    def __len__(self):
        return len(self.lst)
        
    def __getitem__(self, key):
        return self.lst[len(self.lst) - key - 1]
        

r1 = ReversedList([10, 20, 30])
print(r1[0])
print(len(r1))
        