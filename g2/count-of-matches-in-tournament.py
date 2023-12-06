class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        answer = 0

        while n - 1:
            if n % 2:
                n = (n - 1) // 2 + 1
                answer += n - 1
            else:
                n = (n // 2)
                answer += n
            

        return answer