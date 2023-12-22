class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for index, x in enumerate(matrix):
            matrix[index] = x[::-1]
        for x in range(n):
            
            for y in range(x, n):
                
                matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]
        print((matrix))
        for x in range(n // 2):
            matrix[x], matrix[n - x - 1] = matrix[n - x - 1][::-1], matrix[x][::-1]
        
        if n % 2:
            matrix[n // 2] = matrix[n // 2][::-1]