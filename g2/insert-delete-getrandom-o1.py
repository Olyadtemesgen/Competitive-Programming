class RandomizedSet:

    def __init__(self):
        self.set = defaultdict(int)
        self.arr = []
        self.indices = defaultdict(list)

    def insert(self, val: int) -> bool:

        if self.set[val]:
            return False
        
        self.arr.append(val)
        self.indices[val].append(len(self.arr) - 1)
        self.set[val] = 1
        return True

    def remove(self, val: int) -> bool:

        if not self.set[val]:
            return False
        # print(self.arr)
        # print(self.indices)
        self.arr[self.indices[val][-1]] = self.arr[-1]
        self.indices[self.arr[-1]][0] = self.indices[val][-1]
        self.indices[val].pop()

        self.arr.pop()
        self.set[val] = 0
        return True

    def getRandom(self) -> int:
        
        # print(self.arr)
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()