class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        nums.sort()
        
        if len(nums) < 4:
            return 0
        
        lens = len(nums) - 4
        x = 0
        minimum = inf
        
        for xx in range(4):
            
            minimum = min(minimum, nums[lens] - nums[x])
            lens += 1
            x += 1
            
        return(minimum)