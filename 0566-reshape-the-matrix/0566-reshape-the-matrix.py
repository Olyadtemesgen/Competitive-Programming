class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        row = len(mat)
        column = len(mat[0])
        
        length = row * column
        
        if length != r * c or length / r != c:
            return mat
        
        row_p = 0
        col_p = 0
        answer = []
        cc = c
        while row_p < row:
            rows = []
            while cc:
                
                if col_p == column:
                    col_p = 0
                    row_p += 1
                if row_p == row:
                    break
                rows.append(mat[row_p][col_p])
                cc -= 1
                col_p += 1
                
            
            cc = c
            if rows:
                answer.append(rows)
        
        return answer