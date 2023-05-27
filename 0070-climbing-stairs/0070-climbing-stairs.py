class Solution:
    def climbStairs(self, n: int) -> int:

        dict = {1:1, 2: 2}
        
        for x in range(3, n + 1):
            
            dict[x] = dict[x - 1] + dict[x - 2]
        
        return dict[n]