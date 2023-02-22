class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        numss = nums.copy()
        
        nums.sort()
        
        left = 0
        right = len(nums) - 1
        
        while left < len(nums) and nums[left] == numss[left]:
            left += 1
            
        while right > left and nums[right] == numss[right]:
            right -= 1
        
        return right - left + 1