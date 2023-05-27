class Solution:
    
    def tribonacci(self, n: int) -> int:
        
        dict = {0: 0 , 1:1, 2: 1}
        
        if n in dict:
            return dict[n]
        
        def uus(n):
            
            if n in dict:
                return dict[n]
            
            dict[n] = uus(n - 1) + uus(n - 2) + uus(n - 3)
            
            return dict[n]
    
        return uus(n)