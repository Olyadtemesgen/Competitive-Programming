class MyQueue:

    def __init__(self):
        self.Stack1 = []
        self.Stack2 = []

    def push(self, x: int) -> None:
        while self.Stack1:
            self.Stack2.append(self.Stack1.pop())
        self.Stack1.append(x)
        while self.Stack2:
            self.Stack1.append(self.Stack2.pop())
    def pop(self) -> int:
        return self.Stack1.pop()
    def peek(self) -> int:
        return self.Stack1[-1]
    def empty(self) -> bool:
        return not self.Stack1
#Or the other way we can make ADT for ourselves is
class MyQueue2:

    def __init__(self):
        self.Queue = []

    def push(self, x: int) -> None:
        self.Queue.append(x)

    def pop(self) -> int:
        return self.Queue.pop(0)
    def peek(self) -> int:
        return self.Queue[0]
    def empty(self) -> bool:
        return not self.Queue
