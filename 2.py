class Balance:
    
    def __init__(self):
        self.balance = 0
        
    def add_right(self, weight=1):
        self.balance += weight
        
    def add_left(self, weight=-1):
        self.balance -= weight
        
    def result(self):
        if self.balance == 0:
            return print('=')
        elif self.balance > 0:
            return print('R')
        else:
            return print('L')
        
        
balance = Balance()
balance.add_right(10)
balance.add_left(7)
balance.add_right(4)
balance.result()
