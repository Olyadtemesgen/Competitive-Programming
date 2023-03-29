class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        
        for x in range(n + 1):
            
            ans = 0
            
            while x:
                ans += (x % 2)
                x //= 2
            
            result.append(ans)
        
        return result