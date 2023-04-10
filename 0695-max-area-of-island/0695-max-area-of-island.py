class Solution:
    
    def __init__(self):
        self.isvisited = set()
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maximum = 0
        answer = 0
        def dfs(row, col, visited):
            
            nonlocal maximum
            nonlocal answer
            
            index = row * len(grid[0]) + col
            
            
            if index in visited or  0 > row or row >= len(grid)  or 0 > col or col >= len(grid[0]) or  not grid[row][col] or index < 0:
                maximum = max(answer, maximum)
                return
            
            if grid[row][col]:
                answer += 1
                
            visited.add(index)
            self.isvisited.add(index)
  
            dfs(row + 1, col,  visited)
            dfs(row - 1, col,  visited)
            dfs(row, col + 1,  visited)
            dfs(row, col - 1, visited)
            
            
            
        for row in range(len(grid)):
            
            for col in range(len(grid[0])):
                
                index = row * len(grid[0]) + col
                
                if grid[row][col] and index not in self.isvisited:
 
                    answer = 0
                    dfs(row, col, set())
        
        return maximum