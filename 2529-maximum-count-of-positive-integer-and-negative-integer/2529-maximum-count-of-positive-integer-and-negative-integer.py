class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        if nums[0] >= 0:
            return (len(nums) - bisect_left(nums, 1))
        
        elif nums[-1] <= 0:
            return (bisect_right(nums, -1))
        
        return(max(bisect_right(nums, -1), len(nums) - bisect_left(nums, 1)))