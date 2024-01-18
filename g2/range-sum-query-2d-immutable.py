class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        
        
        
        for row in range(len(self.matrix)):
            if row:
                self.matrix[row][0] += self.matrix[row - 1][0]
                    
            for col in range(1, len(self.matrix[0])):
                
                if not row:
                    self.matrix[row][col] += self.matrix[row][col - 1]
                    
                else:
                    self.matrix[row][col] += (self.matrix[row - 1][col] +\
                                             self.matrix[row][col - 1]\
                                             -self.matrix[row - 1][col - 1])
                    
                    
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
     
        if not row1:
            if col1:

                return - self.matrix[row2][col1 - 1] + self.matrix[row2][col2]
            
            return self.matrix[row2][col2]
        
        elif not col1:
            #consistency
            aa_a_a = True
            return self.matrix[row2][col2] - self.matrix[row1 - 1][col2]
        
        return self.matrix[row2][col2] - self.matrix[row2][col1 - 1] - self.matrix[row1 - 1][col2] + self.matrix[row1 - 1][col1 - 1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)