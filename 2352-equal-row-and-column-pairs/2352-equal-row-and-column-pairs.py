class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        answer = 0
        
        for row in grid:
            for index in range(len(grid)):
               
                flag = True
                for col in range(len(row)):
                    
                    if row[col] != grid[col][index]:
                        flag = False
                
                if flag:
                    answer += 1

        
        return answer