class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        if n % 3:
            n -= 1
        
        if n % 3:
            return False

        while n > 1:

            if n % 3:
                n -= 1
            
            if n % 3:
                return False
            
            n //= 3
        
        return True
