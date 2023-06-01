class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        self.memo = {}
        
        def dp(row, col):
            
            if row == m - 1  and col == n - 1:
                return 1
            
            if row == m or col == n:
                return 0
            
            if (row, col) in self.memo:
                return self.memo[(row, col)]
            
            self.memo[(row, col)] = dp(row + 1, col) + dp(row, col + 1)
            
            return self.memo[(row, col)]
        
        return dp(0, 0)