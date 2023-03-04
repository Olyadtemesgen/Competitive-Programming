class MyCircularDeque:

    def __init__(self, k):

        self.k = k
        self.deque = [None] * self.k
        self.pointer_front = 0
        self.pointer_last = 0
        
    def insertFront(self, value: int) -> bool:
        
        if not self.isFull():

            self.deque[self.pointer_front] = value
            self.pointer_front = (self.pointer_front + 1) % self.k
            print(self.deque)
            return True
        
        else:
            return False

    def insertLast(self, value: int) -> bool:
        
        if not self.isFull():
            if self.isEmpty():
                
                self.deque[self.pointer_last] = value
                self.pointer_front = (self.pointer_front + 1) % self.k
                return True
            
            else:
                self.pointer_last = (self.pointer_last - 1) % self.k
                self.deque[self.pointer_last] = value
                return True
        
        else:
            return False
        
    def deleteFront(self) -> bool:

        if not self.isEmpty():
            self.pointer_front = (self.pointer_front - 1) % self.k
            self.deque[self.pointer_front] = None
            return True
        
        else:
            return False
        
    def deleteLast(self) -> bool:

        if not self.isEmpty():
            
            self.deque[self.pointer_last] = None
            self.pointer_last = (self.pointer_last + 1) % self.k
            return True

        return False

    def getFront(self) -> int:
        
        if not self.isEmpty():
            return self.deque[(self.pointer_front - 1) % self.k]
        
        return -1
    
    def getRear(self) -> int:
        
        if not self.isEmpty():
            return self.deque[self.pointer_last]
        
        return -1
        
    def isEmpty(self) -> bool:
        return self.deque[self.pointer_last] == None

    def isFull(self) -> bool:
        return (self.pointer_front == self.pointer_last \
        or self.pointer_front + self.k == self.pointer_last \
        or self.pointer_front == self.pointer_last + self.k ) and self.deque[self.pointer_front]