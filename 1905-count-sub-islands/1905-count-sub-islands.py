class Solution:
    
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        
        answer = set()
        
        def dfs(row, col, visited):
            
            nonlocal ans
            nonlocal answer
            
            value = row * len(grid1[0]) + col
            
            if row < 0 or col < 0 or row >= len(grid1) or col >= len(grid1[0]) or not ans:
                return
            
            if grid2[row][col] and not grid1[row][col]:
                ans = False    
                return
            
            if not grid2[row][col]:
                return
            if value in visited:
                return
            answer.add(value)
            visited.add(value)
            dfs(row + 1, col, visited)
            dfs(row - 1, col, visited)
            dfs(row, col + 1, visited)
            dfs(row, col - 1, visited)
        
        total = 0
        for row in range(len(grid1)):
            
            for col in range(len(grid1[0])):
                
                value = row * len(grid1[0]) + col
                
                if grid2[row][col] and grid1[row][col] and value not in answer:
                    
                    ans = True
                    
                    dfs(row, col, set())
                    
                    if ans:
                        total += 1
        return total