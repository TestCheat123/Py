class Selector():
    
    def __init__(self, values):
        self.numbers = values
        
    def get_odds(self):
        odds = filter(lambda x: x%2 != 0, self.numbers)
        return odds
    
    def get_evens(self):
        evens = filter(lambda x: x%2 == 0, self.numbers)
        return evens
        
        
values = [11, 12, 13, 14, 15, 16, 22, 44, 66]
selector = Selector(values)
odds = selector.get_odds()
evens = selector.get_evens()
print(' '.join(map(str, odds)))
print(' '.join(map(str, evens)))
