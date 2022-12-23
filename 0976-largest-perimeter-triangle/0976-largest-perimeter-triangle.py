class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()
        length = len(nums)
        
        for last in range(length - 1, 1, -1):
            if (nums[last] < nums[last - 1] + nums[last - 2]):
                return nums[last - 1] + nums[last - 2] + nums[last]
        
        return 0
            