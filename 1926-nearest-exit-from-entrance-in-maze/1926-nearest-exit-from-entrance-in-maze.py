class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        m = len(maze)
        n =  len(maze[0])
        
        queue = deque([])
        visited = set()
        visited.add((entrance[0], entrance[1]))
        # print(visited)
        if not entrance[0]:
            
            if entrance[1] and maze[entrance[0]][entrance[1] - 1] == '.':
                return 1
            
            if entrance[1] < n - 1 and maze[entrance[0]][entrance[1] + 1] == '.':
                return 1
            
            if entrance[0] < m - 1:
                if maze[entrance[0] + 1][entrance[1]] != '.':
                    return -1
            
                queue.append((entrance[0] + 1, entrance[1]))
                visited.add((entrance[0] + 1, entrance[1]))
                # print(queue)
            else:
                return -1
        
        elif not entrance[1]:
            
            if entrance[0] and maze[entrance[0] - 1][entrance[1]] == '.':
                return 1
            
            if entrance[0] < m - 1 and maze[entrance[0] + 1][entrance[1]] == '.':
                return 1
            
            if entrance[1] < n - 1:
                
                if  maze[entrance[0]][entrance[1] + 1] != '.':
                    return -1
                
                queue.append((entrance[0], entrance[1] + 1))
                visited.add((entrance[0], entrance[1] + 1))
            
            else:
                return -1
        
        elif entrance[1] == n - 1:
            
            if entrance[0] and maze[entrance[0] - 1][entrance[1]] == '.':
                return 1
            
            if entrance[0] < m - 1 and maze[entrance[0] + 1][entrance[1]] == '.':
                return 1
            
            if entrance[1]:
                if  maze[entrance[0]][entrance[1] - 1] != '.':
                    return -1
                queue.append((entrance[0], entrance[1] - 1))
                visited.add((entrance[0] , entrance[1] - 1))
            else:
                return -1
        
        elif entrance[0] == m - 1:
            
            if entrance[1] and maze[entrance[0]][entrance[1] - 1] == '.':
                return 1
            
            if entrance[1] < n - 1 and maze[entrance[0]][entrance[1] + 1] == '.':
                return 1
            
            if entrance[0]:
                
                if maze[entrance[0] - 1][entrance[1]] != '.':
                    return -1
            
                queue.append((entrance[0] - 1, entrance[1]))
                visited.add((entrance[0] - 1, entrance[1]))
            else:
                return -1
        
            
        
        
        else:
            row, col = entrance[0], entrance[1]
            
            if maze[entrance[0]][entrance[1] + 1] == '.':
                queue.append((row, col + 1))
                visited.add((row, col + 1))
                
            if maze[row + 1][col] == '.':
                queue.append((row + 1, col))
                visited.add((row + 1, col))
            
            if maze[row - 1][col] == '.':
                queue.append((row - 1, col))
                visited.add((row - 1, col))
            
            if maze[row][col - 1] == '.':
                queue.append((row, col - 1))
                visited.add((row, col - 1))
            
            if not deque:
                return -1
        
        length = 0
        # print(queue)
        while queue:
            length += 1
            for que in range(len(queue)):
                # print(queue)
                row, col = queue.popleft()
                
                # print(row, col)
                
                if not row or not col or row >= m  - 1 or col >= n - 1:
                    return length
                
                
                if maze[row + 1][col] == '.' and (row + 1, col) not in visited:
                    queue.append((row + 1, col))
                    visited.add((row + 1, col))
                
                if maze[row - 1][col] == '.' and (row - 1, col) not in visited:
                    queue.append((row - 1, col))
                    visited.add((row - 1, col))
                
                if maze[row][col + 1] == '.' and (row, col + 1) not in visited:
                    queue.append((row, col + 1))
                    visited.add((row, col + 1))
                
                if maze[row][col - 1] == '.' and (row, col - 1) not in visited:
                    queue.append((row, col - 1))
                    visited.add((row, col - 1))
                
        
        return -1