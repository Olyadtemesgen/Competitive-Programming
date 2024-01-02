class Solution:
    def moveZeroes(self, nums):
        
        left = 0
        right = 0
        
        while right < len(nums):
            
            while left < right and nums[left]:
                left += 1
            
            while right < len(nums) and not nums[right]:
                right += 1
            
            if right < len(nums):
                nums[left], nums[right] = nums[right], nums[left]
            
            right += 1
        return nums