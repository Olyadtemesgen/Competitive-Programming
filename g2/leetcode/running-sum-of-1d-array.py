class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for x in range(1, len(nums)):nums[x] += nums[x - 1]
        return nums