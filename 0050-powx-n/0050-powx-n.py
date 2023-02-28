class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        
        if not n % 2:
            
            x *= x
            n //= 2

        return 1 / self.myPow(x, -n) if n < 0 else x * self.myPow(x, n - 1)