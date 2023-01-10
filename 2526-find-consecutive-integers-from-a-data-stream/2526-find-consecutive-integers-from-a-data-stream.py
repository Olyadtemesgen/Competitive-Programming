class DataStream:

    def __init__(self, value: int, k: int):
        self.Stream = []
        self.value = value
        self.k = k
        self.vv = -1
    def consec(self, num: int) -> bool:
        self.Stream.append(num)
        
        if len(self.Stream) < self.k or num != self.value:
            if num != self.value:
                self.vv = len(self.Stream) - 1
            return False
        
        elif self.vv < len(self.Stream) - self.k:
            return True
        
        else:
            return False
            
        

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)