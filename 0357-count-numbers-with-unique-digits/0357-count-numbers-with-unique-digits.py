class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        
        answer = [1]
        
        for x in range(1, 9):
            aa = 9
            for y in range(x - 1):
                aa *= (9 - y)
            
            answer.append(aa)
            answer[-1] += answer[-2]
        
        return answer[n]