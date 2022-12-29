class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        row_len = len(grid)
        col_len = len(grid[0])
        
        prefix_row = [[], []]
        prefix_col = [[], []]
        
        for column in range(col_len):
            
            suum = 0
            for row in range(row_len):
                suum += grid[row][column]
                
            prefix_col[0].append(col_len - suum)
            prefix_col[1].append(suum)
                
        for row in range(row_len):
            
            summ = sum(grid[row])
            
            prefix_row[0].append(row_len - summ)
            prefix_row[1].append(summ)
            
            suum = 0
        diff = [[0 for i in range(col_len)] for answer in range(row_len)]

        for row in range(row_len):
            
            for column in range(col_len):
                
                value1 = prefix_row[1][row] + prefix_col[1][column]
                value2 =  prefix_row[0][row] + prefix_col[0][column]
                
                diff[row][column] = (value1 - value2)
        return diff