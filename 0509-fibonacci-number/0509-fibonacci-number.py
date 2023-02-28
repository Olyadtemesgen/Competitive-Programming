class Solution:
    def fib(self, n: int) -> int:
        
        memory = {0: 0, 1: 1}
        
        if n in memory:
            return memory[n]
        
        else:
            memory[n + 1] = memory.get(n - 1, 0) + memory.get(n , 0)
            return self.fib(n - 1) + self.fib(n - 2)