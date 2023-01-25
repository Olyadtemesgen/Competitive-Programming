class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        
        result = sorted(nums)
        
        for index, value in enumerate(nums):
            
            nums[index] = result.index(value)
        
        return nums