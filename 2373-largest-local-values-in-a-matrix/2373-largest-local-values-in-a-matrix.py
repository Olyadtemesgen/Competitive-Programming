class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        down = 2
        
        row_len = len(grid)
        col_len = len(grid[0])
        
        column = 0
        result = []
        for x in range(row_len - 2):
            result.append([])
        
        while column < col_len - 2:
            row = 0
            while row < row_len - 2:
                
                maximum = 0
                
                for x in range(row, row + 3):
                    maximum = max(maximum, max(grid[x][column:column + 3]))
                
                result[row].append(maximum)
                row += 1
            column += 1
        
        return result