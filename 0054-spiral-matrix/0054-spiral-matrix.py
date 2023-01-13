class Solution:
    
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        
        result = []
        
        row = 0
        column = 0
        
        row_finder_r = len(matrix)
        column_finder_r = len(matrix[0])
        length = len(matrix) * len(matrix[0])
        column_finder_l = 0
        row_finder_l = 0
        counter = 0
        while True:

            first = False
            second = False
            third = False
            fourth = False
            
            while len(result) < length and column < column_finder_r:
            
                result.append(matrix[row][column])
                column += 1
                first = True
            
            if first:
                column -= 1
                row += 1
            
            while len(result) < length and row < row_finder_r:
                result.append(matrix[row][column])
                row += 1
                second = True
            
            if second:
                column -= 1
                row -= 1
            
            while len(result) < length and column >= column_finder_l:
                result.append(matrix[row][column])
                column -= 1
                third = True
            
            
            if third:
                column += 1
                row -= 1
            
            while len(result) < length and row > row_finder_l:
                result.append(matrix[row][column])
                row -= 1
                fourth = True
    
            
            row += 1
            column += 1

            row_finder_l += 1
            column_finder_l += 1

            row_finder_r -= 1
            column_finder_r -= 1
            counter += 1
            
            if not (first and second and third and fourth):
                break
        
        return result