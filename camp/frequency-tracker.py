class FrequencyTracker:

    def __init__(self):
        
        self.data = defaultdict(int)
        self.freq = defaultdict(int)

    def add(self, number: int) -> None:
       
        self.data[number] += 1  
        self.freq[self.data[number]] += 1

        if self.data[number] - 1:
            self.freq[self.data[number] - 1] -= 1
        
 
    def deleteOne(self, number: int) -> None:
        
        if self.data[number]:
            self.data[number] -= 1
            self.freq[self.data[number] + 1] -= 1

            if self.data[number]:
                self.freq[self.data[number]] += 1
    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency]


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)