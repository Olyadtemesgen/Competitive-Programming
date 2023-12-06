class Solution:
    def totalMoney(self, n: int) -> int:
        
        week = n // 7 + (n % 7 != 0)
        answer = 0

        for w in range(week):
            if n < 7:
                
                answer += n* (w + 1 + w + n) // 2
                
                n = 0
            
            else:
                answer += 7 * (w + 1 + w + 7)// 2
                
                n -= 7
        return answer