class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        left = 0
        maxi = 1 if nums else 0
        for right in range(1, len(nums)):
            if nums[right] - nums[right - 1] != 1 and nums[right] - nums[right - 1] != 0:
                left = right
            elif nums[right] - nums[right - 1] == 0:
                left += 1
            
            maxi = max(maxi, right - left + 1)
        
        return maxi
                