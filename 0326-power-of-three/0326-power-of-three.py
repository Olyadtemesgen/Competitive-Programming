class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1.0:
            return True
        
        elif n < 1.0 or n % 3:
            
            return False
        
        return self.isPowerOfThree(n / 3)