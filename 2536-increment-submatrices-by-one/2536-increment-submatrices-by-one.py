class Solution:
    
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        
        matrix = [[0 for x in range(n)] for y in range(n)]
        
        for rectangle in queries:
            
            matrix[rectangle[0]][rectangle[1]] += 1
            
            if rectangle[3] < n - 1:
                matrix[rectangle[0]][rectangle[3] + 1] -= 1
            
            if rectangle[2] < n - 1:
                matrix[rectangle[2] + 1][rectangle[1]] -= 1
            
            if rectangle[2] < n - 1 and rectangle[3] < n - 1:
                matrix[rectangle[2] + 1][rectangle[3] + 1] += 1
            
        for row in range(n):
            for col in range(1, n):
                matrix[row][col] += matrix[row][col - 1]
            
        for col in range( n):
            for row in range(1, n):
                matrix[row][col] += matrix[row - 1][col]
        
        return matrix
                