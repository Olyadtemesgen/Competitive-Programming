class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        dict = {0:0 , 1: 1}
        
        if n in dict:
            return n
               
        maximum = 0
        
        for ind in range(2, n + 1):
            
            if ind % 2:
                dict[ind] = dict[ind // 2] + dict[ind // 2 + 1]
            
            else:
                dict[ind] = dict[ind // 2]
            
            maximum = max(dict[ind], maximum)

        
        return maximum