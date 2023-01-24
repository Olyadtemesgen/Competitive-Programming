class Solution(object):
    
    def validator(self, a, b, grids):
        
        flag = sum(grids[a][b:b + 3])
        
        for x in range(a, a + 3):
            
            if sum(grids[x][b:b + 3]) != flag:
                return False
        
        counter = defaultdict(int)
        
        for x in range(b, b + 3):
            
            summ = 0
            for y in range(a, a + 3):

                if counter[grids[y][x]] or grids[y][x] not in range(1, 10):
                    return False
                else:
                    counter[grids[y][x]] += 1

                summ += grids[y][x]
                
            if summ != flag:
                return False
            
        if grids[a][b] + grids[a + 1][b + 1] + grids[a + 2][b + 2] != flag:
            return False
        
        elif grids[a][b + 2] + grids[a + 1][b + 1] + grids[a + 2][b] != flag:
            return False
        
        return True
    
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_len = len(grid)
        col_len = len(grid[0])
        answer = 0
        
        if row_len < 3 or col_len < 3:
            return answer
        
        for row in range(row_len - 2):

            for column in range(col_len - 2):

                if self.validator(row, column, grid):
                    answer += 1

        return answer