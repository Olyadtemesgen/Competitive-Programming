class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n == 4 or n == 1:
            return True
        
        elif n % 4 or n == 0:
            return False
        
        else:
            return self.isPowerOfFour(n / 4)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     def isPowerOfFour(self, n: int) -> bool:
        
#         if n == 1:
#             return True
#         elif n == 0:
#             return False
        
#         while n % 4 or n == 4:
#             n /= 4
        
#         return not n % 4
    
    