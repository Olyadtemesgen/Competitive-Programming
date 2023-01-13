class Solution:
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        column_length = len(matrix[0])
        row_len = len(matrix)
        
        left = 0
        right = (column_length * row_len) - 1
        
        while left <= right:
            
            current = (left + right) // 2
            print('The current', current)
            curr_row = current // column_length
            curr_col = current % column_length
            
            if matrix[curr_row][curr_col] == target:
            
                return True
            
            elif matrix[curr_row][curr_col] > target:
                
                right = current - 1
            
            else:
                
                left = current + 1
        
        return False