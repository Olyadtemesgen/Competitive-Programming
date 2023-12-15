class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.number = [0] * size
        self.flp= False
        self.number_1 = 0

    def fix(self, idx: int) -> None:
        
        if self.flp:
            if self.number[idx]:
                self.number_1 += 1
                self.number[idx] = 0
        
        else:
            if not self.number[idx]:
                self.number_1 += 1
                self.number[idx] = 1

    def unfix(self, idx: int) -> None:

        if self.flp:
            if not self.number[idx]:
                self.number_1 -= 1
                self.number[idx] = 1
        
        else:
            if self.number[idx]:
                self.number_1 -= 1
                self.number[idx] = 0

    def flip(self) -> None:
        self.flp = not self.flp
        self.number_1 = self.size - self.number_1

    def all(self) -> bool:    
        return self.number_1 == self.size
        
        

    def one(self) -> bool:
        return self.number_1
        


    def count(self) -> int:
        return self.number_1
        

    def toString(self) -> str:

        num = self.number.copy()
        if self.flp:
            for ind in range(self.size):
                num[ind] = 1 - self.number[ind]
        
        string = "".join(list(map(str, num)))
        return string


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()