class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        answer = 0
        
        columns = []
        for index, row in enumerate(grid):
            
            column = []
            for col in range(len(row)):
                column.append(grid[col][index])
            
            columns.append(column)
        
        for column in columns:
            
            for row in grid:
                if column == row:
                    answer += 1
        
        return answer