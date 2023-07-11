class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        increasing = 1
        decreasing = 1
        
        for index in range(1, len(nums)):
            
            if nums[index] < nums[index - 1]:
                increasing = decreasing + 1
            
            elif nums[index] > nums[index - 1]:
                decreasing = increasing + 1
            
        return max(increasing, decreasing)