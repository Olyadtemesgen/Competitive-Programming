class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        demo = {}
        self.minimum = inf
        
        def dp(row, col):
            
            if row == len(triangle) - 1:
                return triangle[row][col]
            
            if (row, col) in demo:
                return demo[(row, col)]
            
            demo[row, col] = min(dp(row + 1, col), dp(row + 1, col + 1)) + triangle[row][col]         
            
            return demo[row, col]
        
        return dp(0, 0)