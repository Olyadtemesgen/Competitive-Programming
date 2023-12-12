class OrderedStream:

    def __init__(self, n: int):

        self.n = n
        self.array = ["" for _ in range(n)]
        self.idx = 0

    def insert(self, idKey: int, value: str) -> List[str]:

        answer = []

        self.array[idKey - 1] = value

        while self.idx < self.n and self.array[self.idx]:
            answer.append(self.array[self.idx])
            self.idx += 1
        
        return answer

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)