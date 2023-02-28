class Solution:
    def fib(self, n: int) -> int:
        
        memory = {0: 0, 1: 1}
        
        if n in memory:
            
            memory[n + 1] = memory.get(n - 1, 0) + memory[n]
            return memory[n]
        
        else:
            return self.fib(n - 1) + self.fib(n - 2)