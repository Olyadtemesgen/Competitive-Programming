class StockSpanner:

    def __init__(self):
        
        self.stackvalue = []
        self.stackspan = []
        self.length = 0

    def next(self, price: int) -> int:
        
        while self.stackspan and  self.stackvalue[-1] <= price:
            self.stackspan.pop()
            self.stackvalue.pop()
        
        if not self.stackspan:
            
            self.stackspan.append(self.length)
            self.stackvalue.append(price)
            self.length += 1
            
            return self.length
        
        else:
            self.stackspan.append(self.length)
            self.stackvalue.append(price)
            self.length += 1
            return self.length - self.stackspan[-2] - 1
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)