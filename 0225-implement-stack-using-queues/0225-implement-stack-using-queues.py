class MyStack:
    from collections import deque
    def __init__(self):
        self.queue = deque([])

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        
        length = len(self.queue)
        
        if length:
            
            while length - 1:
                self.queue.append(self.queue.popleft())
                length -= 1
            
            return self.queue.popleft()

    def top(self) -> int:
        
        if self.queue:
            return self.queue[-1]

    def empty(self) -> bool:
        
        if self.queue:
            return False
        
        return True
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()