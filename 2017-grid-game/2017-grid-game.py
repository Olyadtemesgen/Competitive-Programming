class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        
        for row in range(2):
            
            for col in range(1, len(grid[0])):
                grid[row][col] += grid[row][col - 1]
            
        
        
        result = 0
        for row in range(len(grid[0])):
            
            if not row:
                result = grid[0][-1] - grid[0][0]

            elif row < len(grid[0]) - 1:
                
                result = min(result, max(grid[1][row - 1], grid[0][-1] - grid[0][row] ))
            
            else:
                result = min(result, grid[1][-2])
        
        return result