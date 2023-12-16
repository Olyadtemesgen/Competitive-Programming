class ATM:

    def __init__(self):
        self.value_ind = {20:0, 50:1, 100:2, 200:3, 500:4}
        self.values = [20, 50, 100, 200, 500]
        
        self.value_count = {_:0 for _ in self.values}

    def deposit(self, banknotesCount: List[int]) -> None:
        for c, val in zip(banknotesCount, self.values):
            self.value_count[val] += c

    def withdraw(self, amount: int) -> List[int]:
        value_count = self.value_count.copy()
        withdraw_count = {_:0 for _ in self.values}
        while True:
            # get all bills with values <= amount
            values = [v for v, c in value_count.items() if c > 0 and v <= amount]
            if not values:
                if amount == 0:
                    self.value_count = value_count.copy()
                    return [withdraw_count[v] for v in self.values]
                return [-1]
            value_max = max(values)
            while value_count[value_max] > 0 and amount >= value_max:
                cnt = min(value_count[value_max], amount // value_max)
                value_count[value_max] -= cnt
                withdraw_count[value_max] += cnt
                amount -= value_max * cnt

        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)