class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        index = 0
        res = 0
        ans = 1
        
        while n > res:
            res += ans
            ans += 1
        
        if res == n:
            return ans - 1
        else:
            return ans - 2