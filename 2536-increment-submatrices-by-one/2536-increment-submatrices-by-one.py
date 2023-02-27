class Solution:
    
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        
        matrix = [[0 for x in range(n)] for y in range(n)]
        
        for rectangle in queries:
            
            for row in range(rectangle[0] , rectangle[2] + 1):
                
                matrix[row][rectangle[1]] += 1
                
                if rectangle[3] + 1 < n:
                    matrix[row][rectangle[3] + 1] -= 1
            
        for row in range(n):
            
            for col in range(1, n):
                
                matrix[row][col] += matrix[row][col - 1]
        
        return matrix