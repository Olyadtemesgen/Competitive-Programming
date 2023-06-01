class Solution:
    
    def __init__(self):
        self.memoization = {}
    
    def fib(self, n: int) -> int:
        
        if n in self.memoization:
            return self.memoization
        
        if n <= 1:
            return n
        
        return self.fib(n - 1) + self.fib(n - 2)