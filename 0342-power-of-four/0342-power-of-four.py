class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n == 4 or n == 1:
            return True
        
        elif n % 4 or n <= 0:
            return False
        
        else:
            return self.isPowerOfFour(n / 4)
    
    def isPowerOfFour1(self, n: int) -> bool:
        
        if n == 1:
            return True
        elif n <= 0:
            return False
        
        while not n % 4 and n != 4:
            n /= 4
        
        return not n % 4
    
    def isPowerOfFour(self, n: int) -> bool:
        
        starting = 1
        if n <= 0:
            return False
        
        while starting < n:
            starting *= 4
        
        return starting == n