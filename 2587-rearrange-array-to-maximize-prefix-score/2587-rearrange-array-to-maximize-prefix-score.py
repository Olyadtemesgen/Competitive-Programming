class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        nums.sort(reverse=True)
        
        
        for x in range(1, len(nums)):
            nums[x] += nums[x - 1]
            
        for x in range(len(nums)):
            if nums[x] < 1:
                return x
        
        return len(nums)