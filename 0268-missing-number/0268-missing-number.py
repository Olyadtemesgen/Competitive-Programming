class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maximum = max(nums)
        for x in range(maximum):
            if x not in nums:
                return x
                
        return maximum + 1