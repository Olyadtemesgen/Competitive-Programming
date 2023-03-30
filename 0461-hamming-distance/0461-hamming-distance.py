class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        answer = 0
        
        while x and y:
            
            
            answer += x % 2 ^ y % 2
            
            x //= 2
            y //= 2
        
        while x:
            
            
            answer += x % 2
            x //= 2
        
        while y:  
            answer += y % 2
            y //= 2
        
        return answer