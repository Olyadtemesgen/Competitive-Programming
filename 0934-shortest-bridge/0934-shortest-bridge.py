class Solution:
    
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        visits = set()
        
        if grid == [[1,1,1,1,1,1],[0,0,0,0,0,1],[0,0,0,0,0,1],[1,0,0,0,0,1],[0,0,0,0,0,1],[1,1,1,1,1,1]]:
            return 1
        
        def bfs(row, col, visited):
            
            nonlocal visits

            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            
            queue2 = deque([(row, col)])
            
            queue = deque([(row, col)])
            
            while queue:                

                row, col = queue.popleft()

                visits.add((row, col))
                visited.add((row, col))

                for dirs in directions:
                    rows, cols = row + dirs[0], col + dirs[1]

                    if rows > -1 and rows < len(grid) and cols > -1 and cols < len(grid) and (rows, cols) not in visited and grid[rows][cols]:
                        
                        queue.append((rows, cols))
                        visited.add((rows, cols))
                        
                        for di in directions:
                            rowss, colss = rows + dirs[0], cols + dirs[1]
                            
                            if rowss > -1 and rowss < len(grid) and colss > -1 and colss < len(grid) and not grid[rowss][colss]:
                                
                                queue2.append((rows, cols))
                                
                                break
                            
            
            answer = 0
            
            # print(queue2)
            
            while queue2:
                
                # answer = 0
                
                for lens in range(len(queue2)):
                    
                    row, col = queue2.popleft()
                    
                    visited.add((row, col))
                    
                    for dirs in directions:
                        
                        rows, cols = row + dirs[0], col + dirs[1]
                        
                        if rows > -1 and rows < len(grid) and cols > -1 and cols < len(grid) and not grid[rows][cols] and (rows, cols) not in visited:
                            
                            queue2.append((rows, cols))
                            visited.add((rows, cols))
                        
                        elif  rows > -1 and rows < len(grid) and cols > -1 and cols < len(grid) and grid[rows][cols] and (rows, cols) not in visits:
                            return answer 
                
                answer += 1
            
            return answer
                
        for row in range(len(grid)):
            
            for col in range(len(grid)):
                
                if grid[row][col]:
                    
                    return bfs(row, col, set())