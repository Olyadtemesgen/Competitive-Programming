class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        l, r, res = 0, 0, 0
        summ = 1
        others = 0
        if not 0 in set(nums):
            return len(nums) - 1
        if not 1 in set(nums):
            return 0
        for r in range(len(nums)):
            if not summ and not nums[r]:
                l = others + 1
            if not nums[r]:
                others = r
            if not nums[r] and summ:
                summ = 0
            res = max(res, r - l + summ)
        return res