class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n == 4 or n == 1:
            return True
        
        elif n % 2 or n <= 0:
            return False
        
        else:
            return self.isPowerOfTwo(n / 2)