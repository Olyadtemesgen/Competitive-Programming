class MyCircularDeque:
    def __init__(self, k):
        self.k = k
        self.Deque = [None] * self.k

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            if self.Deque[0] is None:
                self.Deque[0] = value
            else:
                for x in range(self.Deque.index(None), 0,- 1):
                    self.Deque[x] = self.Deque[x - 1]
                self.Deque[0] = value
            return True
        else:
            return False
    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            if self.Deque[self.k - 1] is None:
                self.Deque[self.k - 1] = value
            else:
                for x in range(self.Deque.index(None),self.k - 1):
                    self.Deque[x] = self.Deque[x + 1]
                self.Deque[self.k - 1] = value
            return True
        else:
            return False
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        else:
            if self.isFull() or self.Deque[0] is not None:
                self.Deque[0] = None
            else:
                for x in self.Deque:
                    if x is not None:
                        self.Deque[self.Deque.index(x)] = None
                        break
            return True
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            if self.isFull():
                self.Deque[self.k - 1] = None
            elif self.Deque[self.k - 1] is not None:
                self.Deque[self.k - 1] = None
            else:
                self.Deque.reverse()
                for x in range(self.k):
                    if self.Deque[x] is not None:
                        self.Deque[x] = None
                        break
                self.Deque.reverse()
            return True
    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            value = None
            for x in self.Deque:
                if x is not None:
                    value = x
                    break
            return value
    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            vaa = None
            for abbb in list(reversed(self.Deque)):
                if abbb is not None:
                    vaa = abbb
                    break
            return vaa
    def isEmpty(self) -> bool:
        value = True
        for x in self.Deque:
            if x is not None:
                value = False
                break
        return value
    def printer(self):
        print(self.Deque)
    def isFull(self) -> bool:
        value = True
        for x in self.Deque:
            if x is None:
                value = False
                break
        return value
