class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0]:
            return -1

        queue = deque([(0, 0)])
        visited = set()
        visited.add(0)
        
        length = 1
        
        while queue:
            
            lengs = len(queue)
            
            for lens in range(lengs):
                
                row , col = queue.popleft()
                
                if  (row, col) == (len(grid) - 1, len(grid) - 1):
                    return length

                if row < len(grid) - 1 and col < len(grid) - 1 and not grid[row + 1][col + 1] and ((row + 1)*len(grid) + col + 1) not in visited:
                    queue.append((row + 1, col + 1))
                    visited.add(((row + 1)*len(grid) + col + 1))

                if row < len(grid) - 1 and not grid[row + 1][col] and (row + 1)*len(grid) + col not in visited:
                    queue.append((row + 1, col))
                    visited.add(((row + 1)*len(grid) + col))
                
                if col < len(grid) - 1 and not grid[row][col + 1] and ((row)*len(grid) + col + 1) not in visited:
                    queue.append((row, col + 1))
                    visited.add(((row)*len(grid) + col + 1))
                
                if row and not grid[row - 1][col] and (row - 1)*len(grid) + col not in visited:
                    queue.append((row - 1, col))
                    visited.add(((row - 1)*len(grid) + col))
                
                if col and not grid[row][col - 1] and (row)*len(grid) + col - 1 not in visited:
                    queue.append((row, col - 1))
                    visited.add((row)*len(grid) + col - 1)
                
                if col < len(grid) - 1 and row and not grid[row - 1][col + 1] and (row - 1)*len(grid) + col + 1 not in visited:
                    queue.append((row - 1, col + 1))
                    visited.add((row - 1)*len(grid) + col + 1)
                
                if col and row < len(grid) - 1 and not grid[row + 1][col - 1] and (row + 1)*len(grid) + col - 1 not in visited:
                    queue.append((row + 1, col - 1))
                    visited.add((row + 1)*len(grid) + col - 1)
                
                if col and row and not grid[row - 1][col - 1] and (row - 1)*len(grid) + col - 1 not in visited:
                    queue.append((row - 1, col - 1))
                    visited.add((row - 1)*len(grid) + col - 1)

            # print(queue, length)
            
            length += 1
        
        return -1