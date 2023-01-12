class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        returned = 0
        for row in range(len(strs[0])):
            
            for column in range(len(strs) - 1):
                         
                if strs[column][row] > strs[column + 1][row]:
                    
                    returned += 1
                    break
                         
        return returned