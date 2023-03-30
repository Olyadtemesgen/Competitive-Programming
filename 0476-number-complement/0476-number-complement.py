class Solution:
    def findComplement(self, num: int) -> int:
        
        answer = 0

        index = 0
        
        while num:
            
            answer += (1 - num % 2) * 2 ** index
            num //= 2
            index += 1
            
        return answer