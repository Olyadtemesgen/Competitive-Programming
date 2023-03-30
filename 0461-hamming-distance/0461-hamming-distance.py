class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        answer = 0
        
        while x and y:
            
            if x % 2 + y % 2 == 1:
                answer += 1
            
            x //= 2
            y //= 2
        
        while x:
            
            if x % 2:
                answer += 1
            
            x //= 2
        
        while y:
            if y % 2:
                answer += 1
            
            y //= 2
        
        return answer