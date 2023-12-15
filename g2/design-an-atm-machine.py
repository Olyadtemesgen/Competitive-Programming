class ATM:

    def __init__(self):
        self.numbers = defaultdict(int)
        self.keys = {1: 20, 2: 50, 3: 100, 4: 200, 5: 500}

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.numbers[i + 1] += banknotesCount[i]        

    def withdraw(self, amount: int) -> List[int]:
        keyss = defaultdict(int)
        temp_key = self.numbers.copy()

        for money in range(5, 0, -1):
            
            if self.numbers[money]:

                multipliers = amount // self.keys[money]
                if multipliers:
                    minimum = min(self.numbers[money], multipliers)
                    amount -= minimum * self.keys[money]
                    self.numbers[money] -= minimum
                    keyss[money] = minimum
            
            if not amount:
                break
        
        if amount:
            self.numbers = temp_key
            return [-1]
            
        
        answer = [0] * 5

        for ky in keyss:
            answer[ky - 1] = keyss[ky]
        
        return answer

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)