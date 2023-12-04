class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        right = 0
        maxx = right

        while right < len(nums):
            if nums[right] == 1:
                right += 1
                maxx = max(maxx, right - left)
            
            else:
                right += 1
                left = right
        
        return maxx