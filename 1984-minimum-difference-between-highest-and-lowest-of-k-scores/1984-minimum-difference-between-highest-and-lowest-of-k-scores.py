class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        left = 0
        right = k - 1
        minimums = float("inf")
        
        while right < len(nums):
            
            minimums = min(minimums, nums[right] - nums[left])
            
            right += 1
            left += 1
        
        return minimums